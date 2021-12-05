from homework8.task2 import TableData

# creating wrapper object for sqlite database
storage = TableData("/homework8/example.sqlite", "presidents")


def test_tabledata_len():
    """ checking for records number in presidents table """
    assert len(storage) == 3


def test_tabledata_get_record():
    """ checking for 'Yeltsin's' record in table """
    record = storage['Yeltsin']
    record_data = [record[key] for key in record.keys()]
    assert record_data == ['Yeltsin', 999, 'Russia']


def test_tabledata_in():
    """ checking for positive in example """
    assert "Yeltsin" in storage


def test_tabledata_not_in():
    """ .. and for negative too """
    assert "Bush" not in storage


def test_tabledata_iterate():
    """ checking if storage object can be iterated through """
    names_list = [row['name'] for row in storage]
    assert names_list == ['Yeltsin', 'Trump', 'Big Man Tyrone']
