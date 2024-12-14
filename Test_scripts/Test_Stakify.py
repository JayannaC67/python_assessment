import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
import pytest
from Page_objects.Stackify_pageobjects import Stakify_page_object


@pytest.mark.usefixtures("browser_crbt")
class Test_Stakify_e2e:

    def test_homepage_validation(self, readJson):
        homepage = Stakify_page_object(self.driver)  # Activating the driver which we have created in supporting file (qualitrix_page_object.py).
        homepage.launch_the_app(readJson['stakify_url'])
        homepage.test_validate_url(readJson)
        homepage.validate_headermenu()
        homepage.test_mouseoveraction()
        homepage.test_click_languages()
        homepage.test_click_ruby()
        homepage.test_validate_checkboxes()
        homepage.click_review_doc_link()
        homepage.test_validating_buttons()
        homepage.test_schedule_demo()
        homepage.test_fillthe_details(readJson)



