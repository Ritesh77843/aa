import struct

def mask(n): return (1 << n) - 1

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

def booths_multiply(m, q, bits):
    A = 0
    Q = q & mask(bits)
    Qn1 = 0
    Mmag = m & mask(bits)
    M = to_signed(Mmag, bits)

    for _ in range(bits):
        Q0 = Q & 1

        if Q0 == 1 and Qn1 == 0:
            A = to_signed((A - M) & mask(bits), bits)
        elif Q0 == 0 and Qn1 == 1:
            A = to_signed((A + M) & mask(bits), bits)

        Au = A & mask(bits)
        Qu = Q & mask(bits)
        newQn1 = Q & 1
        shiftedQ = (Qu >> 1) | ((Au & 1) << (bits - 1))
        signA = (Au >> (bits - 1)) & 1
        shiftedA = (Au >> 1) | (signA << (bits - 1))
        A = to_signed(shiftedA, bits)
        Q = shiftedQ
        Qn1 = newQn1

    result_unsigned = ((A & mask(bits)) << bits) | (Q & mask(bits))
    return to_signed(result_unsigned, 2 * bits)

def parse_input(s):
    s = s.strip()
    # try integer first (handles "-9", "3")
    try:
        return int(s), True
    except ValueError:
        # fallback to float
        f = float(s)
        if f.is_integer():
            return int(f), True
        return f, False

def main():
    sm = input("Enter the Multiplier (M) = ")
    sq = input("Enter the Multiplicand (Q) = ")

    m_val, m_is_int = parse_input(sm)
    q_val, q_is_int = parse_input(sq)

    if m_is_int and q_is_int:
        m = int(m_val)
        q = int(q_val)
        n = max(mag_bits(m), mag_bits(q)) + 1   # bits for signed representation
        res = booths_multiply(m, q, n)
        print("Binary representation of Multiplicand (Q) = " + to_binary_int(q, n))
        print("Binary representation of Multiplier (M) = " + to_binary_int(m, n))
        print("Result of multiplication in binary = " + to_binary_int(res, 2 * n))
    else:
        m_f = float(m_val)
        q_f = float(q_val)
        res_f = m_f * q_f
        print("Binary representation of Multiplicand (Q) = " + float_to_binary32(q_f))
        print("Binary representation of Multiplier (M) = " + float_to_binary32(m_f))
        print("Result of multiplication in binary = " + float_to_binary32(res_f))

if __name__ == "__main__":
    main()
