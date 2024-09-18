"""
Part 1:
Per the instructions, the problem prompts the user for the following information:
* Cost per ice cream serving
* Employee labor rate (per hour)
* Shop rental (per month)
* Utilities (per month)
* Advertising (per month)
* Selling price (each)
* ice cream servings sold per month

You program should operate in a loop in which a menu is displayed with the
following options:

------
Expenses:
1. Cost per serving:
2. Labor rate per hour:
3. Shop rental per month:
4. Utilities per month:
5. Advertising budget per month:

Income:
6. Selling price (each):
7. Servings sold per month:

Analysis:
8. Profit/Loss Calculation
9. "What If" analysis with 10% variance

Enter Selection (0 to Exit):
-----

Menu items 1 - 7 should display the current value of the category and allow
the user to change it.

Menu item 8 should display a single value indicating the amount of profit or
loss. It should then, while holding the income fixed, vary the expenses from
- to + 10 percent in 2 percent increments and outputting the values and the
resulting profit or loss in a table. Finally, while holding the expenses
fixed, vary the income parameters from - to + 10 percent in 2 percent increments.

Sample Output:
Enter Selection (0 to Exit): 8
The Ice Cream Shop will have a monthly profit/loss of 90.0 or 4.0 per serving.

Enter Selection (0 to Exit): 9
Varying the Expenses +/-10%:
Percent:  -10 Expenses:  1719.0 Profit/Loss:  281.0
Percent:  -8 Expenses:  1757.2 Profit/Loss:  242.8
Percent:  -6 Expenses:  1795.4 Profit/Loss:  204.6
Percent:  -4 Expenses:  1833.6 Profit/Loss:  166.4
Percent:  -2 Expenses:  1871.8 Profit/Loss:  128.2
Percent:  0 Expenses:  1910.0 Profit/Loss:  90.0
Percent:  2 Expenses:  1948.2 Profit/Loss:  51.8
Percent:  4 Expenses:  1986.4 Profit/Loss:  13.6
Percent:  6 Expenses:  2024.6 Profit/Loss:  -24.6
Percent:  8 Expenses:  2062.8 Profit/Loss:  -62.8
Varying the Income +/-10%:
Percent:  -10 Income:  1800.0 Profit/Loss:  -110.0
Percent:  -8 Income:  1840.0 Profit/Loss:  -70.0
Percent:  -6 Income:  1880.0 Profit/Loss:  -30.0
Percent:  -4 Income:  1920.0 Profit/Loss:  10.0
Percent:  -2 Income:  1960.0 Profit/Loss:  50.0
Percent:  0 Income:  2000.0 Profit/Loss:  90.0
Percent:  2 Income:  2040.0 Profit/Loss:  130.0
Percent:  4 Income:  2080.0 Profit/Loss:  170.0
Percent:  6 Income:  2120.0 Profit/Loss:  210.0
Percent:  8 Income:  2160.0 Profit/Loss:  250.0

Bonus:
Add functionality that will that use the current expenses and sales volume but
vary the sale price until the "break-even" point is found. If the initial calculation
is positive then reduce the price iteratively and if negative, increase the price
iteratively (think loop). Note that your algorithm doesn't have to find the exact
break even point, only the point where it changes from negative to positive or
positive to negative

10. Find Break-Even

Enter Selection (0 to Exit): 10
Break-Even occurs with a selling price of: 5.7


Note that in all these calculations, assume that the shop operates with a single
employee six days a week, eight hours per day.
"""

"""
# Tip: Always make constants ALL CAPS and give them descriptive names. Think about what
constants you will need in your script. I.e. what numbers will you use that are fixed?
"""


"""
Naming variables well is a best practice. While formats vary by developer/language, 
"snake_case" is commonly used in Python. For example, a variable containing the cost
per serving of ice cream could be named serving_cost. Doing this consistently with a
consistent convention is one mark of a professional developer as it reduces the long
term cost of software maintenance by creating "built in" documentation.

What variables will you need? Start out by listing what the script needs (inputs)
and what the script will produce (outputs). Hint: look at the sample menu. List those
 out and you'll be well on your way.
"""


"""
Additional Hints:
You'll need some form of loop that the script will stay in until the user chooses option
0 to exit. In this loop, you'll want to print out the menu and prompt for user input. 
In this way, everytime a selection is made, the work is done then the loop starts over
and refreshes the menu. Once the user wants to exit, just break out of the loop just like
learned in the text reading.

Next you'll need some logic to either update your variables or to calculate the requested
information.

IDE's support something called "breakpoints" which allow you to stop execution and examine the
of variables in the code. If you don't want to learn that yet then remember you can always put
extra "prints" to output intermediate values to test your algorithms.

Don't forget to comment your code. It's the perfect time to start a good habit!

"""

def calculate_monthly_expenses(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month):
    labor_hours_per_month = 8 * 6 * 4
    total_labor_cost = labor_rate * labor_hours_per_month
    total_serving_cost = serving_cost * servings_per_month
    total_expenses = total_serving_cost + total_labor_cost + shop_rental + utilities + advertising
    return round(total_expenses, 2)

def calculate_monthly_income(selling_price, servings_per_month):
    total_income = selling_price * servings_per_month
    return round(total_income, 2)

def calculate_profit_or_loss(total_income, total_expenses):
    profit_or_loss = total_income - total_expenses
    return round(profit_or_loss, 2)

def what_if_analysis(total_expenses, total_income):
    print("\nVarying the Expenses From -10% to +10%:")
    for i in range(-10, 12, 2):
        varied_expenses = total_expenses * (1 + i / 100)
        profit_or_loss = calculate_profit_or_loss(total_income, varied_expenses)
        print(f"Percent: {i}% Expenses: {round(varied_expenses, 2)} Profit/Loss: {profit_or_loss}")
   
    print("\nVarying the Income From -10% to +10%:")
    for i in range(-10, 12, 2):
        varied_income = total_income * (1 + i / 100)
        profit_or_loss = calculate_profit_or_loss(varied_income, total_expenses)
        print(f"Percent: {i}% Income: {round(varied_income, 2)} Profit/Loss: {profit_or_loss}")

def find_break_even_point(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month):
    selling_price = 0.01
    while True:
        total_expenses = calculate_monthly_expenses(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month)
        total_income = calculate_monthly_income(selling_price, servings_per_month)
        profit_or_loss = calculate_profit_or_loss(total_income, total_expenses)
        if profit_or_loss >= 0:
            return round(selling_price, 2)
        selling_price += 0.01

def main():
    serving_cost = 1.00
    labor_rate = 7.50
    shop_rental = 800
    utilities = 150
    advertising = 100
    servings_per_month = 1000
    selling_price = 4.00

    while True:
        print("\nExpenses:")
        print(f"1. Cost per serving: {serving_cost}")
        print(f"2. Labor rate per hour: {labor_rate}")
        print(f"3. Shop rental per month: {shop_rental}")
        print(f"4. Utilities per month: {utilities}")
        print(f"5. Advertising budget per month: {advertising}")
        print(f"\nIncome:")
        print(f"6. Selling price (each): {selling_price}")
        print(f"7. Servings sold per month: {servings_per_month}")
        print(f"\nAnalysis:")
        print("8. Profit/Loss Calculation")
        print("9. What If Analysis with 10% Variance")
        print("10. Find Break-Even")
        print("0. Exit")

        choice = int(input("\nEnter Selection (0 to Exit): "))

        if choice == 0:
            break
        elif choice == 1:
            serving_cost = float(input("Enter new cost per serving: "))
        elif choice == 2:
            labor_rate = float(input("Enter new labor rate per hour: "))
        elif choice == 3:
            shop_rental = float(input("Enter new shop rental per month: "))
        elif choice == 4:
            utilities = float(input("Enter new utilities per month: "))
        elif choice == 5:
            advertising = float(input("Enter new advertising budget per month: "))
        elif choice == 6:
            selling_price = float(input("Enter new selling price (each): "))
        elif choice == 7:
            servings_per_month = int(input("Enter new servings sold per month: "))
        elif choice == 8:
            total_expenses = calculate_monthly_expenses(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month)
            total_income = calculate_monthly_income(selling_price, servings_per_month)
            profit_or_loss = calculate_profit_or_loss(total_income, total_expenses)
            print(f"\nThe Ice Cream Shop will have a monthly profit/loss of {profit_or_loss} or {round(profit_or_loss / servings_per_month, 2)} per serving.")
        elif choice == 9:
            total_expenses = calculate_monthly_expenses(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month)
            total_income = calculate_monthly_income(selling_price, servings_per_month)
            what_if_analysis(total_expenses, total_income)
        elif choice == 10:
            break_even_price = find_break_even_point(serving_cost, labor_rate, shop_rental, utilities, advertising, servings_per_month)
            print(f"\nBreak-Even occurs with a selling price of: {break_even_price}")
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()