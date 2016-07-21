from vtu import results
import os
import json

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))

'''
Helper functions to ease creation of test cases.
'''


#  A helper function, not a test case.
def regular_mba_results(format):
    test_file = open(os.path.join(TESTS_DIR, 'data/regular_mba.html'))
    test_content = test_file.read()
    test_file.close()

    results_processor = results.RegularResultProcessor(usn='rajn1k4nth', output_format=format)
    dict_result = results_processor.parse_html_response(test_content)
    return results_processor.formatted_results(dict_result)


'''
Tests for MBA result.
'''


def test_regular_mba_results_as_dict():
    program_result = regular_mba_results(format='dict')
    expected_result = {'marksheet': [
        {'subject': u'Data Structures Using C (13MCA21)', 'internal': u'70', 'semester': u'2', 'external': u'49',
         'total': u'119', 'result': u'P'},
        {'subject': u'Object Oriented Programming using C++ (13MCA22)', 'semester': u'2', 'internal': u'78',
         'external': u'48', 'total': u'126', 'result': u'P'},
        {'subject': u'Operating Systems (13MCA23)', 'semester': u'2', 'internal': u'54', 'external': u'45',
         'total': u'99', 'result': u'P'},
        {'subject': u'System Programming (13MCA24)', 'semester': u'2', 'internal': u'72', 'external': u'47',
         'total': u'119', 'result': u'P'},
        {'subject': u'Database Management Systems (13MCA25)', 'semester': u'2', 'internal': u'63', 'external': u'48',
         'total': u'111', 'result': u'P'},
        {'subject': u'DataStructures Using C Lab (13MCA26)', 'semester': u'2', 'internal': u'47', 'external': u'50',
         'total': u'97', 'result': u'P'},
        {'subject': u'Database Laboratory (13MCA27)', 'semester': u'2', 'internal': u'48', 'external': u'49',
         'total': u'97', 'result': u'P'},
        {'subject': u'OOP Using C++ Laboratory (13MCA28)', 'semester': u'2', 'internal': u'48', 'external': u'50',
         'total': u'98', 'result': u'P'}],
        'usn': 'rajn1k4nth', 'total': 866, 'name': u'Rajnikanth',
        'result': u'FIRST CLASS WITH DISTINCTION'}

    assert program_result == expected_result


def test_regular_mba_results_as_json():
    program_result = regular_mba_results(format='json')
    dict_response = regular_mba_results(format='dict')
    assert sorted(program_result) == sorted(json.dumps(dict_response))
