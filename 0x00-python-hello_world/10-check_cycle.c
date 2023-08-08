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
	listint_t *current = list;
	int is_loop;

	while (current->next != NULL)
	{
		is_loop = is_looped(current);

		if (is_loop == 0)
			return (1);
		current = current->next;
	}
	return (0);
}

/**
 * is_looped - This function checks if there is
 * a loop to the current node
 * @current: List node
 * Return: 0 if true otherwise 1
 */
int is_looped(listint_t *current)
{
	listint_t *h = current;
	listint_t *curr = current->next;

	while (curr != NULL)
	{
		if (curr == h)
		{
			return (0);
		}
		curr = curr->next;
	}
	return (1);
}
