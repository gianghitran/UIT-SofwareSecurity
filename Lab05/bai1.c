#include <stdio.h>
int main() {
    short int a = 0x7fff;
    unsigned short int b = 0xffff;
    printf("0x%x + 1 = %hd + 1 = %hd\n", a, a, a + 1);
    printf("0x%x + 1 = %hu + 1 = %hu\n", b, b, b + 1);
    return 0;
}