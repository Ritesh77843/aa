#include <stdio.h>

int main() {
    int A, B;

    printf("Enter input A (0 or 1): ");
    scanf("%d", &A);

    printf("Enter input B (0 or 1): ");
    scanf("%d", &B);

    // NOT Gate
    printf("\nNOT Gate:\n");
    printf("NOT %d = %d\n", A, !A);
    printf("NOT %d = %d\n", B, !B);

    // AND Gate
    printf("\nAND Gate:\n");
    printf("%d AND %d = %d\n", A, B, A && B);

    // OR Gate
    printf("\nOR Gate:\n");
    printf("%d OR %d = %d\n", A, B, A || B);

    // NAND Gate
    printf("\nNAND Gate:\n");
    printf("%d NAND %d = %d\n", A, B, !(A && B));

    // NOR Gate
    printf("\nNOR Gate:\n");
    printf("%d NOR %d = %d\n", A, B, !(A || B));

    // XOR Gate
    printf("\nXOR Gate:\n");
    printf("%d XOR %d = %d\n", A, B, A ^ B);

    // XNOR Gate
    printf("\nXNOR Gate:\n");
    printf("%d XNOR %d = %d\n", A, B, !(A ^ B));

    return 0;
}
