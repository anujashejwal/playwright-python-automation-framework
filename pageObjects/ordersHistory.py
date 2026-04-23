from pageObjects.orderDetailsPage import OrderDetailsPage


class OrdersHistoryPage:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderId):
        row = self.page.locator("tr", has_text=orderId)  # extract a row where orderId is present
        row.get_by_role("button", name="View").click()  # On that row click on View button
        orderDetailsPage = OrderDetailsPage(self.page)
        orderDetailsPage.verifyOrderMessage()
        return orderDetailsPage
