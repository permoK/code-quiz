#include "main.h"


int main(void)
{
	int n, len;
	char *string;

	n = 1111111;
	string = to_string(n);
	for (len = 0; string[len]; len++)
		;
	printf("%d\n", check_palindrome(string, 0, len - 1));
	return (0);
}
