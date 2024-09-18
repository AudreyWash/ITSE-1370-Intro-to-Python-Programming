# Global variable
multiplier_amount = 1_000_000


def calculate_gains(amount_inv=0.0):
    """ Calculate the return gains of an investment. """
    base_gain_margin = 0.001  # 0.1% base gain margin
    gain_margin = base_gain_margin


    if amount_inv > 1_000:
        # Calculate additional gain margin based on the investment
        additional_margin = min((amount_inv // multiplier_amount) * 0.01, 1.0)
        gain_margin = base_gain_margin + additional_margin


        # Calculate the total gains
        total_gains = amount_inv * gain_margin


        # Calculate the total amount including gains
        total_amount = amount_inv + total_gains


        return total_gains, total_amount, gain_margin
   
    # If the investment is below the threshold, no gains
    return 0.0, amount_inv, gain_margin

