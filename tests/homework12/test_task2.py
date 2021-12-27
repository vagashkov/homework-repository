from os import getcwd
from os.path import exists

from homework12.get_report import get_report_for_hw_results


def test_get_report_for_hw_results():
    """ call report generator and assert for report
    existance and content (two lines for two
    homework result records) """
    get_report_for_hw_results()
    assert exists(getcwd() + "/tests/homework12/report.csv")
    with open(getcwd() + "/tests/homework12/report.csv") as file:
        assert len(file.readlines()) == 2
