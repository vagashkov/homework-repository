from os import getcwd, remove
from os.path import exists

import pytest
from sqlalchemy import inspect

from homework12.models.base import engine, session
from homework12.models.homework import Homework
from homework12.models.homework_result import HomeworkResult
from homework12.models.person import Person
from homework12.task1 import create_tables, populate_tables

test_data = [
    ("person", True),
    ("homework", True),
    ("homework_result", True),
    ("tests", False)]


def test_if_dbfile_exists():
    """ delete db file if it is already exists """
    if exists(getcwd() + "/tests/homework12/main.db"):
        remove(getcwd() + "/tests/homework12/main.db")
    assert not exists(getcwd() + "/tests/homework12/main.db")


@pytest.mark.parametrize("table_name, is_existing", test_data)
def test_tables_existance(table_name, is_existing):
    """ checking three real tables and one fake for existance """
    create_tables()

    inspector = inspect(engine)
    assert inspector.has_table(table_name) == is_existing


def test_tables_records():
    """ populate tables with records and check if it
    is not empty """
    populate_tables()
    assert session.query(Person).count() > 0
    assert session.query(Homework).count() > 0
    assert session.query(HomeworkResult).count() > 0
