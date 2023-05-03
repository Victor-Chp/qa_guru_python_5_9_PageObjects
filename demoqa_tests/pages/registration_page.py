from selene import browser, have, command
from demoqa_tests import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        # return self

    def register(self, student):
        # WHEN
        browser.element('#firstName').set(student.first_name)
        browser.element('#lastName').set(student.last_name)
        browser.element('#userEmail').set(student.email)
        browser.element(f'[name=gender][value={student.genders}]+label').click()
        browser.element('#userNumber').set(student.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(
            student.date_of_birth.year
        )
        browser.element('.react-datepicker__month-select').send_keys(
            student.date_of_birth.strftime('%B')
        )
        browser.element(f'.react-datepicker__day--0{student.date_of_birth.day}').click()

        for subject in student.subjects:
            browser.element('#subjectsInput').send_keys(subject).press_tab()
        for hobby in student.hobbies:
            browser.all('#hobbiesWrapper .custom-checkbox').element_by(
                have.exact_text(hobby)
            ).click()
        browser.element('#uploadPicture').send_keys(
            resource.path(student.upload_filename)
        )

        browser.element('#currentAddress').send_keys(student.current_address)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.city)
        ).click()
        browser.element('#submit').press_enter()

    #
    # def fill_hobbie(self, value):
    #     browser.all('#hobbiesWrapper .custom-checkbox').element_by(
    #         have.exact_text(value)
    #     ).click()
    #
    # def upload_picture(self, name):
    #     browser.element('#uploadPicture').send_keys(resource.path(name))
    #
    # def fill_address(self, value):
    #     browser.element('#currentAddress').send_keys(value)
    #
    # def fill_state(self, name):
    #     self.state.perform(command.js.scroll_into_view)
    #     self.state.click()
    #     browser.all('[id^=react-select][id*=option]').element_by(
    #         have.exact_text(name)
    #     ).click()
    #
    # def fill_city(self, name):
    #     browser.element('#city').click()
    #     browser.all('[id^=react-select][id*=option]').element_by(
    #         have.exact_text(name)
    #     ).click()
    #
    # def submit(self):
    #     browser.element('#submit').press_enter()
    #
    # def should_registered_user_with(
    #     self,
    #     full_name,
    #     email,
    #     gender,
    #     user_number,
    #     date_of_birth,
    #     subjects,
    #     hobbies,
    #     picture,
    #     address,
    #     state_city,
    # ):
    #     browser.all('.table-responsive td:nth-child(2)').should(
    #         have.exact_texts(
    #             full_name,
    #             email,
    #             gender,
    #             user_number,
    #             date_of_birth,
    #             subjects,
    #             hobbies,
    #             picture,
    #             address,
    #             state_city,
    #         )
    #     )
