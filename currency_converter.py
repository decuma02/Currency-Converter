import requests

def get_rate(from_cur, to_cur):
    """
    Fetches the exchange rate between two currencies using the Frankfurter API.

    Args:
        from_cur (str): The base currency code (e.g., 'USD').
        to_cur (str): The target currency code (e.g., 'INR').

    Returns:
        float or None: The exchange rate if successful, otherwise None.
    """
    url = f"https://api.frankfurter.app/latest?from={from_cur}&to={to_cur}"

    try:
        # Send GET request to the API
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Automatically raise exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

    # Parse JSON response
    data = response.json()

    # Check if 'rates' and target currency exist in response
    rate = data.get("rates", {}).get(to_cur)
    if rate is None:
        print(f"Currency code '{to_cur}' not found.")
        return None

    return rate


def convert(amount, rate):
    """
    Converts the given amount using the provided exchange rate.

    Args:
        amount (float): The amount of money to convert.
        rate (float): The exchange rate.

    Returns:
        float: The converted amount.
    """
    return amount * rate


def main():
    """
    Main function to run the currency converter.
    Prompts the user for input, fetches the rate, performs conversion,
    and displays the result.
    """
    print("Welcome to the Currency Converter\n")

    # Get user inputs
    from_cur = input("From currency (e.g., USD): ").upper().strip()
    to_cur = input("To currency (e.g., INR): ").upper().strip()

    # Validate amount input
    try:
        amount = float(input("Enter the amount to be converted: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    # Fetch exchange rate
    rate = get_rate(from_cur, to_cur)
    if rate is None:
        print("Conversion failed due to invalid input or network issue.")
        return

    # Perform conversion
    converted = convert(amount, rate)

    # Display results
    print(f"\n1 {from_cur} = {rate:.4f} {to_cur}")
    print(f"{amount} {from_cur} = {converted:.2f} {to_cur}")


if __name__ == "__main__":
    main()
