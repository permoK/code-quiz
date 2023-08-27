#include "main.h"

int check_palindrome(char *str, int start,  int end)
{

	if (start >= end)
	{
		return (1);
	}
	else if (str[start] != str[end])
	{
		return (0);
	}

	return (check_palindrome(str, start + 1, end - 1));

}


char *to_string(int a)
{
	int tmp, length, i;
	char *str;

	length = 1;

	tmp = a;
	if (a < 0)
	{
		length++, a = (unsigned int)(-a);
	}

	else
	{
		a = (unsigned int)a;
	}

	while (tmp /= 10)
	{
		length++;
	}

	str = malloc(length * sizeof(char));
	if (!str)
	{
		return (NULL);
	}
	str[length] = '\0';
	if (a < 0)
	{
		str[0] = '-';
	}

	for (i = length - 1; i  >= 0; i--)
	{
		str[i] = (a % 10) + '0', a /= 10;
	}
	return (str);
}
