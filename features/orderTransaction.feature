Feature: Order Transaction
  Tests related to Order Transactions

  Scenario Outline: Verify Order success message show in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    And select the order
    Then order message is successfully displayed
    Examples:
    | username                     | password    |
    | rahulshettyacademy@gmail.com | Iamking@000 |
