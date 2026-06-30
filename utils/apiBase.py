
#🎯 Goal: Reusable API methods (clean framework design)

#🧠 What this file does:
#getToken() → login API → returns token
#createOrder() → creates order → returns orderId

from playwright.sync_api import Playwright

ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

#Encapsulation: bundling data and method in single unit(class)
#without class def getToken and createOrder would be standalone functions with Class Everything API-related stays in one place.
class APIutils:

#1. Login via API ==> Sends login request and gets token
#def getToken - Input: playwright object, Output: Token
    def getToken(self,playwright:Playwright): #The playwright parameter should be a Playwright object
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com") #Create API context -  creates new API session
        response = api_request_context.post("api/ecom/auth/login",data={"userEmail": "rahulshettyacademy@gmail.com", "userPassword": "Iamking@000"}) #Login API call
        assert response.ok #Verify response
        print(response.json())  #to extract json to retrieve the token
        responseBody = response.json()  #convert response to json
        return responseBody["token"] #returns abc123xyz

#2. Create order via API ==> uses token -> calls orders API-> Creates order in backend
#def createOrder - Create order, Return OrderId
    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright) #login -> get Token -> store in variable
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com/client") #Create API session
        #after giving new context -> open a page
        #copy network tab element where order is created -> copy url and payload for data
        #Create Order request
        response = api_request_context.post("api/ecom/order/create-order",
                                 data=ordersPayLoad,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})
        #Headers - Without authorization server says 401 Unauthorized
        print(response.json())
        response_body = response.json() #convert response to json
        orderId = response_body["orders"][0] #Extract OrderId -> ORDER12345
        return orderId

#FLOW->
#createOrder() --> getToken()-->Login API-->Get Token-->Create Order API-->Get Order ID-->Return Order ID

#I created APIutils.py to centralize reusable API operations. Instead of duplicating login and order creation logic in multiple tests, I created reusable methods like getToken() and createOrder(). This improves maintainability and allows tests to focus on business validation rather than API setup logic.

#FILEs FLOW
#apiBase.py → provides API methods
#       ↓
#test_e2e_web_api.py → uses API + UI
#        ↓
#test_network_mock.py → mocks response
#        ↓
#test_network_modify.py → modifies request
#        ↓
#test_session_storage.py → optimizes login