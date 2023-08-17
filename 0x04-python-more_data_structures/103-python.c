#include <stdio.h>
#include <Python.h>

#define OBJ_SIZE(ptr, obj) (((ptr *) obj)->ob_size)
#define OBJ_SVAL(ptr, obj) (((ptr *) obj)->ob_sval)
#define OBJ_IDX(ptr, obj, idx) (((ptr *) obj)->ob_item[idx])


/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int sz, i, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = OBJ_SIZE(PyVarObject, p);
	str = OBJ_SVAL(PyBytesObject, p);


	printf("  size: %ld\n", sz);
	printf("  trying string: %s\n", str);

	if (sz >= 10)
		lim = 10;
	else
		lim = sz + 1;

	printf("  first %ld bytes:", lim);

	for (i = 0; i < lim; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - Prints basic information of a list
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	PyObject *object;
	PyListObject *list;
	long int size, i;

	size = OBJ_SIZE(PyVarObject, p);
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		object = OBJ_IDX(PyListObject, p, i);
		printf("Element %ld: %s\n", i, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}

