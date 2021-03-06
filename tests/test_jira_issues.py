from pageobjects.login_page import LoginPage
from pageobjects.issues_page import IssuePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import allure
import pytest

creds = "OlegAverkin"
base_url = "http://jira.hillel.it:8080"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=WEBINAR"
my_issues = base_url + "/issues/?filter=-1"
all_issues = base_url + "/issues/?filter=-4"


class TestCreateIssue:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.issue_page = IssuePage(self.driver)
        self.login_page.open(my_issues)
        self.login_page.login_to_jira(creds, creds)

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Create issue")
    def test_create_issue(self):
        assert self.issue_page.create_issue("OA_new_issue", "Blocker", "OlegAverkin") is True

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Verify created issue")
    def test_verify_created_issue(self):
        self.issue_page.open_issue_in_list("OA_new_issue")
        assert self.issue_page.get_issue_fields() == ["OA_new_issue", "Blocker"]

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Create issue with long summary")
    def test_create_issue_with_long_summary(self):
        assert self.issue_page.create_issue("x" * 256, "Blocker", "OlegAverkin") is False

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Vreate issue with empty summary")
    def test_create_issue_with_empty_summary(self):
        assert self.issue_page.create_issue("", "Blocker", "OlegAverkin", True) is False

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Search issue")
    def test_search_issue(self):
        assert self.issue_page.search_issues("OA_new_issue") == 1

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Search nonexistent issue")
    def test_search_nonexistent_issue(self):
        assert self.issue_page.search_nonexistent_issues("somethingwrong") == 0

    @pytest.mark.ui
    @allure.tag('ui')
    @allure.title("Update issue")
    def test_update_issue(self):
        self.issue_page.open_issue_in_list("OA_new_issue")
        assert self.issue_page.update_issue("OA_updated_issue", "Low", "OlegAverkin") is True

    def teardown_method(self):
        self.driver.close()
