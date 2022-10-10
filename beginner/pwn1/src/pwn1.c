#include <stdio.h>
#include <stdlib.h>

#ifndef FLAG
  #define FLAG "TUDCTF{FAKE}"
#endif 

typedef struct pwnable {
    char buf[16];
    int flag;
} Pwnable;


int main(){
    Pwnable* pwn = (Pwnable*)malloc(20);
    pwn->flag  = 0xDEADC0DE;

    scanf("%20s", pwn->buf);

    if(pwn->flag == 0xCAFEBEEF){
        printf("%s\n\n", FLAG);
    }else{
        printf("You were supposed pwn me >.<\n");
    }
}
