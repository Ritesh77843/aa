print("Prajapati Ritesh Harilal")

import struct

def mask(n):
    return (1 << n) - 1

def to_signed(x, n):
    sign = 1 << (n - 1)
    return x - (1 << n) if (x & sign) != 0 else x

def to_binary_int(num, bits):
    if num < 0:
        num = (1 << bits) + num
    s = bin(num & ((1 << bits) - 1))[2:]
    return s.zfill(bits)

def float_to_binary32(f):
    b = struct.pack('!f', float(f))
    i = struct.unpack('!I', b)[0]
    return f"{i:032b}"

def mag_bits(x):
    x = abs(x)
    return 1 if x == 0 else x.bit_length()

def arithmetic_division(dividend, divisor, n):
    q = int(dividend / divisor)
    r = dividend - q * divisor
    return q, r

def parse_input(s):
    s = s.strip()
    try:
        return int(s), True
    except ValueError:
        f = float(s)
        if f.is_integer():
            return int(f), True
        return f, False

def main():
    sd = input("Enter the Dividend (Q) = ")
    sm = input("Enter the Divisor (M) = ")
    d_val, d_is_int = parse_input(sd)
    m_val, m_is_int = parse_input(sm)

    if d_is_int and m_is_int:
        dividend = int(d_val)
        divisor = int(m_val)
        if divisor == 0:
            print("Error: Division by zero")
            return
        n = max(mag_bits(dividend), mag_bits(divisor))
        n = max(1, n)
        quotient, remainder = arithmetic_division(dividend, divisor, n)
        print("Binary representation of Dividend (Q) = " + to_binary_int(dividend, n))
        print("Binary representation of Divisor (M) = " + to_binary_int(divisor, n))
        print("Quotient (binary) = " + to_binary_int(quotient, n))
        print("Remainder (binary) = " + to_binary_int(remainder, n))
    else:
        d_f = float(d_val)
        m_f = float(m_val)
        if m_f == 0.0:
            print("Error: Division by zero")
            return
        res_f = d_f / m_f
        rem_f = d_f % m_f
        print("Binary representation of Dividend (Q) = " + float_to_binary32(d_f))
        print("Binary representation of Divisor (M) = " + float_to_binary32(m_f))
        print("Quotient (binary) = " + float_to_binary32(res_f))
        print("Remainder (binary) = " + float_to_binary32(rem_f))

if __name__ == "__main__":
    main()
