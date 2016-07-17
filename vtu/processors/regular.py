from vtu.processors.generic import GenericVtuResultsProcessor
import re
from bs4 import BeautifulSoup


class RegularResultProcessor(GenericVtuResultsProcessor):
    """
    Handles requests for regular results without backlogs.
    """
    def __init__(self, usn, output_format):
        self.usn = usn
        self.output_format = output_format

    def parse_html_response(self, html_response):
        result = {}

        soup = BeautifulSoup(html_response, 'html.parser')
        results_table = soup.find('td', {'width': '513'})
        bold_tags = results_table.findAll('b')

        italic_tags = results_table.findAll('i')
        subjects = [tag.text for tag in italic_tags]

        result['name'] = re.search(r'^[a-zA-Z\s]+', bold_tags[0].text).group(0).strip()
        result['result'] = bold_tags[3].text[10:].strip()
        result['usn'] = self.usn
        result['semester'] = bold_tags[2].text
        result["marksheet"] = []

        tags_with_marks = results_table.findAll('td', {'width': '60'})
        tags_with_marks = tags_with_marks[4:]  # Remove 'Internal', 'External', 'Total' and 'Result'

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

            # Update totalmarks and tagindex
            totalmarks += int(tags_with_marks[index + 2].text)
            index += 4

        result['total'] = totalmarks
        return result
