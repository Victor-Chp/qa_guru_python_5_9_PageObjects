from datetime import date

from selene import browser, have
from demoqa_tests import resource
from demoqa_tests.data.users import User, Gender, Subject, Hobby
from demoqa_tests.pages.registration_page import RegistrationPage


def test_form_filling_submitting():
    student = User(
        first_name='Василий',
        last_name='Алибабаев',
        email='alibabavas@gmail.com',
        genders=Gender.male.value,
        phone_number=9093335555,
        date_of_birth=date(1980, 7, 11),
        subjects=[Subject.english.value, Subject.chemistry.value, Subject.arts.value],
        hobbies=[Hobby.music.value, Hobby.reading.value],
        upload_filename='account.png',
        current_address='проспект Революции 285 - 45',
        state='Uttar Pradesh',
        city='Agra',
    )

    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.should_have_registered(student)

    ...
