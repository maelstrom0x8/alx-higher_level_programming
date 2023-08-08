#include "lists.h"
#include <stdio.h>
#include <unistd.h>

/**
 * check_cycle - A function in C that checks if a singly linked list
 * has a cycle in it.
 * @list: Head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *behind = list;
	listint_t *ahead = list;

	if (list == NULL)
		return (0);

	while (ahead != NULL && ahead->next != NULL)
	{
		ahead = ahead->next->next;
		behind = behind->next;

		if (behind == ahead)
			return (1);
	}

	return (0);
}
