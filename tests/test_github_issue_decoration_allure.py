import allure_steps as step


def test_github_issue_decoration_allure():
    step.browser_open('/')
    step.search_repo("eroshenkoam/allure-example")
    step.go_repo("eroshenkoam/allure-example")
    step.go_issues_tab()
    step.should_issue("#76")
