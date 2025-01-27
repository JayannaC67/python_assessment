
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
class coviddata:

    def covid_death_data(self):

        global driver
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.worldometers.info/coronavirus/")
        driver.maximize_window()
        time.sleep(5)

        #rows = driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today']/tbody/tr")
        Table_name=driver.find_elements(By.XPATH,"//table[@id='main_table_countries_today']")
        covid_cases_data = {}
        covid_death_data = {}

        country_name=driver.find_elements(By.XPATH,"//table[@id='main_table_countries_today']//tr[@role='row']//td[2]")
        Total_case=driver.find_elements(By.XPATH,"//table[@id='main_table_countries_today']//tr[@role='row']//td[3]")



        Total_countries=len(driver.find_elements(By.XPATH,"//table[@id='main_table_countries_today']//tr[@role='row']//td[2]"))
        print(Total_countries)
        Total_cases=len(driver.find_elements(By.XPATH,"//table[@id='main_table_countries_today']//tr[@role='row']//td[3]"))
        print(Total_cases)
        for i in range(len(country_name)):
            covid_cases_data[country_name[i].text]=Total_case[i].text
        return covid_cases_data

    def write_the_covid_cases_to_file(self):

        country_with_covid_cases = self.covid_death_data()
        file_name = "Total_cases.txt"
        with open("Total_cases.txt", "w") as file:

            file.write("The Covid Cases in each country are : " + "\n" + str(country_with_covid_cases) + "\n")





obj=coviddata()
obj.covid_death_data()
obj.write_the_covid_cases_to_file()