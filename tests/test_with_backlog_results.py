from vtu import results
import os
import json

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))

'''
Helper functions to ease creation of test cases.
'''


#  A helper function, not a test case.
def regular_mba_results(format):
    test_file = open(os.path.join(TESTS_DIR, 'data/one_backlog_mba.html'))
    test_content = test_file.read()
    test_file.close()

    results_processor = results.RegularResultProcessor(usn='1pe15mca33', output_format=format)
    dict_result = results_processor.parse_html_response(test_content)
    return results_processor.formatted_results(dict_result)


'''
Tests for MBA result.
'''


def test_one_backlog_mba_results_as_dict():
    program_result = regular_mba_results(format='dict')
    expected_result = {'marksheet': [
        {'subject': u'Data Structures Using C (13MCA21)', 'semester': u'2', 'internal': u'44', 'external': u'42',
         'total': u'86', 'result': u'P'},
        {'subject': u'Object Oriented Programming using C++ (13MCA22)', 'semester': u'2', 'internal': u'45',
         'external': u'47', 'total': u'92', 'result': u'P'},
        {'subject': u'Operating Systems (13MCA23)', 'semester': u'2', 'internal': u'43', 'external': u'40',
         'total': u'83', 'result': u'P'},
        {'subject': u'System Programming (13MCA24)', 'semester': u'2', 'internal': u'45', 'external': u'37',
         'total': u'82', 'result': u'P'},
        {'subject': u'Database Management Systems (13MCA25)', 'semester': u'2', 'internal': u'40', 'external': u'38',
         'total': u'78', 'result': u'P'},
        {'subject': u'DataStructures Using C Lab (13MCA26)', 'semester': u'2', 'internal': u'43', 'external': u'47',
         'total': u'90', 'result': u'P'},
        {'subject': u'Database Laboratory (13MCA27)', 'semester': u'2', 'internal': u'42', 'external': u'35',
         'total': u'77', 'result': u'P'},
        {'subject': u'OOP Using C++ Laboratory (13MCA28)', 'semester': u'2', 'internal': u'38', 'external': u'48',
         'total': u'86', 'result': u'P'},
        {'subject': u'Discrete Mathematics Structure (13MCA12)', 'semester': u'1', 'internal': u'36', 'external': u'32',
         'total': u'68', 'result': u'F'},
        {'subject': u'Introduction to Unix (13MCA14)', 'semester': u'1', 'internal': u'42', 'external': u'30',
         'total': u'72', 'result': u'F'}], 'usn': '1pe15mca33', 'total': 814, 'name': u'VISVA JEET',
                       'result': u'FIRST CLASS'}
    assert program_result == expected_result


def test_one_backlog_mba_results_as_json():
    program_result = regular_mba_results(format='json')
    dict_response = regular_mba_results(format='dict')
    assert sorted(program_result) == sorted(json.dumps(dict_response))
