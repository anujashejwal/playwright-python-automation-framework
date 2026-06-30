#Goal: Reusable API methods (clean framework design)

#What this file does:
# getToken() -> Login API -> Returns token
# createOrder() -> Creates order -> Returns orderId

from playwright.sync_api import Playwright

# Copy from Network tab
ordersPayLoad = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "6960eae1c941646b7a8b3ed3"
        }
    ]
}


class APIutils:

    # 1. Login via API ==> Sends login request and gets token
    def getToken(self, playwright: Playwright, user_credentials):

        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]

        api_request_context = playwright.request.new_context(
            base_url="https://www.rahulshettyacademy.com/client"
        )

        response = api_request_context.post(
            "api/ecom/auth/login",
            data={
                "userEmail": user_email,
                "userPassword": user_password
            }
        )

        assert response.ok, f"{response.status} - {response.text()}"

        responseBody = response.json()
        print("Login Response:", responseBody)

        return responseBody["token"]

    # 2. Create order via API ==> Uses token -> Calls Order API -> Creates order
    def createOrder(self, playwright: Playwright, user_credentials):

        token = self.getToken(playwright, user_credentials)

        api_request_context = playwright.request.new_context(
            base_url="https://www.rahulshettyacademy.com"
        )

        response = api_request_context.post(
            "api/ecom/order/create-order",
            data=ordersPayLoad,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )

        print("Create Order Response:", response.json())

        response_body = response.json()
        orderId = response_body["orders"][0]

        return orderId

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