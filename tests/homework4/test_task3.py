from homework4.task3 import my_precious_logger


def test_my_precious_logger_err(capsys):
    """Checking the error stream output """
    my_precious_logger('error text')
    captured = capsys.readouterr()
    assert captured.err == "error text\n"


def test_my_precious_logger_out(capsys):
    """Checking the stdout stream output """
    my_precious_logger('sample test')
    captured = capsys.readouterr()
    assert captured.out == "sample test\n"
