import allure
from allure_commons.types import Severity
from selene import browser, have, be, command

import resource


@allure.tag('QA_GURU_python_10_11')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Bykat')
@allure.feature('Student Registration Form')
@allure.story('Filling registration form')
def test_filling_form():
    # student registration form
    with allure.step('Open practice-form'):
        browser.open('/automation-practice-form')

    # firstname and lastname
    with allure.step('Fill first name and Last name'):
        browser.element('#firstName').should(be.blank).type('Cortny')
    browser.element('#lastName').should(be.blank).type('Love')
    # email
    with allure.step('Fill email'):
        browser.element('#userEmail').should(be.blank).type('CLU@mail.com')
    # gender
    with allure.step('Choose gender'):
        browser.element('[for="gender-radio-2"]').click()
    # mobile phone number
    with allure.step('Fill phone number'):
        browser.element('#userNumber').should(be.blank).type('3133265290')
    # date of birth
    with allure.step('Fill date of birth'):
        browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element(f'option[value="7"]').click()
    browser.element('.react-datepicker__year-select').element(f'option[value="1991"]').click()
    browser.element('.react-datepicker__day--029:not(.react-datepicker__day--outside-month)').click()
    # subject
    with allure.step('Fill subjects'):
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('Maths').press_enter()
    # hobbie
    with allure.step('Choose hobbies'):
        browser.element("label[for='hobbies-checkbox-2']").click()
    # picture
    with allure.step('Upload picture'):
        browser.element('#uploadPicture').send_keys(resource.path('image.jpg'))
    # current address
    with allure.step('Fill current address'):
        browser.element('#currentAddress').type('Javakhishvili St, 47, ap 39')
    # state and city
    with allure.step('Fill State and City'):
        browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').perform(command.js.click)
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').perform(command.js.click)

    # submit application
    with allure.step('Submit'):
        browser.element('#submit').perform(command.js.click)

    # results checking
    with allure.step('Check data correctness after registration'):
        browser.element('.table').all('td').even.should(have.exact_texts(
            'Cortny Love',
            'CLU@mail.com',
            'Female',
            '3133265290',
            '29 August,1991',
            'Maths',
            'Reading',
            'image.jpg',
            'Javakhishvili St, 47, ap 39',
            'NCR Noida'))