#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Data types */
typedef int64_t saint_t;
typedef int64_t saidx_t;
typedef uint8_t sauchar_t;

#include <divsufsort.h>

int main() {
    printf("Hello world!\n");

    // intput data
    char *Text = "abracadabra";
    int64_t n = strlen(Text);

    printf("n = %lul\n", n);

    int64_t i, j;

    // allocate
    int64_t *SA = (int64_t *)malloc(n * sizeof(int64_t));

    // sort
    divsufsort((unsigned char *)Text, SA, n);

    // output
    for(i = 0; i < n; ++i) {
        printf("SA[%2d] = %2d: ", i, SA[i]);
        for(j = SA[i]; j < n; ++j) {
            printf("%c", Text[j]);
        }
        printf("$\n");
    }

    // deallocate
    free(SA);

    return 0;
   
}
