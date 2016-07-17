from vtu.processors.regular import RegularResultProcessor


def get_results(usn, results_type='regular', output_format='dict'):
    """
    The entry point to get results for a given usn.
    :param usn: A unique id of a student.
    :param type: Specify the type of results. Possible values are regular, revaluation, backlog.
    """

    if results_type == 'regular':
        results = RegularResultProcessor(usn=usn, output_format=output_format).process()
    else:
        # TODO
        raise NotImplementedError('The results_type %s has not been implemented yet!.' % results_type)

    return results
