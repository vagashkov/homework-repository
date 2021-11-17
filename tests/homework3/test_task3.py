from homework3.task3 import make_filter

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


def test_make_filter_by_ont_condition():
    assert make_filter(type='person').apply(sample_data) == [{
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     }]


def test_make_filter_by_two_conditions():
    assert make_filter(name='polly', type='bird').apply(sample_data) == [{
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }]
