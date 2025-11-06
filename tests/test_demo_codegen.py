from pages.demo_codegen import loginSauceDemo

def test_login_saucedemo(page):
    login_page = loginSauceDemo(page)
    login_page.goto()
    login_page.fillUsernamePass(page)
    login_page.clickLogin(page)
    assert page.url == "https://www.saucedemo.com/inventory.html"
