import java.util.Scanner;

public class IEEE754 {
    
    static String intToBinary(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            sb.append(n % 2);
            n /= 2;
        }
        return sb.reverse().toString();
    }

    static String fracToBinary(float frac, int limit) {
        StringBuilder sb = new StringBuilder();
        while (frac > 0 && sb.length() < limit) {
            frac *= 2;
            if (frac >= 1) {
                sb.append("1");
                frac -= 1;
            } else {
                sb.append("0");
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Decimal Number = ");
        float num = sc.nextFloat();
        sc.close();

        int bits = Float.floatToIntBits(num);
        int sign = (bits >>> 31) & 1;
        int exponent = (bits >>> 23) & 0xFF;
        int mantissa = bits & 0x7FFFFF;

        int intPart = (int) num;
        float fracPart = num - intPart;

        String intBinary = intToBinary(intPart);
        String fracBinary = fracToBinary(fracPart, 10); 
        String fullBinary = intBinary + "." + fracBinary;

        
        int shift = intBinary.length() - 1;
        String sciNotation = "1." + intBinary.substring(1) + fracBinary + " * 2^" + shift;

        int realExp = shift;
        int biasedExp = realExp + 127;
        String biasedExpBinary = String.format("%8s", Integer.toBinaryString(biasedExp)).replace(' ', '0');

        String mantissaStr = (intBinary.substring(1) + fracBinary);
        mantissaStr = String.format("%-23s", mantissaStr).replace(' ', '0');

        String bin32 = String.format("%1s %8s %23s", sign, biasedExpBinary, mantissaStr).replace(" ", "");

        String hex = String.format("%08X", bits);

        System.out.println("Given number in Binary = " + fullBinary);
        System.out.println("Given number in Scientific Notation = " + sciNotation);
        System.out.println("Real Exponent = " + realExp);
        System.out.println("Select the destination floating point format = 32 bit");
        System.out.println("Biased Exponent = " + realExp + " + 127 = " + biasedExp + " = " + biasedExpBinary);
        System.out.println("Actual fractional part = " + intBinary.substring(1) + fracBinary);
        System.out.println("Mantissa of 23 bits = " + mantissaStr);
        System.out.println("Sign bit = " + sign);
        System.out.println("32 bit representation of the given number = " + bin32);
        System.out.println("Hex representation = " + hex);

        sc.close();
    }
}
