class loginSauceDemo:
    def __init__(self, page):
        self.page = page
    def goto(self):
        self.page.goto("https://www.saucedemo.com/")
    def fillUsernamePass(self, page):
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
    def clickLogin(self, page):
         page.locator("[data-test=\"login-button\"]").click()