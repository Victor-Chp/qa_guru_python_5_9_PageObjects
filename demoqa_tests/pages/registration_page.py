from selene import browser, have, command
from demoqa_tests import resource


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').set(value)

    def fill_last_name(self, value):
        browser.element('#lastName').set(value)

    def fill_email(self, value):
        browser.element('#userEmail').set(value)

    def select_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').set(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').send_keys(value).press_enter()

    def fill_hobbie(self, value):
        browser.all('#hobbiesWrapper .custom-checkbox').element_by(
            have.exact_text(value)
        ).click()

    def upload_picture(self, name):
        browser.element('#uploadPicture').send_keys(resource.path(name))

    def fill_address(self, value):
        browser.element('#currentAddress').send_keys(value)

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        user_number,
        date_of_birth,
        subjects,
        hobbies,
        picture,
        address,
        state_city,
    ):
        browser.all('.table-responsive td:nth-child(2)').should(
            have.exact_texts(
                full_name,
                email,
                gender,
                user_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_city,
            )
        )
