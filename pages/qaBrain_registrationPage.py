from playwright.sync_api import expect
class registrationPage:
    def __init__(self, page):
        self.page = page
    def goto(self):
        self.page.goto("https://practice.qabrains.com/registration")
    def fillRegistrationFrom(self,name,country,accountType,email,paaword,confirmPassword):
        self.page.locator("#name").click()
        self.page.locator("#name").fill(name)
        self.page.locator("#country").click()
        self.page.locator("#country").select_option(label=country)
        self.page.locator("#account").click()
        self.page.locator("#account").select_option(label=accountType)
        self.page.locator("#email").click()
        self.page.locator("#email").fill(email)
        self.page.locator("#password").click()
        self.page.locator("#password").fill(paaword)
        self.page.locator("#confirm_password").click()
        self.page.locator("#confirm_password").fill(confirmPassword)
    def clickSignup(self):
        self.page.locator("text=Signup").click()
    def assertSuccessfulRegistration(self):
        heading = self.page.locator("h2:text('Registration Successful')")
        expect(heading).to_have_text("Registration Successful")



