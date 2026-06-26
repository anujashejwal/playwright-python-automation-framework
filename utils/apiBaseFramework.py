
#🎯 Goal: Reusable API methods (clean framework design)

#🧠 What this file does:
#getToken() → login API → returns token
#createOrder() → creates order → returns orderId

from playwright.sync_api import Playwright

from conftest import user_credentials

#copy from network tab
ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

class APIutils:

#1. Login via API ==> Sends login request and gets token
    def getToken(self,playwright:Playwright,user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        print(response.json())  #to extract json to retrieve the token
        responseBody = response.json()  #convert response to json
        return responseBody["token"]

#2. Create order via API ==> uses token -> calls orders API-> Creates order in backend
#Only logged-in users can create order that's why we need Token in createOrder()
    def createOrder(self, playwright: Playwright,user_credentials):
        token = self.getToken(playwright,user_credentials) #calls previous method
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com")
        #after giving new context -> open a page
        #copy network tab element where order is created -> copy url and payload for data
        #send create order request =>
        response = api_request_context.post("api/ecom/order/create-order",
                                 data=ordersPayLoad,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})

        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        #why "[0]" 👉 It’s a list → take first element
        return orderId

#apiBase.py → provides API methods
#       ↓
#test_e2e_web_api.py → uses API + UI
#        ↓
#test_network_mock.py → mocks response
#        ↓
#test_network_modify.py → modifies request
#        ↓
#test_session_storage.py → optimizes login