from pages.login_page import LoginPage
import pytest
from time import sleep
from Utiilities.read_excel import get_login_data

@pytest.mark.parametrize("email,password",get_login_data())
def test_login(setup_and_teardown,email,password):
    lpp = LoginPage(setup_and_teardown)
    lpp.enter_username(email)
    sleep(1)
    lpp.enter_password(password)
    sleep(1)
    lpp.click_login()
