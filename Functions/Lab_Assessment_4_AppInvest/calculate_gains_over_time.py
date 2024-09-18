from calculate_gains import calculate_gains


def calculate_gains_over_time(amount_inv=0.0, period=12):
    """
    Calculate the total amount earned over a period of time with monthly compounding.
    :param amount_inv: The initial money amount invested.
    :param period: The number of months for the investment.
    :return: Final amount after the period.
    """
    total_amount = amount_inv
   
    for _ in range(period):
        # Calculate the gains for the current amount
        total_gains, total_amount, gain_margin = calculate_gains(total_amount)
       
        # Update the total amount with the new gains
        total_amount += total_gains
   
    return total_amount
