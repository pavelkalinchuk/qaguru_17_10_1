from selene import browser, by, be
import allure


def test_github_issue_steps_allure():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open('/')

    with allure.step("Ищем репозиторий eroshenkoam/allure-example"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").press_enter()

    with allure.step("Переходим в репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим на вкладку со списком проблем"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие проблемы №76 на вкладке"):
        browser.element(by.partial_text("#76")).should(be.visible)
