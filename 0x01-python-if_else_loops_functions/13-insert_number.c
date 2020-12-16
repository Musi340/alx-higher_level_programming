#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *mypointer;
	listint_t *newnode;

	if (head == NULL)
	return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	mypointer = *head;
	while (mypointer)
	{
		if (mypointer->n > number)
		{
		newnode->next = mypointer;
		}
		else if (mypointer->next->n >= number)
		{
			newnode->next = mypointer->next;
			mypointer->next = newnode;
			return (newnode);
		}
		mypointer = mypointer->next;
	}
	return(NULL);
}
