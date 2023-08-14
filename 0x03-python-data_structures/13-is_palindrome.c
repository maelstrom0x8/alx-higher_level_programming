#include <stdio.h>
#include <stdlib.h>

#include "lists.h"


/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed linked list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next_node;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	return (prev);
}


/**
 * compare_lists - Compares two linked lists.
 * @list1: Pointer to the first linked list.
 * @list2: Pointer to the second linked list.
 * Return: 1 if the lists are equal, 0 if not.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}
	return (1);
}


/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Address of pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	if ((*head) == NULL || (*head)->next == NULL)
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

	prev_slow->next = NULL;
	second_half = reverse_list(slow);
	int is_palindrome = compare_lists((*head), second_half);

	prev_slow->next = reverse_list(second_half);

	return (is_palindrome);
}
