**Scenario**

Abby has always dreamed of having her own ice cream shop. Now as a young entrepreneur she has decided to pursue her dream, but she needs some help in determining the financial viability of her plan. She has come up with a list of income and expense parameters and needs a simple program to input these parameters and calculate the monthly profit or loss as well as performing some variable cost what-if analysis.

For expenses, she has:

    - Raw ingredient cost per serving
    - Hourly labor rate
    - Real estate monthly rental
    - Utilities per month
    - Monthly advertising budget

On the income side, she has:

    - Selling price per serving (assume only one size for simplicity)
    - Number of servings sold per month

Based on some research, she has determined that a single employee can run the shop and she plans to have the shop open eight hours per day and six days per week.

Create the text-based, menu interface

Write a Python script with a menu driven, text-based user interface that looks like this:

Expenses:
1. Cost per serving: 1.0
2. Labor rate per hour: 7.5
3. Shop rental per month: 800
4. Utilities per month: 150
5. Advertising budget per month: 100

Income:
6. Selling price (each): 4.0
7. Servings sold per month: 500

Analysis:

```
Enter Selection (0 to Exit):

In which the current parameter value is displayed but the user can select and modify each one. For Example:

Enter Selection (0 to Exit): 1
Enter cost per serving:
```

Use the following as the default starting values:

```
serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 1000
selling_price = 4.00
```