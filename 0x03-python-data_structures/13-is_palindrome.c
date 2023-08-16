#include "lists.h"

/**
 * reverse - Wil reverse the second half of the list
 *
 * @s_head: Head of the second half
 * Return: void
 */

void reverse(listint_t **s_head)
{
	listint_t *prev_n;
	listint_t *current_n;
	listint_t *next_n;

	prev_n = NULL;
	current_n = *s_head;

	while (current != NULL)
	{
		next_n = current_n->next;
		current_n->next = prev_n;
		prev_n = current_n;
		current_n = next_n;
	}

	*s_head = prev_n;
}

int compare(listint_t *1_loop, listint_t *2_loop)
{
	listint_t *trav1;
	listint_t *trav2;

	trav1 = 1_loop;
	trav2 = 2_loop;

	while (trav1 != NULL && trav2 != NULL)
	{
		if (1_loop->n == 2_loop->n)
		{
			1_loop = 1_loop->next;
			2_loop = 2_loop->next;
		}
		else
		{
			return (0);
		}
	}

	if (trav1 == NULL && trav2 == NULL)
	{
		return (1);
	}

	return (0);
}

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
