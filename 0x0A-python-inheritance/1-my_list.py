#!/usr/bin/python3

"""A module providing a custom list class with sorting functionality.
This module defines a custom list class, `MyList`, which inherits from
the built-in `list` class. `MyList` provides methods for performing insertion
sort and printing the sorted list."""


class MyList(list):
    """A custom list class with sorting functionality."""

    def insertion_sort(self):
        """Sort the elements of the list in ascending order
           using the insertion sort algorithm."""
        elem = self.copy()
        for i in range(1, len(elem)):
            key = elem[i]
            j = i - 1
            while j >= 0 and key < elem[j]:
                elem[j + 1] = elem[j]
                j -= 1
                elem[j + 1] = key
        return elem

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """
        sortv = self.insertion_sort()
        print(sortv)
