#include "lists.h"


/**
 * insert_node - Adds a node to a sorted linked list
 * @head: Head of the list
 * @number: Node value
 * Return: Address of node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new_node;

	if ((*head) == NULL)
	{
		return (NULL);
	}
	else
	{
		node = (*head);
		new_node = (listint_t *)malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);

		new_node->n = number;

		while (node->next != NULL && node->next->n < number)
		{
			node = node->next;
		}
		new_node->next = node->next;
		node->next = new_node;
		return (new_node);
	}

	return (NULL);
}
