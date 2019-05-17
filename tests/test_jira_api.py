import pytest
from src.jira_api import *

api = JiraApi()


class TestSuite:

    @allure.tag('api')
    @allure.title("Login via API")
    @pytest.mark.api
    @pytest.mark.parametrize("response,expected", [
        (api.login("OlegAverkin", "fake"), [401, "AUTHENTICATED_FAILED"]),
        (api.login("fake", "OlegAverkin"), [401, "AUTHENTICATED_FAILED"]),
        (api.login("OlegAverkin", "OlegAverkin"), [200, "OK"]), ])
    def test_login_to_jira(self, response, expected):
        assert response == expected

    @allure.tag('api')
    @allure.title("Post issue")
    @pytest.mark.api
    def test_post_issue(self):
        response = api.post_issue("OA API Issue001", "OlegAverkin", "Low")
        assert response.status_code == 201

    @allure.tag('api')
    @allure.title("Update issue")
    @pytest.mark.api
    def test_update_issue(self):
        response = api.post_issue("OA API Issue002 ", "OlegAverkin", "Medium")
        issue_id = response.json().get('id')
        response_update = api.update_issue(issue_id, "OA API Issue002 Updated", "OlegAverkin", "Low")
        assert response_update.status_code == 204

    @allure.tag('api')
    @allure.title("Post multiple issues")
    @pytest.mark.api
    @pytest.mark.parametrize("response,expected", [
        (api.post_issue("OA API Issue003", "OlegAverkin", "Low"), 201),
        (api.post_issue("OA API Issue004", "OlegAverkin", "Low"), 201),
        (api.post_issue("OA API Issue005", "OlegAverkin", "Low"), 201),
        (api.post_issue("OA API Issue006", "OlegAverkin", "Low"), 201)])
    def test_post_issues(self, response, expected):
        assert response.status_code == expected

    @allure.tag('api')
    @allure.title("Missing required fields")
    @pytest.mark.api
    def test_post_issue_missing_fields(self):
        response = api.post_issue("", "OlegAverkin", "Low")
        assert response.status_code == 400
        assert response.json().get('errors').get('summary') == "You must specify a summary of the issue."

    @allure.tag('api')
    @allure.title("Long summary")
    @pytest.mark.api
    def test_post_issue_long_summary(self):
        response = api.post_issue("AO" * 256, "OlegAverkin", "Low")
        assert response.status_code == 400
        assert response.json().get('errors').get('summary') == "Summary must be less than 255 characters."

    @allure.tag('api')
    @allure.title("Test search issue")
    @pytest.mark.api
    def test_search_1_issue(self):
        response = api.search_issue("Issue001")
        assert response.status_code == 200
        assert response.json().get('total') == 1

    @allure.tag('api')
    @allure.title("Test five issue")
    @pytest.mark.api
    def test_search_5_issues(self):
        response = api.search_issue("OA")
        assert response.status_code == 200
        assert response.json().get('total') == 6

    @allure.tag('api')
    @allure.title("Test search unknown issue")
    @pytest.mark.api
    def test_search_none_issue(self):
        response = api.search_issue("somethingwrong")
        assert response.status_code == 200
        assert response.json().get('total') == 0

    @allure.tag('api')
    @allure.title("Delete all issues")
    @pytest.mark.api
    def test_delete_all_issues(self):
        response = api.delete_all_issues()
        assert len(response) == 6
