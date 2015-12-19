#include <stdio.h>

int main(){
	long long int num;
	do{
		scanf("%lld",&num);
		if(num%2 == 0)	printf("%lld\n",num);
	}while(num != -1);
    return 0;
}

