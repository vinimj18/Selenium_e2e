# type: ignore

import pytest

from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)

    elif browser_name == 'edge':
        edge_options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=edge_options)

    elif browser_name == 'ie':
        ie_options = webdriver.IeOptions()
        driver = webdriver.Ie(options=ie_options)

    elif browser_name == 'safari':
        safari_options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=safari_options)

    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
