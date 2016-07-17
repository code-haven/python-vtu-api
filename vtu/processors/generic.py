import requests
import traceback
import json


class GenericVtuResultsProcessor(object):
    """
    A generic class that has to be inherited by every processor. The 'parse_html_response' function should be implemented by
    all processors that are derived.
    """
    usn = None
    output_format = 'dict'

    def make_web_request(self):
        """
        This will make a POST request with parameters same as in the web form. The response will be a HTML document
        that should be passed on to process function, implemented in the processors that inherits this class,
        which would then convert it into a dictionary.
        """
        BASE_URL = 'http://results.vtu.ac.in/vitavi.php'
        payload = {'rid': self.usn, 'submit': 'SUBMIT'}

        if not self.usn:
            raise Exception("USN cannot be None")
        try:
            response = requests.post(BASE_URL, payload)
            return response.text
        except:
            raise Exception("Unable to query VTU server. Traceback = %s" % traceback.print_exc())

    def process(self):
        html_response = self.make_web_request()

        try:
            result_as_dictionary = self.parse_html_response(html_response=html_response)
            return self.formatted_results(result_as_dictionary)
        except AttributeError:
            raise Exception('Encountered an exception while parsing results with traceback = %s' % traceback.print_exc())

    def formatted_results(self, result_as_dictionary):
        if self.output_format == 'dict':
            return result_as_dictionary
        if self.output_format == 'json':
            return json.dumps(result_as_dictionary)

    def parse_html_response(self, html_response):
        pass