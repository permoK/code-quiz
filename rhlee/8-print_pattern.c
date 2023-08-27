#include "main.h"
#include <stdio.h>

void print_pattern(void)
{
	int i, j;

	for (i = 1; i <= 5; i++)
	{
		for (j = 1; j <= i; j++)
		{
			printf("%d", i);
		}
		printf("\n");
	}
}
