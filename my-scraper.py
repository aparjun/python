import scrapy
from lxml import etree
import csv
# run: scrapy runspider my-scraper.py to run this code
class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://agencyportal.irdai.gov.in/_WebService/PublicAccess/AgentLocator.asmx/LocateAgent']
    
    insurerIds = ['59', '3', '8', '10', '13', '57', '16', '17', '56', '19', '24', '25', '53', '47', '51', '50', '31', '55', '35', '34', '36', '37', '38', '4', '30', '32', '44', '45', '0']
    stateIds = ['26', '1', '2', '3', '4', '27', '33', '28', '29', '30', '5', '6', '7', '8', '9', '34', '10', '11', '31', '12', '13', '14', '15', '16', '17', '18', '32', '19', '20', '21', '22', '37', '23', '24', '35', '25']
    
    def start_requests(self):
        # Headers for the POST request
        headers = {
            'authority': 'agencyportal.irdai.gov.in',
            'accept': 'application/xml, text/xml, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'path=/; ASP.NET_SessionId=5yofns4q4whfouzydnspzhiq; path=/; path=/',
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
        self.data_list = []
        for location in locations:
            form_data = {
                'page': '1',
                'rp': '9999',
                'sortname': 'AgentName',
                'sortorder': 'asc',
                'query':'',
                'qtype':'',
                'customquery': location
            }

            # Make a POST request
            yield scrapy.FormRequest(
                url='https://agencyportal.irdai.gov.in/_WebService/PublicAccess/AgentLocator.asmx/LocateAgent',  # Replace with the actual URL
                formdata=form_data,
                headers=headers,
                callback=self.parse
            )
        

    def parse(self, response):
        # Parse the XML response
        xml_content = response.body
        root = etree.fromstring(xml_content)

        # Iterate over each 'row' element
        for row in root.xpath('//row'):
            item = {
                'Agent Name': row.xpath('cell[2]/text()')[0],
                'License No': row.xpath('cell[3]/text()')[0],
                'IRDA URN': row.xpath('cell[4]/text()')[0],
                'Agent ID': row.xpath('cell[5]/text()')[0],
                'Insurance Type': row.xpath('cell[6]/text()')[0],
                'Insurer': row.xpath('cell[7]/text()')[0],
                'DP ID': row.xpath('cell[8]/text()')[0],
                'State': row.xpath('cell[9]/text()')[0],
                'District': row.xpath('cell[10]/text()')[0],
                'Pincode': row.xpath('cell[11]/text()')[0],
                'Valid From': row.xpath('cell[12]/text()')[0],
                'Valid To': row.xpath('cell[13]/text()')[0],
                'Absorbed Agent': row.xpath('cell[14]/text()')[0],
                'Phone No': row.xpath('cell[15]/text()')[0],
                'Mobile No': row.xpath('cell[16]/text()')[0], 
            }
            self.data_list.append(item)

    def closed(self, reason):
        # Save all data to CSV file when the spider is closed
        csv_file_path = 'output_combined.csv'
        self.save_to_csv(self.data_list, csv_file_path)

    def save_to_csv(self, data_list, csv_file_path):
        # Write data to CSV file
        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ['Agent Name',
                'License No',
                'IRDA URN',
                'Agent ID',
                'Insurance Type',
                'Insurer',
                'DP ID',
                'State',
                'District',
                'Pincode',
                'Valid From',
                'Valid To',
                'Absorbed Agent',
                'Phone No',
                'Mobile No', ]
            # Add more fieldnames as needed
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write data rows
            writer.writerows(data_list)

        self.log(f'Data saved to {csv_file_path}')

    custom_settings = {
        'CONCURRENT_REQUESTS': 30,  # Set the number of concurrent requests as needed
    }