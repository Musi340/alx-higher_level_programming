#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* is_palindrome - checks if list is palindrome
* @head: list
*
* Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	int i;
	int j;
	int k;
	int myarray[100];

	i = 0;
	j = 0;
	if (*head == NULL)
	return (1);
	while (*head)
	{
		myarray[j] = (*head)->n;
		*head = (*head)->next;
		j++;
	}
	j--;
	k = j / 2;
	while (i < k)
	{
		if (myarray[i] == myarray[j])
		{
			i++;
			j--;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
