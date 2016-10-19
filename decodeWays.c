#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
int numDecodings(char* s) {
    static volatile int i;
    static int cnt = 0;
    int e = 0; // for function return roll back i
    for (; s[i]!=0; ++i) {
        if ((s[i]!='0')&&(s[i+1]!=0)){
            int num_t=10*(s[i]-'0')+(s[i+1]-'0');
            printf("num_t:%d\n",num_t);
            if ((num_t>9)&&(num_t <= 26)){
                printf("in i: %d\n",i);
                ++i;
                numDecodings(s);
            }
        }
        printf("out i: %d\n",i);
        ++e;
        printf("out e: %d\n",e);
    }
    i=i-e;
    printf("cnt:%d\n",++cnt);
    printf("ret i: %d\n",i);
    return cnt;
}
int main(int argc, char **argv) { 
    numDecodings(argv[1]);
    return 0;
}
