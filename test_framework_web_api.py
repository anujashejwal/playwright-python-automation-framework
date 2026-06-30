#1. Read users from JSON
#2. Run same test for each user
#3. Do Log in + order validation

import json
import os

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIutils


print("Current Working Directory:", os.getcwd())
#json file -> util->access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    print("Loaded JSON:", test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials",user_credentials_list)  #Run this test multiple times Each time with different data
#pytest converts this into-> test(user_credentials = {"userEmail": "user1", "userPassword": "pass1"}) and test(user_credentials = {"userEmail": "user2", "userPassword": "pass2"})
def test_e2e_web_api(playwright:Playwright,browserInstance, user_credentials):
    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    # Playwright gives access to browser, context & request and playwright is passed into this function
    # ":" type annotation, "is type of"
    # The variable playwright should be of type Playwright
    # playwright is coming from Playwright class
    # Playwright class is coming from sync api
    # sync_api is coming from the pytest-playwright package that we installed

#1. Open Browser
#2. Call API method (Create Order -> orderId)
#3. Login via UI
#4. Navigate to Orders Page
#5. Select Specific Order
#6. Verify Order Details

    #Call the API to create an order and store the returned order ID in "orderId”
    api_utils = APIutils() #creates object of APIutils class to call any method of APIutils class
    orderId = api_utils.createOrder(playwright,user_credentials)

#Creates object of API class
#        ↓
#Calls createOrder()
#        ↓
#Login API → get token
#        ↓
#Create order API
#        ↓
#Returns orderId

    loginPage = LoginPage(browserInstance) #object for loginPage class
    loginPage.navigate()
    dashboardPage = loginPage.login(userEmail,userPassword)

    #Orders History page -> order is present
    #if userEmail == "rahulshetty@gmail.com":
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderHistoryPage.selectOrder(orderId)

#command : pytest test_framework_web_api.py --browser_name firefox/chrome
#command : pytest --browser_name chrome -m smoke -n 3 --tracing on --html=report.html
#upload zip on "trace.playwright.dev"

#JSON → user_credentials_list
#        ↓
#pytest.parametrize
#        ↓
#test runs multiple times
#        ↓
#browserInstance fixture creates fresh browser
#        ↓
#API creates order (backend)
#        ↓
#UI logs in
#        ↓
#Order validation (only for valid user)

