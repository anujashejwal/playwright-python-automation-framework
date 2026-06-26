from pageObjects.orderDetailsPage import OrderDetailsPage


class OrdersHistoryPage:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderId):
        row = self.page.locator("tr", has_text=orderId)  # extract a row where that specific orderId is present
        row.get_by_role("button", name="View").click()  # On that row click on View button
        orderDetailsPage = OrderDetailsPage(self.page)
        orderDetailsPage.verifyOrderMessage()
        return orderDetailsPage

#API → Create Order → get orderId
#        ↓
#Orders Page → find row using orderId
#        ↓
#Click "View"
#        ↓
#Order Details Page opens
#        ↓
#Verify order details/message