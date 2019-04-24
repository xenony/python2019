from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage

login_form_id = 'login-form-username'
password_form_id = 'login-form-password'
submit_button_id = 'login-form-submit'
login_error = "aui-message aui-message-error"
create_issue_id = "create_link"


class LoginPage(BasePage):

    def get_title(self):
        return self.driver.title

    def login_to_jira(self, login, password):
        self.type_to_elem(login_form_id, By.ID, login)
        self.type_to_elem(password_form_id, By.ID, password)
        self.click_elem(submit_button_id, By.ID)
        return self.presence_of_element(create_issue_id, By.ID)

    def on_page(self):
        return self.presence_of_element(create_issue_id, By.ID)

    def open(self, url):
        self.driver.get(url)
        return self
