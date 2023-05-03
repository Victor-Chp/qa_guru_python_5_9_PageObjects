from datetime import date

from selene import browser, have
from demoqa_tests import resource
from demoqa_tests.data.users import User, Gender, Subject, Hobby
from demoqa_tests.pages.registration_page import RegistrationPage


def test_form_filling_submitting():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Василий')
    registration_page.fill_last_name('Алибабаев')
    registration_page.fill_email('alibabavas@gmail.com')
    registration_page.select_gender('Male')
    registration_page.fill_phone_number('9093335555')
    registration_page.fill_date_of_birth('1980', 'July', '11')

    registration_page.fill_subject('English')
    registration_page.fill_subject('Accounting')
    registration_page.fill_hobbie('Music')
    registration_page.upload_picture('account.png')

    registration_page.fill_address('проспект Революции 285 - 45')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')
    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        'Василий Алибабаев',
        'alibabavas@gmail.com',
        'Male',
        '9093335555',
        '11 July,1980',
        'English, Accounting',
        'Music',
        'account.png',
        'проспект Революции 285 - 45',
        'Uttar Pradesh Agra',
    )

    ...
