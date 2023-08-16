#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

#define LIST_CAST(type, ptr) ((type *)(ptr))

/**
 * print_python_list_info - Prints information about a Python list object.
 * @p: Pointer to a PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	long int list_size = PyList_Size(p);
	int count;

	PyListObject *object = LIST_CAST(PyListObject, p);

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", object->allocated);

	for (count = 0; count < list_size; count++)
		printf("Element %i: %s\n", count, Py_TYPE(object->ob_item[count])->tp_name);
}
