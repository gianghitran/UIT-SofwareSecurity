#include <stdio.h>
int a = 123, b = 456;
int main() {
    int c = 789;
    char s[100];
    printf("%p\n", &c);
    scanf("%s", s);
    printf(s);
    if (c == 16) {
        puts("\nYou modified c.");
    } else if (a == 2) {
        puts("\nYou modified a for a small number.");
    } else if (b == 0x12345678) {
        puts("\nYou modified b for a big number!");
    }
    printf("\na = %d, b = %x, c = %d", a, b, c);
    return 0;
}

// luu s : 0xffffccc8
//print() thu 2: 0xffffccb0
// 0xffffccc8-0xffffccb0=0x18
// 24 bytes / 4 bytes/tham số = 6 --> s o vi tri thu 7 cua prinf