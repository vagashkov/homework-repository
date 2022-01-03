from homework2.task1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


def test_get_longest_diverse_words():
    """ Find 10 longest words consisting from largest amount
    of unique symbols """
    expected_result = [
                       u"unmi\u00dfverst\u00e4ndliche",
                       u"Bev\u00f6lkerungsabschub",
                       u"Kollektivschuldiger",
                       u"Werkst\u00e4ttenlandschaft",
                       u"Schicksalsfiguren",
                       u"Selbstverst\u00e4ndlich",
                       u"Fingerabdrucks",
                       u"Friedensabstimmung",
                       u"au\u00dfenpolitisch",
                       u"Seinsverdichtungen"]
    assert (get_longest_diverse_words('/homework2/data.txt',
                                      encoding="unicode-escape")
            == expected_result)


def test_get_rarest_char():
    """ Find rarest symbol for document """
    assert get_rarest_char('/homework2/data.txt',
                           encoding="unicode-escape") == u"\u203a"


def test_count_punctuation_chars():
    """ Count every punctuation char """
    assert count_punctuation_chars('/homework2/data.txt',
                                   encoding="unicode-escape") == 40208


def test_count_non_ascii_chars():
    """ Count every non ascii char """
    assert count_non_ascii_chars('/homework2/data.txt',
                                 encoding="unicode-escape") == 2972


def test_get_most_common_non_ascii_char():
    """ Find most common non ascii char for document """
    assert (get_most_common_non_ascii_char('/homework2/data.txt',
                                           encoding="unicode-escape")
            == '\u00E4')
