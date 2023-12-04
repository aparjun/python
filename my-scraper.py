import scrapy
from lxml import etree
import csv
import json
# run: scrapy runspider my-scraper.py to run this code
class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://agencyportal.irdai.gov.in/_WebService/PublicAccess/AgentLocator.asmx/LocateAgent']
    
    insurerIds = ['59', '3', '8', '10', '13', '57', '16', '17', '56', '19', '24', '25', '53', '47', '51', '50', '31', '55', '35', '34', '36', '37', '38', '4', '30', '32', '44', '45', '0']
    stateIds = [
        '26',
    ]
    
    def start_requests(self):
        # Headers for the POST request

        headers = {
        'authority': 'www.letsmakeaplan.org',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'ASP.NET_SessionId=am4qsndpxh4bdsjfkhlrj0yq; SC_ANALYTICS_GLOBAL_COOKIE=53009e7da0744a83abfa56330733af1f|False; visid_incap_2438554=oYiFlOOSQo67/mPGbCujl/EEbmUAAAAAQUIPAAAAAAA0SUwyLbRt17AGygA0CrxH; incap_ses_33_2438554=iAslUaDiHgaoXfRPkj11APIEbmUAAAAAYYC8Po6bLM1YWPZSGwF3fQ==; __RequestVerificationToken=3cHlUhOrJt8NR4NUNecSombJt1EOI5Ykr5fhQJ58V96PLb-iHAX3XWZVMCTXV6efWghBYrp19il7FAwu7MKy86mHJr-iec0-f2It5igRfMw1; visid_incap_2438554=oYiFlOOSQo67/mPGbCujl/EEbmUAAAAAQkIPAAAAAACAXcSwATEl426+y6FG/EBmMp1/FqaKsXO8',
        'referer': 'https://www.letsmakeaplan.org/find-a-cfp-professional?limit=10&pg=1&randomKey=597&sort=random&distance=100',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.data_list = []
        for page in range(1, 661):
            form_data = {
                'page': '1',
                'rp': '9999',
                'sortname': 'AgentName',
                'sortorder': 'asc',
                'query':'',
                'qtype':'',
                'customquery': page
            }
            
            url = "https://www.letsmakeaplan.org/api/feature/lmapprofilesearch/search?limit=100&pg=" + str(page) + "&randomKey=597&sort=random&distance=100"

            # Make a POST request
            # yield scrapy.FormRequest(
            #     url='https://agencyportal.irdai.gov.in/_WebService/PublicAccess/AgentLocator.asmx/LocateAgent',  # Replace with the actual URL
            #     formdata=form_data,
            #     headers=headers,
            #     callback=self.parse
            # )

            # Make a GET request
            yield scrapy.Request(url, callback=self.parse)
        

    def parse(self, response):
         # Parse JSON response
        data = json.loads(response.body)

        # Extract information from each result item
        for result in data.get('results', []):
            item = {
                'cst_ind_full_name_dn': result.get('cst_ind_full_name_dn'),
                'planning_services': result.get('planning_services'),
                'expertises': result.get('expertises'),
                'min_assets': result.get('min_assets'),
                'cst_org_name_dn': result.get('cst_org_name_dn'),
            }

            # Extract address information if available
            addresses = result.get('_childDocuments_', [])
            if addresses:
                address = addresses[0]  # Assuming only one address is present
                item.update({
                    'adr_line1': address.get('adr_line1'),
                    'adr_line2': address.get('adr_line2'),
                    'adr_city': address.get('adr_city'),
                    'adr_state': address.get('adr_state'),
                    'adr_post_code': address.get('adr_post_code'),
                })

            # Additional information
            item.update({
                'photoUrl': result.get('photoUrl'),
            })
            self.data_list.append(item)

    def closed(self, reason):
        # Save all data to CSV file when the spider is closed
        csv_file_path = 'output_combined.csv'
        self.save_to_csv(self.data_list, csv_file_path)

    def save_to_csv(self, data_list, csv_file_path):
        # Write data to CSV file
        with open(csv_file_path, mode='w', newline='') as csv_file:
            fieldnames = ['cst_ind_full_name_dn', 'planning_services', 'expertises', 'min_assets', 'cst_org_name_dn', 'adr_line1', 'adr_line2', 'adr_city', 'adr_state', 'adr_post_code', 'photoUrl']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write data rows
            writer.writerows(data_list)

        self.log(f'Data saved to {csv_file_path}')

    custom_settings = {
        'CONCURRENT_REQUESTS': 20,  # Set the number of concurrent requests as needed
    }