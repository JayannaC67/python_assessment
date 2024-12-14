from inspect import isfunction
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locatorss import Stackify_locators
import time
from Test_scripts.conftest import readJson


class Stakify_page_object:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Stakify Application is launched Successfully ... ..... PASS")
        if self.driver.find_element(By.XPATH,Stackify_locators.Stakify_logo()).is_displayed():
            print("we are in Stakify homepage")
        else:
            print("We are not in homepage")
    def test_validate_url(self,readJson):
        #url
        get_url = self.driver.current_url
        print(get_url)
        if get_url=="https://stackify.com/":
        #if get_url =='readJson([stakify_url])':
            print("valid url")
        else:
            print("Invalid url")

        get_title = self.driver.title
        print(get_title)

    def validate_headermenu(self):
        headers=self.driver.find_elements(By.XPATH,Stackify_locators.Stakify_headers())
        print(len(headers))
        for i in headers:
            print(i.text)

        total_headers = len(self.driver.find_elements(By.XPATH,Stackify_locators.Stakify_headers()))

        file = open("C:\\Users\LenT14G2ITL\\PycharmProjects\\jay_pythonbasic_learning\PT_scripts\\Text.txt", "w")

        for i in range(1, total_headers + 1):

            #xpath="Stackify_locators.Stakify_headers()['+ str(i) + ']"
            xpath = "(//ul[@id='menu-mega-menu']/li/a) [' + str(i) + ']"
            #print(xpath)

            header_name = self.driver.find_element(By.XPATH, xpath).text
            print("when the value of i is :" + str(i) + " " + "the value of the text is : " + header_name)

            file.write("when the value of i is :" + str(i) + " " + "the value of the text is : " + header_name)
            file.write("\n")
        file.close()
        print("Data is written into the file.")

    def test_mouseoveraction(self):
        element=self.driver.find_element(By.XPATH,Stackify_locators.mouseover())
        hover=ActionChains(self.driver).move_to_element(element)
        hover.perform()
        time.sleep(5)
        self.driver.find_element(By.XPATH,Stackify_locators.Bylanguage()).click()

    def test_click_languages(self):
        languages=self.driver.find_elements(By.XPATH,Stackify_locators.Bylanguage())
        print(len(languages))
    def test_click_ruby(self):
        self.driver.find_element(By.XPATH,Stackify_locators.Ruby()).click()
        time.sleep(3)
        if self.driver.find_element(By.XPATH,Stackify_locators.ruby_header()).is_displayed():
            print("ruby clicked")
        else:
            print("ruby not clicked")

        get_ruby_url = self.driver.current_url
        print(get_ruby_url)
        if get_ruby_url == "https://stackify.com/retrace-apm-ruby/":
            print("valid ruby url")
        else:
            print("Invalid ruby url")

    def test_validate_checkboxes(self):
        checkbox1 = self.driver.find_element(By.XPATH, Stackify_locators.checkbox1()).is_selected()
        time.sleep(2)
        #checkbox2 = self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").is_selected()
        print(checkbox1)
       # print(checkbox2)

    def click_review_doc_link(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")#to scroll down the page
        time.sleep(3)
        ruby_text=self.driver.find_element(By.XPATH,Stackify_locators.ruby_text()).text
        print("The value of ruby_text is :" + ruby_text)
        review_doc=self.driver.find_element(By.XPATH,Stackify_locators.reviewdoc()).text
        time.sleep(2)
        print(review_doc)
        #reviedoc.click()
        self.driver.find_element(By.XPATH,Stackify_locators.reviewdoc()).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH,Stackify_locators.reviwdocclicked()).is_displayed():
            print("review doc clicked")
        else:
            print("review doc not clicked")

        self.driver.back()
        time.sleep(3)
        if self.driver.find_element(By.XPATH,Stackify_locators.reviewdoc()).is_displayed():
            print("came back to previous page")
        else:
            print("still in review doc page")
        self.driver.execute_script("window.scrollTo(0, 5000)")  # to scroll down the page
        time.sleep(3)

    def test_validating_buttons(self):
        #to validate start free trial
        if self.driver.find_element(By.XPATH,Stackify_locators.startfree_trial()).is_displayed():
            print("Start free trial displayed")
        else:
            print("Start free trail not displayed")

        #to validate request demo button
        if self.driver.find_element(By.XPATH,Stackify_locators.requestdemo()).is_displayed():
            print("request demo button displayed")
        else:
            print("request demo button not displayed")

        self.driver.find_element(By.XPATH,Stackify_locators.requestdemo()).click()
        time.sleep(2)
        header_text=self.driver.find_element(By.XPATH,Stackify_locators.demorequest_headertext()).text
        print(header_text)
        if self.driver.find_element(By.XPATH,Stackify_locators.demorequest_headertext()).is_displayed():
            print("demo req clicked")
        else:
            print("demo req not clicked")

    def test_schedule_demo(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")  # to scroll down the page
        time.sleep(3)
        #to click schedule demo button
        self.driver.find_element(By.XPATH,Stackify_locators.schedule_demo()).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH,Stackify_locators.schedule_demo_clicked()).is_displayed():
            print("schedule demo clicked without details")
        else:
            print("schedule demo not clicked without details")

    def test_fillthe_details(self,readJson):
        self.driver.execute_script("window.scrollTo(1000, 0)")  # to scroll down the page
        time.sleep(3)

        self.driver.find_element(By.XPATH,Stackify_locators.First_name()).send_keys(readJson["First_name"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, Stackify_locators.Last_name()).send_keys(readJson["Last_name"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, Stackify_locators.Email()).send_keys(readJson["Email"])
        time.sleep(1)
        self.driver.find_element(By.XPATH, Stackify_locators.Phone()).send_keys(readJson["Phone"])
        time.sleep(1)

        select=Select(self.driver.find_element(By.XPATH,Stackify_locators.Job_roledropdown()))
        select.select_by_visible_text("Quality Assurance")
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, Stackify_locators.Industry_dropdown()))
        select.select_by_index(1)
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, Stackify_locators.Company_sizedropdown()))
        select.select_by_index(2)
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, Stackify_locators.Monitoring_tooldropdown()))
        select.select_by_index(1)
        time.sleep(2)
        select = Select(self.driver.find_element(By.XPATH, Stackify_locators.Timeline_implementation_dropdown()))
        select.select_by_index(2)
        time.sleep(2)
        self.driver.find_element(By.XPATH,Stackify_locators.Note_textfield()).send_keys(readJson["Note"])
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000)")  # to scroll down the page
        time.sleep(3)
        #checkbox
        checkbox1 = self.driver.find_element(By.XPATH, Stackify_locators.validate_checkbox()).is_selected()
        print(checkbox1)
        time.sleep(1)
        self.driver.find_element(By.XPATH,Stackify_locators.validate_checkbox()).click()
        time.sleep(1)
        checkbox2 = self.driver.find_element(By.XPATH, Stackify_locators.validate_checkbox()).is_selected()
        print(checkbox2)






