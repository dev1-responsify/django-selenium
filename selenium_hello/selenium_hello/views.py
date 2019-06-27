from django.http import HttpResponse
from selenium import webdriver
import time



def homePageView(request):
        return HttpResponse('Hello, World!')

#driver = webdriver.Chrome("/Users/responsify/Desktop/selenium_project/drivers/chromedriver")

#driver.set_page_load_timeout(10)
#driver.get("http://google.com")
#driver.refresh()



def repeat(n):
    for i in range(n):
        driver = webdriver.Chrome("/Users/responsify/Desktop/selenium_project/drivers/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://google.com")
        driver.refresh()
      

repeat(2)
    