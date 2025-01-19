// SPDX-License-Identifier: Apache-2.0
// Author: Peter Bohus

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <windows.h>

HHOOK hKeyboardHook;
PyObject* callback = NULL;

LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0 && wParam == WM_KEYDOWN) {
        KBDLLHOOKSTRUCT* kbdStruct = (KBDLLHOOKSTRUCT*)lParam;

        if (callback != NULL) {
            PyGILState_STATE gstate = PyGILState_Ensure();
            PyObject* arg = PyLong_FromLong(kbdStruct->vkCode);
            PyObject* result = PyObject_CallOneArg(callback, arg);
            Py_XDECREF(result);
            Py_DECREF(arg);
            PyGILState_Release(gstate);
        }
    }
    return CallNextHookEx(hKeyboardHook, nCode, wParam, lParam);
}

static PyObject* install_hook(PyObject* self, PyObject* args) {
    PyObject* cb;
    if (!PyArg_ParseTuple(args, "O", &cb)) {
        return NULL;
    }
    if (!PyCallable_Check(cb)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be callable");
        return NULL;
    }

    Py_XINCREF(cb);
    Py_XDECREF(callback);
    callback = cb;

    hKeyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, NULL, 0);
    if (!hKeyboardHook) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to install hook");
        return NULL;
    }

    Py_RETURN_NONE;
}


static uint8_t should_exit = 0;

static PyObject* run_message_loop(PyObject* self, PyObject* args) {
    MSG msg;
    should_exit = 0;
    while (!should_exit && GetMessage(&msg, NULL, 0, 0)) {
        if (callback == NULL) break;
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    PyErr_Clear();
    Py_RETURN_NONE;
}

static PyObject* uninstall_hook(PyObject* self, PyObject* args) {
    if (hKeyboardHook) {
        if (!UnhookWindowsHookEx(hKeyboardHook)) {
            PyErr_SetString(PyExc_RuntimeError, "Failed to uninstall hook");
            return NULL;
        }
        hKeyboardHook = NULL;
    }

    Py_XDECREF(callback);
    callback = NULL;

    should_exit = 1;
    PostQuitMessage(0);

    Py_RETURN_NONE;
}

static PyMethodDef DokkeyMethods[] = {
    {"install_hook", install_hook, METH_VARARGS, 
     "Install a keyboard hook.\n\n"
     "Arguments:\n"
     "  callback (callable): A Python function to call on key press."},
    {"uninstall_hook", uninstall_hook, METH_NOARGS, 
     "Uninstall the keyboard hook.\n\n"
     "Stops the global keyboard hook."},
    {"run_message_loop", run_message_loop, METH_NOARGS, 
     "Run the Windows message loop.\n\n"
     "Processes events until `uninstall_hook` is called."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef dokkeymodule = {
    PyModuleDef_HEAD_INIT,
    "dokkey",
    "Keyboard hook module",
    -1,
    DokkeyMethods
};

PyMODINIT_FUNC PyInit_dokkey(void) {
    return PyModule_Create(&dokkeymodule);
}
