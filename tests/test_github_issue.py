from selene import browser, by, be


def test_github_issue():
    browser.open('/')
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#76")).should(be.visible)
