import re

def luhn_check(card_number):
    total = 0
    num_digits = len(card_number)
    odd_even = num_digits % 2

    for i in range(num_digits):
        digit = int(card_number[i])

        if (i % 2) == odd_even:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    return (total % 10 == 0)

def validate_credit_card(card_number):
    # Remove non-numeric characters
    card_number = re.sub(r'\D', '', card_number)

    # Check if the card number is valid
    return luhn_check(card_number)

def main():
    # Take input from user
    card_number = input("Enter the credit card number: ")

    # Validate the card number
    if validate_credit_card(card_number):
        print("TRUE The card number is valid.")
    else:
        print("FALSE The card number is invalid.")

if __name__ == "__main__":
    main()
