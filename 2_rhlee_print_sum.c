#include <stdio.h>

/**
 *main - entry point
 *Return: 0
 */

int main(void)
{
	int i;
	int sum = 0;

	for (i = 0; i <= 10; i++)
	{
		if (i != 0)
		{
			sum = i + i - 1;
		}
		printf("%d\n", sum);
	}

	return (0);
}
