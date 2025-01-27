import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Corona:
    def Launch_coronapp(self):

        global driver # making driver as global variable
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.get("https://www.worldometers.info/coronavirus/") # Using ".get" we can launch the URL.
        driver.maximize_window()
        time.sleep(5)


    def get_covid_count_in_each_country(self):
        Corona_virus_report_header = driver.find_element(By.XPATH, '//strong[text()="Report coronavirus cases"]')
        driver.execute_script("arguments[0].scrollIntoView();", Corona_virus_report_header)
        time.sleep(2)
        Country_names = driver.find_elements(By.XPATH, "//a[@class='mt_a']")
        total_covid_cases =driver.find_elements(By.XPATH, "//tr[.//a[@class='mt_a']]//td[3]")
        country_with_covid_cases = {}
        for i in range(len(Country_names)):
            country_with_covid_cases[Country_names[i].text] = total_covid_cases[i].text
        return country_with_covid_cases


    def write_the_covid_cases_to_file(self):
        country_with_covid_cases = self.get_covid_count_in_each_country()
        file_name = "corona.txt"
        with open("corona.txt", "w") as file:
            file.write("The Covid Cases in each country are : " + "\n" + str(country_with_covid_cases) + "\n")

'''            
            for country, cases in country_with_covid_cases.items():
                if country != "":
                    file.write(country + " : " + cases + "\n")
            file.write("The number of countries with covid cases are : " + str(len(country_with_covid_cases)))
'''




obj=Corona()
obj.Launch_coronapp()
obj.get_covid_count_in_each_country()
obj.write_the_covid_cases_to_file()


