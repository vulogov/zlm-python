#include <Python.h>
#include "log.h"

/* extern void zabbix_log(int level, const char *fmt, ...); */

static PyObject* zabbix_module_log(PyObject *self, PyObject *args);

static PyMethodDef ZabbixMethods[] = {
 {"log",  zabbix_module_log, METH_VARARGS, "Send a string to a Zabbix logfile with WARNING severity."},
 {NULL, NULL, 0, NULL}
};

static PyObject* zabbix_module_log(PyObject *self, PyObject *args) {
   int   level;
   const char *log;
   if (!PyArg_ParseTuple(args, "is", &level, &log))   {
      PyErr_SetString(PyExc_RuntimeError, "Two parameters expected: log level and a message");
      return NULL;
   }
   zabbix_log(level, log);
   Py_RETURN_NONE;
};


PyMODINIT_FUNC  initzabbix(void) {   
       (void) Py_InitModule("Zabbix", ZabbixMethods);
}

