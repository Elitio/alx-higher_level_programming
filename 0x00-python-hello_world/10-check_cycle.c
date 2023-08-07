#include "lists.h"

/**
 * check_cycle - Checks if singly linked lists has a cycle.
 * @list: Points to the list
 * Return: 0 for no cycle, 1 for cycle exists.
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *end;

	if (!list || !list->next)
	{
		return (0);
	}
	head = list;
	end = list;
	while (end != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		end = end->next;

		if (head == end)
		{
			return (1);
		}
	}
	return (0);
}
