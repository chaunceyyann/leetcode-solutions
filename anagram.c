#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
bool isAnagram(char* s, char* t) {
    if(strlen(s)!=strlen(t)){
        return false;
    }
    
    int len=strlen(s);
    typedef struct charar {
        char ch;
        int cnt;
    } charar;
    charar arr[len], tmp[len];
    for (int i = 0; i<len; ++i){    // check every char
        printf("%c\n",s[i]);
        for (int j = 0;;++j){  // check duplication
            if (s[i]==arr[j].ch) {
                ++arr[j].cnt;
                break;
            }
            else if (arr[j].ch==NULL){
                arr[j].ch = s[i];
                arr[j].cnt = 1;
                break;
            }
        }
    }
    for (int i = 0;i<len;++i){
        printf("|%c",arr[i].ch);
    }
    printf("|\n");
    for (int i = 0;i<len;++i){
        printf("|%d",arr[i].cnt);
    }
    printf("|\n");
    memcpy(&tmp, &arr, sizeof(charar));
    for (int i = 0; i<len; ++i){    // check every char
        printf("%c\n",t[i]);
        for (int j = 0;;++j){  // check duplication
            if (t[i]==arr[j].ch) {
                ++arr[j].cnt;
                break;
            }
            else if (arr[j].ch==NULL){
                arr[j].ch = t[i];
                arr[j].cnt = 1;
                break;
            }
        }
    }

    bool match;
    for (int i = 0; i<len; ++i){
        match = false;
        for (int j = 0; j<len; ++j){
            if (arr[i].ch == tmp[j].ch){
                match = true;
                if (arr[i].cnt != tmp[j].cnt){
                    printf("1\n");
                    return false;
                }
                else break;
            }
        }
        if (!match){
            printf("2\n");
            return false;
        }
    }
    return true;
}
int main(int argc, char **argv){
    printf("%s\n",argv[1]);
    printf("%s\n",argv[2]);
    if (isAnagram(argv[1],argv[2]))
        printf("Yes\n");
    else printf("No\n");
    return 0;
}
