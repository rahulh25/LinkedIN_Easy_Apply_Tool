from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class EasyApply:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.s=Service(ChromeDriverManager().install())
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.url = 'https://www.linkedin.com'
        self.window = Tk()
        self.window['bg'] = '#232323'
        self.txt_email = Entry(self.window, borderwidth=5, width=40)
        self.txt_pwd = Entry(self.window, show="*", borderwidth=5, width=40)
        self.txt_search_criteria = Entry(self.window, borderwidth=5, width=40)

    def loadGUI(self):
        self.window.title("LinkedIN Easy Apply App")
        self.window.geometry('400x300')
        lbl_email = Label(self.window, text="Enter Email",
                          background='#232323', foreground='white')

        lbl_pwd = Label(self.window, text="Enter Password",
                        background='#232323', foreground='white')
        lbl_search_criteria = Label(
            self.window, text="Enter Search Criteria", background='#232323', foreground='white')
        submit_button = Button(self.window,
                               text="Run",
                               background='#254d70',
                               foreground='white',
                               width=25,
                               command=self.log_in_linkedin)
        lbl_email.pack()
        self.txt_email.pack(pady=5)
        lbl_pwd.pack()
        self.txt_pwd.pack(pady=5)
        lbl_search_criteria.pack()
        self.txt_search_criteria.pack(pady=5)
        submit_button.pack(pady=30)
        self.window.mainloop()

    def log_in_linkedin(self):
        self.driver = webdriver.Chrome(options=self.options,service=self.s)
        self.driver.set_page_load_timeout(30)
        self.driver.get(self.url)
        self.driver.maximize_window()
        login_email = self.driver.find_element(
            By.XPATH, '//*[@id="session_key"]')
        login_email.clear()
        login_email.send_keys(self.txt_email.get())
        login_pwd = self.driver.find_element(
            By.XPATH, '//*[@id="session_password"]')
        login_pwd.clear()
        login_pwd.send_keys(self.txt_pwd.get())
        login_pwd.send_keys(Keys.RETURN)

        time.sleep(1)
        self.searchJobs()
        time.sleep(1)
        self.filter()

    def searchJobs(self):
        job_link = self.driver.find_element(By.ID, 'ember22')
        job_link.click()
        time.sleep(1)
        search_box = self.driver.find_element(
            By.XPATH, '//input[starts-with(@id,"jobs-search-box-keyword")]')
        search_box.clear()
        search_box.send_keys(self.txt_search_criteria.get())
        time.sleep(1)
        location_box = self.driver.find_element(
            By.XPATH, '//input[starts-with(@id,"jobs-search-box-location")]')
        location_box.send_keys('United States')
        time.sleep(1)
        location_box.send_keys(Keys.RETURN)
        self.window.destroy()

    def filter(self):
        easy_apply_button = self.driver.find_element(
            By.XPATH, '//button[@aria-label="Easy Apply filter."]')
        easy_apply_button.click()


if __name__ == "__main__":
    bot = EasyApply()
    bot.loadGUI()
