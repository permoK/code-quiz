#include <stdio.h>

/**
 *main - entry point
 *@ac: argument count
 *@av: argument vector
 *Return 0
 */

int main(int ac, char **av)
{
	char *word, *a;
	int i, result = 0, hold, j;

	if (ac != 3)
	{
		printf("no word input.compile with\ngcc 4-rhlee_remove_n_chars.c\
\nthen run with\n./a.out <word> <number>\n");
		return (1);
	}

	word = av[1];
	a = av[2];

	for (j = 0; word[j]; j++)
		;

	for (i = 0; a[i]; i++)
	{
		if (a[i] >= 48 && a[i] <= 57)
		{
			hold = a[i] - '0';
			result = result * 10 + hold;
		}

		else
		{
			printf("Non integer input, exiting .......\n");
			return (1);
		}
	}

	if (result >= j)
	{
		printf("%d\n", result);
		printf("index out of range, exiting\n");
		return  (1);
	}


	for (i = 0; i < result; i++)
	{
		word++;
	}

	printf("%s\n", word);
	return (0);
}
