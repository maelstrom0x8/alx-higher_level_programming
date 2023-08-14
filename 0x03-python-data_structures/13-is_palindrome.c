#include <stdio.h>
#include <stdlib.h>

#include "lists.h"

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	prev_slow->next = NULL;
	listint_t *prev = NULL;
	listint_t *current = second_half;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	second_half = prev;
	listint_t *temp1 = *head;
	listint_t *temp2 = second_half;
	int is_palindrome = 1;

	while (temp2 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			is_palindrome = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	prev = NULL;
	current = second_half;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	second_half = prev;
	prev_slow->next = second_half;

	return is_palindrome;
}
