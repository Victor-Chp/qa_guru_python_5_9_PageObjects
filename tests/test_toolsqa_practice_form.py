import os
from selene import browser, have, command


def test_form_filling_submitting():
    browser.open('/automation-practice-form')

    browser.element('#firstName').set('Василий')
    browser.element('#lastName').set('Алибабаев')
    browser.element('#userEmail').set('alibabavas@gmail.com')
    browser.element('[name=gender][value=Male]+label').click()
    browser.element('#userNumber').set('9093335555')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys('1980')
    browser.element('.react-datepicker__month-select').send_keys('July')
    browser.element('.react-datepicker__day--011').click()

    browser.element('#subjectsInput').send_keys('English').press_enter().send_keys('Accounting').press_enter()
    browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text('Music')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, 'tests/account.png')
        )
    )

    browser.element('#currentAddress').send_keys('проспект Революции 285 - 45')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(
        'Василий Алибабаев',
        'alibabavas@gmail.com',
        'Male',
        '9093335555',
        '11 July,1980',
        'English, Accounting',
        'Music',
        'account.png',
        'проспект Революции 285 - 45',
        'Uttar Pradesh Agra'
    ))


    '''
        При таком варианте отправляется форма, т.е. нажатие "Enter" нажимает конпку "Submit"
        browser.element('#subjectsInput').send_keys('English', 'Accounting').press_enter()
    '''
    ...