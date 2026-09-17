def analyze_digits_and_case(user_input):
    # Remove leading and trailing spaces
    user_input = user_input.strip()

    uppercase_count = 0
    digit_sum = 0

    for char in user_input:

        # Count uppercase letters
        if char.isupper():
            uppercase_count += 1

        # Add numeric digits
        elif char.isdigit():
            digit_sum += int(char)

    return (uppercase_count, digit_sum)
