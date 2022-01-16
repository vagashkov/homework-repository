from unittest.mock import patch

from homework4.task2 import count_dots_on_i


# class to imitate HTTPResponse object
class FakeResponse(object):
    # it has status code
    status_code = 200
    # and some content
    content = "iiiiiii"

    # we need to mock it's read() method
    def read(self):
        return self.content.encode()

    # and close() method
    def close(self):
        pass


def test_count_dots_on_i_positive():
    # buiding fake response object
    fake_response = FakeResponse()
    # mocking urlopen function
    with patch('urllib.request.urlopen') as mock_urlopen:
        # and returning 'hand-crafted' response object
        mock_urlopen.return_value = fake_response
        assert count_dots_on_i('http://google.com') == 7
