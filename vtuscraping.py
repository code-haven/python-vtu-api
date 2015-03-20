import requests
from bs4 import BeautifulSoup
import re


BASE_URL = 'http://results.vtu.ac.in/vitavi.php'
USN = '1pe11cs003'
payload = {'rid': USN, 'submit': 'SUBMIT'}
result = {}

request = requests.post(BASE_URL, payload)
soup = BeautifulSoup(request.text)

results_table = soup.find('td', {'width': '513'})

try:
	bold_tags = results_table.findAll('b')

	result['name'] = re.search(r'^[a-zA-Z\s]+', bold_tags[0].text).group(0).strip()

	result['usn'] = USN
	result['semester'] = bold_tags[2].text

except AttributeError: 
	result['error'] = 'Results not avaliable'

print(result)
