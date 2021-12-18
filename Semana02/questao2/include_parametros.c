// inclui a biblioteca padrao do C
#include <stdio.h>
// inclui as funcoes (add e multiply)
// geradas em um arquivo header
#include "parametros.h"

// main function
int main()
{
    int num1, num2;
	// passa dois parametros para as
    // funcoes add e multiply
    printf("Type the first number: ");
    scanf("%d", &num1);
    printf("Type the second number: ");
    scanf("%d", &num2);

	add(num1, num2);

	multiply(num1, num2);

	// printf defined in stdio.h
	printf("Process completed\n");
	return 0;
}
