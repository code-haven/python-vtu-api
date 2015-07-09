import requests
from bs4 import BeautifulSoup
import re
import sys

try:
	USN = sys.argv[1]
except:
	raise Exception("USN not specified! Usage: python vturesults.py <USN>") 

BASE_URL = 'http://results.vtu.ac.in/vitavi.php'
payload = {'rid': USN, 'submit': 'SUBMIT'}
result = {}

try:
	request = requests.post(BASE_URL, payload)
except:
	raise Exception("Unable to query VTU server")

soup = BeautifulSoup(request.text)
results_table = soup.find('td', {'width': '513'})

try:
	bold_tags = results_table.findAll('b')

	italic_tags = results_table.findAll('i')
	subjects = [tag.text for tag in italic_tags]

	result['name'] = re.search(r'^[a-zA-Z\s]+', bold_tags[0].text).group(0).strip()
	result['result'] = bold_tags[3].text[10:].strip()
	result['usn'] = USN
	result['semester'] = bold_tags[2].text
	result["marksheet"] = []

	tags_with_marks = results_table.findAll('td', {'width': '60'})
	tags_with_marks = tags_with_marks[4:] # Remove 'Internal', 'External', 'Total' and 'Result'

	index = 0
	lastIndex = len(tags_with_marks)
	totalmarks = 0

	for subject in subjects:
		if index >= lastIndex:
			break

		result["marksheet"].append({
			'subject': subject,
			'internal': tags_with_marks[index].text,
			'external': tags_with_marks[index + 1].text,
			'total': tags_with_marks[index + 2].text,
			'result': re.search(r'P|F', tags_with_marks[index + 3].text).group()
		})

		#Update totalmarks and tagindex
		totalmarks += int(tags_with_marks[index + 2].text)
		index += 4

	result['total'] = totalmarks


except AttributeError: 
	result['error'] = 'Results not avaliable'

print(result)
