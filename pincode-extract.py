import requests
import xml.etree.ElementTree as ET
import json

def save_text_file(filename, content):
    content = list(set(content))
    file = open(filename, 'w')
    file.write(str(content))
    file.close()
    print(len(content), 'records')

filename = 'C:/Users/arjun/Desktop/my_text_file.txt'

def xml_to_json(xml_data):
    root = ET.fromstring(xml_data)
    json_data = []

    for table in root.findall('Table'):
        district_data = {}
        for child in table:
            key = child.tag
            value = child.text
            district_data[key] = value

        json_data.append(district_data)

    return json_data

url = "https://agencyportal.irdai.gov.in/_WebService/General/DataLoader.asmx/GetDistrict"

# Initialize an empty list to store the JSON data
json_data_list = []

stateIds = ['1', ]
headers = {
  'authority': 'agencyportal.irdai.gov.in',
  'accept': 'application/xml, text/xml, */*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json; charset=UTF-8',
  'cookie': 'path=/; ASP.NET_SessionId=lzl4p0hpymx5cdr0uoayy502; path=/; path=/',
  'origin': 'https://agencyportal.irdai.gov.in',
  'referer': 'https://agencyportal.irdai.gov.in/PublicAccess/AgentLocator.aspx',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

for stateId in stateIds:
  payload = "{StateID:'" + stateId + "'}"
  response = requests.request("POST", url, headers=headers, data=payload)
  if response.status_code == 200:
        # Parse the XML response into an ElementTree object
        xml_data = response.content

        # Convert the XML data to JSON
        districts = xml_to_json(xml_data)
        for district in districts:
            start_num, end_num = district['varPINCodeRange'].split("-")
            if(int(end_num) - int(start_num) > 1000):
                json_data_list.append(',,,1,,' + stateId + ',' + district['sntDistrictID'] + ',')
            for num in range(int(start_num), int(end_num) + 1):
                json_data_list.append(',,,1,,' + stateId + ',' + district['sntDistrictID'] + ',' + str(num))

        # Append the JSON data to the list

# Save the JSON data to a text file
save_text_file(filename, json_data_list)



