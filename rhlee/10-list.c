#include <Python.h>
#include <stdio.h>


void  print_python_list_info(PyObject *p)
{
	PyObject *ls;
	int len;

	ls = PyList_GetItem(p, 1);
	len = PyList_Size(p);

	printf("%s\n%d\n", Py_TYPE(ls)->tp_name, len);
}
