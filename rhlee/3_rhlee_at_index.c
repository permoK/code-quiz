#include <stdio.h>

/**
 *main - entry point
 *@ac: argument count
 *@av: argument vector
 *Return: 0
 */

int main(int ac __attribute__ ((unused)), char **av)
{
	int i = 0;
	char *word;

	if (!av[1])
	{
		printf("usage:compile with :gcc 3_rhlee_at_index.c\n.then run with\
		       ./a.out <word>\n");
		return (1);
	}

	word = av[1];
	printf("innitial string is %s\n", word);
	printf("printing only even index char\n");


	for (i = 0; word[i]; i++)
	{
		if (i % 2 == 0)
		{
			printf("%c\n", word[i]);
		}
	}

	return (0);
}
