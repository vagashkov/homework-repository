"""
(*) optional task: write standalone script (get_report.py)
that retrieves and stores the following information into
CSV file report.csv
for all done (completed) homeworks:
Student name (who completed homework)
Creation date
Teacher name who created homework
Utilize ORM capabilities as much as possible,
avoiding executing raw SQL queries.
"""
import csv
import os

from sqlalchemy.orm import aliased

from homework12.models.base import session
from homework12.models.homework import Homework
from homework12.models.homework_result import HomeworkResult
from homework12.models.person import Person


def get_report_for_hw_results():
    """ making join request to database and store results into csv file """
    # we need aliases to perform two request for one persons table
    student = aliased(Person, name="student")
    teacher = aliased(Person, name="teacher")
    # making request
    records = (session.query(HomeworkResult, student, Homework, teacher)
               # getting homework result author (student)
               .filter(HomeworkResult.author_id == student.person_id)
               # and homework for result
               .filter(HomeworkResult.homework_id == Homework.homework_id)
               # and homework task author (teacher)
               .filter(Homework.author_id == teacher.person_id)
               .all())
    # now we can put results into csv file
    with open(os.getcwd() + r"/tests/homework12/report.csv",
              mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        # put student name, homewotk creation date and teacher name
        for hw_res, stud, hw, teach in records:
            csv_writer.writerow((stud.first_name + " " + stud.last_name,
                                str(hw.created),
                                teach.first_name + " " + teach.last_name))
