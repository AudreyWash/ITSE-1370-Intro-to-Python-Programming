def format_currency(amount):
    """
    Formats a number as currency with 2 decimal places.
    :param amount: The amount to be formatted
    :return: Formatted string
    """
    return f"${amount:,.2f}"


# Example usage
print(format_currency(1200.2300001))  # Expected output: "$1,200.23"