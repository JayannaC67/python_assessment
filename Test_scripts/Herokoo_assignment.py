import itertools

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (assuming you're using Chrome, change if using Firefox, etc.)
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update with the correct path
class Herokoo_assignment:
    def Launch_herokoo(self):

        global driver # making driver as global variable
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.get("https://the-internet.herokuapp.com/") # Using ".get" we can launch the URL.
        driver.maximize_window()
        time.sleep(5)


    def print_links(self):

        # Find all link elements (anchor tags <a>)
        #links = driver.find_elements(By.TAG_NAME, "a")
        links=driver.find_elements(By.XPATH,"//a")
        linkss=len(driver.find_elements(By.XPATH,"//a"))
        print(linkss)


        # Extract the text from each link
        link_texts = [link.text for link in links]
        # Print the list of link texts
        print(link_texts)
        # convert to tupple
        link_texts_tuple = tuple(link_texts)
        print(link_texts_tuple)
        file_name = "link_text.txt"
        with open("link_text.txt", "w") as file:
            file.write("The home page links are:" + str(link_texts_tuple))

            # Close the browser
        driver.quit()












"""
        linkk=[]
        for i in links:
            link_name=[","]
            linkk=i.text
            print(linkk)
        return linkk
    def convert_to_tupple(self):
        homepage_links=self.print_links()
        link_texts_tuple = tuple(homepage_links)
        print(link_texts_tuple)



       

            xpath = '(//a)['+str(i)+']'
            xpath = '(//a)['+str(i)+']'
            link_name=driver.find_element(By.XPATH,xpath).text


            print(link_name)
            # convert to tupple
            #link_texts_tuple = tuple(link_name)
            #print(link_texts_tuple)

            #link_name = driver.find_element(By.XPATH, xpath).text


        # Extract the text from each link
        #link_texts = [link.text for link in links if link.text]

        # Print the list of link texts
            #print(link_name)
        #convert to tupple
            link_texts_tuple = tuple(link_name)
            print(link_texts_tuple)
            
"""







obj=Herokoo_assignment()
obj.Launch_herokoo()
obj.print_links()
