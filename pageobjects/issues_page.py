from selenium.webdriver.common.by import By
import allure

from pageobjects.base_page import BasePage

create_issue_button_id = "create_link"
summary_field_id = "summary"
priority_field_css = "input#priority-field"
assignee_field_id = "assignee-field"
submit_issue_button = "create-issue-submit"
error_element_css = ".content .error"
issue_dialog_id = "create-issue-dialog"
more_options_id = "opsbar-operations_more"
edit_issue_button_id = "opsbar-edit-issue_container"
update_issue_button_id = "edit-issue-submit"
cancel_issue_button_css = ".buttons-container .cancel"
search_field_id = "quickSearchInput"
issues_list_css = ".issue-list"
issues_in_list_css = ".issue-list a"


class IssuePage(BasePage):

    @allure.step
    def get_title(self):
        return self.driver.title

    @allure.step
    def create_issue(self, summary=None, priority=None, assignee=None, new_issue=True):
        if new_issue:
            self.click_elem(create_issue_button_id, By.ID)
        self.type_to_elem(summary_field_id, By.ID, summary, True)
        self.type_to_elem(priority_field_css, By.CSS_SELECTOR, priority, True, True)
        self.type_to_elem(assignee_field_id, By.ID, assignee, True, True)
        if self.presence_of_element(issue_dialog_id, By.ID):
            return False
        return True

    @allure.step
    def update_issue(self, summary=None, priority=None, assignee=None):
        self.type_to_elem(summary_field_id, By.ID, summary, True)
        self.type_to_elem(priority_field_css, By.CSS_SELECTOR, priority, True, True)
        self.type_to_elem(assignee_field_id, By.ID, assignee, True, True)
        if self.presence_of_element(issue_dialog_id, By.ID):
            return False
        return True

    @allure.step
    def open_issue_in_list(self, summary):
        self.click_elem('.issue-list [title="%s"] a' % summary, By.CSS_SELECTOR)
        self.wait_for_element(edit_issue_button_id, By.ID)
        self.click_elem(edit_issue_button_id, By.ID)

    @allure.step
    def get_issue_fields(self, close_edit=True):
        fields_data_list = []
        fields_data_list.append(self.get_field_data(summary_field_id, By.ID))
        fields_data_list.append(self.get_field_data(priority_field_css, By.CSS_SELECTOR))
        if close_edit:
            self.click_elem(cancel_issue_button_css, By.CSS_SELECTOR)
        return fields_data_list

    @allure.step
    def search_issues(self, summary):
        self.type_to_elem(search_field_id, By.ID, summary, True, True)
        self.wait_for_element(edit_issue_button_id, By.ID)
        if self.driver.find_elements(By.CSS_SELECTOR, issues_list_css):
            return len(self.count_issues(issues_in_list_css, By.CSS_SELECTOR))
        else:
            return 0

    @allure.step
    def search_nonexistent_issues(self, summary):
        self.type_to_elem(search_field_id, By.ID, summary, True, True)
        if self.driver.find_elements(By.CSS_SELECTOR, issues_list_css):
            return len(self.count_issues(issues_in_list_css, By.CSS_SELECTOR))
        else:
            return 0
