#include <stdio.h>

int main(){
	long long int i;
    do{
    	scanf("%lld",&i);
    	if(i%2==0)	printf("%lld\n",i);
    }
    while(i != -1);
    return 0;
}

