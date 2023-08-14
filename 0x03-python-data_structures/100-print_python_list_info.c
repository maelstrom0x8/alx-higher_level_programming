#include <stdio.h>
#include <Python.h>


/**
 * print_python_list_info - Prints information about a Python list object.
 * @p: Pointer to a PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	long int alloc, len, iter;

	PyObject *obj;

	iter = 0;

	len = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc);

	for (iter; iter < len; iter++)
	{
		obj = PyList_GetItem(p, iter);
		printf("Element %ld: %s\n", iter, Py_TYPE(obj)->tp_name);
	}
}
