import requests
import json
import allure
from src.json_fixtures import JSONFixture

username = "OlegAverkin"
password = "OlegAverkin"
base_url = "https://jira.hillel.it"
create_issue = base_url + "/rest/api/2/issue"
search_issue = base_url + "/rest/api/2/search"
modify_issue = base_url + "/rest/api/2/issue/{0}"

headers = {
    "Authorization": "Basic T2xlZ0F2ZXJraW46T2xlZ0F2ZXJraW4=",
    "Content-Type": "application/json; charset=utf8"
}

created_issues = []
j = JSONFixture()
times_rerun = []


class JiraApi:

    @allure.step
    def login(self, username, password):
        result = requests.get(base_url, auth=(username, password))
        return [result.status_code, result.headers.get("X-Seraph-LoginReason")]

    @allure.step
    def search_issue(self, issue_name, start=0, max_results=10):
        result = requests.post(search_issue, data=json.dumps(j.search_issue(issue_name, start, max_results)),
                                headers=headers)
        return result

    @allure.step
    def post_issue(self, summary, assignee, priority):
        result = requests.post(create_issue, data=json.dumps(j.create_issue(summary, assignee, priority)),
                               headers=headers)
        if result.status_code == 400:
            return result
        else:
            created_issues.append(result.json().get('id'))
            return result

    @allure.step
    def update_issue(self, issue_id, summary, assignee, priority):
        result = requests.put(modify_issue.format(issue_id), data=json.dumps(j.create_issue(summary, assignee, priority)),
                               headers=headers)
        return result

    @allure.step
    def delete_issue(self, issue_id):
        result = requests.delete(modify_issue.format(issue_id), headers=headers)
        return result

    @allure.step
    def delete_all_issues(self):
        response_codes_list = []
        for issue_id in created_issues:
            result = JiraApi.delete_issue(self, issue_id)
            response_codes_list.append(result.status_code)
        return response_codes_list

    @allure.step
    def rerun(self):
        if len(times_rerun) == 0:
            times_rerun.append(1)
            return 1
        else:
            return 2
