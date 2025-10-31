#include <stdio.h>

int main() {
    int A, B;

    printf("Enter input A (0 or 1): ");
    scanf("%d", &A);

    printf("Enter input B (0 or 1): ");
    scanf("%d", &B);

    // Half Adder
    int sum = A ^ B;         // XOR for sum
    int carry = A & B;       // AND for carry

    printf("\n--- Half Adder ---\n");
    printf("A = %d, B = %d\n", A, B);
    printf("Sum = %d\n", sum);
    printf("Carry = %d\n", carry);

    // Half Subtractor
    int difference = A ^ B;  // XOR for difference
    int borrow = (!A) & B;   // NOT A AND B for borrow

    printf("\n--- Half Subtractor ---\n");
    printf("A = %d, B = %d\n", A, B);
    printf("Difference = %d\n", difference);
    printf("Borrow = %d\n", borrow);

    return 0;
}
