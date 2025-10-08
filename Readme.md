# Currency Converter

## Overview

This Python script converts an amount from one currency to another using the Frankfurter API.  
It fetches live exchange rates and performs the conversion.

## Features

- Fetch latest exchange rates from Frankfurter API
- Convert any amount between supported currencies
- Handles invalid input and network errors gracefully

## Functions

### `get_rate(from_cur, to_cur)`

- Fetches the exchange rate between `from_cur` and `to_cur`.
- Returns a float if successful, otherwise `None`.

### `convert(amount, rate)`

- Converts the given amount using the provided exchange rate.
- Returns the converted amount as a float.

### `main()`

- Handles user input for source and target currencies and amount.
- Calls `get_rate()` to fetch the exchange rate.
- Calls `convert()` to calculate the converted value.
- Displays the result formatted to two decimal places.
- Handles invalid inputs and network errors.

## Usage

1. Run the script:

```bash
python currency_converter.py
```

Follow the prompts:

Enter the source currency code (e.g., USD)

Enter the target currency code (e.g., INR)

Enter the amount to convert

The script will display the conversion rate and the converted amount.

Dependencies

Python 3.x

requests library

Install requests if not already installed:

pip install requests

Example
Welcome to the Currency Converter

From currency (e.g., USD): usd
To currency (e.g., INR): inr
Enter the amount to be converted: 10

1 USD = 85.4300 INR
10 USD = 854.30 INR

Supported Currency Codes

The Frankfurter API supports a wide range of currencies. Some common examples:

USD – United States Dollar

EUR – Euro

INR – Indian Rupee

GBP – British Pound Sterling

JPY – Japanese Yen

AUD – Australian Dollar

CAD – Canadian Dollar

CHF – Swiss Franc

CNY – Chinese Yuan

BRL – Brazilian Real

MXN – Mexican Peso

ZAR – South African Rand

For a complete list of supported currencies, refer to the Frankfurter API documentation
or Supported Currency Codes
.
