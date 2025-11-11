from pages.qaBrain_registrationPage import registrationPage

def test_registration_page(page):
    registrationPage_obj = registrationPage(page)
    registrationPage_obj.goto()
    registrationPage_obj.fillRegistrationFrom(
        name="etu mahmuda",
        country="Albania",
        accountType="Engineer",
        email="etu1@demo.com",
        paaword="password@123",
        confirmPassword="password@123"
    )
    registrationPage_obj.clickSignup()
    registrationPage_obj.assertSuccessfulRegistration()