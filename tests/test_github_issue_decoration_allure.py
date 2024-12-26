from selene import browser, be, by
import allure


def test_github_issue_decoration_allure():
    browser_open('/')
    search_repo("eroshenkoam/allure-example")
    go_repo("eroshenkoam/allure-example")
    go_issues_tab()
    should_issue("#76")


@allure.step("Открываем главую страницу GitHub")
def browser_open(url):
    browser.open(url)


@allure.step("Ищем репозиторий eroshenkoam/allure-example")
def search_repo(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").press_enter()


@allure.step("Переходим в репозиторий")
def go_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Переходим на вкладку со списком проблем")
def go_issues_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие проблемы №76 на вкладке")
def should_issue(issue_id):
    browser.element(by.partial_text(issue_id)).should(be.visible)
