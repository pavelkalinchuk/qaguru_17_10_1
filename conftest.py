from selene import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def browser_start():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1200
    browser.config.window_height = 800

    yield

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
