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
	listint_t *mypointer;
	int myarray[1000];

	i = j = 0;
	if (head == NULL || *head == NULL)
	return (1);
	if ((*head)->next == NULL)
	return (1);
	mypointer = *head;
	while (mypointer)
	{
		myarray[j] = mypointer->n;
		mypointer = mypointer->next;
		j++;
	}
	j--;
	while (j >= 0 && i <= j)
	{
		if (myarray[i] == myarray[j])
		{
			i++;
			j--;
		}
		else
		return (0);
	}
	return (1);
}

