print("Prajapati Ritesh Harilal")

import struct

def int_to_binary(n):
    """Convert integer part to binary string"""
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits

def frac_to_binary(frac, limit=10):
    """Convert fractional part to binary string up to given precision"""
    bits = ""
    while frac > 0 and len(bits) < limit:
        frac *= 2
        if frac >= 1:
            bits += "1"
            frac -= 1
        else:
            bits += "0"
    return bits

def float_to_binary32(f):
    """Return 32-bit binary representation of a float"""
    [bits] = struct.unpack('!I', struct.pack('!f', f))
    return f"{bits:032b}", bits

def main():
    num = float(input("Enter the Decimal Number = "))

    bin32, bits = float_to_binary32(num)
    sign = (bits >> 31) & 1
    exponent = (bits >> 23) & 0xFF
    mantissa = bits & 0x7FFFFF

    int_part = int(abs(num))
    frac_part = abs(num) - int_part

    int_binary = int_to_binary(int_part)
    frac_binary = frac_to_binary(frac_part, 10)
    full_binary = f"{int_binary}.{frac_binary}"

    shift = len(int_binary) - 1
    sci_notation = f"1.{int_binary[1:]}{frac_binary} * 2^{shift}"

    real_exp = shift
    biased_exp = real_exp + 127
    biased_exp_binary = f"{biased_exp:08b}"

    mantissa_str = (int_binary[1:] + frac_binary).ljust(23, '0')[:23]

    bin32_str = f"{sign:b}{biased_exp_binary}{mantissa_str}"
    hex_str = f"{bits:08X}"

    print(f"Given number in Binary = {full_binary}")
    print(f"Given number in Scientific Notation = {sci_notation}")
    print(f"Real Exponent = {real_exp}")
    print("Select the destination floating point format = 32 bit")
    print(f"Biased Exponent = {real_exp} + 127 = {biased_exp} = {biased_exp_binary}")
    print(f"Actual fractional part = {int_binary[1:]}{frac_binary}")
    print(f"Mantissa of 23 bits = {mantissa_str}")
    print(f"Sign bit = {sign}")
    print(f"32 bit representation of the given number = {bin32_str}")
    print(f"Hex representation = {hex_str}")

if __name__ == "__main__":
    main()
