def convert_base(number, from_base, to_base):
    """Convert a number from one base to another, supporting float values"""
    DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Split integer and fractional parts
    parts = number.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ""

    # Convert integer part to decimal
    decimal_integer = int(integer_part, from_base)

    # Convert integer part to target base
    if decimal_integer == 0:
        converted_integer = "0"
    else:
        converted_integer = ""
        temp = decimal_integer
        while temp > 0:
            converted_integer = DIGITS[temp % to_base] + converted_integer
            temp //= to_base

    # Print step for integer part
    print(f"Decimal {integer_part} converted into Base-{to_base} system = {converted_integer}")
    
    # Handle fractional part if exists
    if not fractional_part:
        return converted_integer 

    # Convert fractional part to decimal
    fractional_decimal = 0.0
    power = 1.0 / from_base
    for digit in fractional_part:
        digit_value = DIGITS.index(digit.upper())
        fractional_decimal += digit_value * power
        power /= from_base

    # Convert fractional decimal to target base
    converted_fractional = ""
    precision = 6  # to match your sample (0.020202)
    while fractional_decimal > 0 and len(converted_fractional) < precision:
        fractional_decimal *= to_base
        digit = int(fractional_decimal)
        converted_fractional += DIGITS[digit]
        fractional_decimal -= digit  

    # Print step for fractional part
    print(f"Fractional decimal 0.{fractional_part} converted into Base-{to_base} system = 0.{converted_fractional}")    
    return converted_integer + "." + converted_fractional

def main():
    try:
        number = input("Enter the Input decimal number = ").strip()
        from_base = 10   # since input is decimal
        to_base = int(input("Enter the base of the destination number system = "))
        result = convert_base(number, from_base, to_base)
        print(f"Hence, Base-{to_base} equivalent of input decimal = {result}") 
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__== "__main__":
    main()
