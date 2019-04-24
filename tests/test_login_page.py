from pageobjects.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

creds = "OlegAverkin"
fake_creds = "fake_user"
base_url = "http://jira.hillel.it:8080"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=WEBINAR"
login_title = "Log in - Hillel IT School JIRA"


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)

    def test_check_title(self):
        self.login_page.open(auth_url)
        assert self.login_page.get_title() == login_title

    def test_login_with_wrong_password(self):
        self.login_page.open(auth_url)
        self.login_page.login_to_jira(creds, fake_creds)
        assert self.login_page.get_title() == login_title

    def test_login_with_wrong_username(self):
        self.login_page.open(auth_url)
        self.login_page.login_to_jira(creds, fake_creds)
        assert self.login_page.get_title() == login_title

    def test_login_with_correct_credentials(self):
        self.login_page.open(auth_url)
        self.login_page.login_to_jira(creds, creds)
        assert self.login_page.on_page() is True

    def teardown_method(self):
        self.driver.close()
