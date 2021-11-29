from homework6.task1 import User


def test_decorated_User():
    """ Checking instances number three times:
    - before object creation
    - after three objects were created
    - after resetting the counter"""
    assert not User.get_created_instances()
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert not User.get_created_instances()
