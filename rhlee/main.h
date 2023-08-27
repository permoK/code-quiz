#ifndef MAIN_H
#define MAIN_H

#include  <stdio.h>
#include <stdlib.h>
#include <string.h>


int count_substring(char *str);
int str_cmp(char *fst, char *scd);
void print_pattern(void);
int check_palindrome(char *str, int start,  int end);
char *to_string(int a);

#endif
