# include <iostream>
# include <fstream>
# include <string>
# include <Python.h>
using namespace std;

string concatinate(string first, string second) { 
    string endline = "\n";
    return first + endline + second;
}

const char* Cread(const char* filename) {
    ifstream file(filename);
    string line, lines = "";

    if (file.is_open()) {
        while (getline(file, line)) {
            lines = concatinate(lines, line);
        }
    } else {
        lines = "bad open";
    }
    file.close();
    return lines.c_str();
}

int Cwrite(const char* filename, const char* lines) {
    ofstream file;
    file.open(filename);

    if (file.is_open()) {

        file << lines << endl;
        file.close();

        return 1;
    } else {

        file.close();

        return 0;
    }
}




static PyObject* write(PyObject* self, PyObject* args) {
    const char* filename;
    const char* data;

    if (!PyArg_ParseTuple(args, "ss", &filename, &data)) {
        return NULL;
    }

    Cwrite(filename, data);

    Py_RETURN_NONE;
}

static PyObject* read(PyObject* self, PyObject* args) {
    const char* filename;

    if (!PyArg_ParseTuple(args, "s", &filename)) {
        return NULL;
    }

    const char* read_result = Cread(filename);

    return Py_BuildValue("s", read_result);
}

static PyMethodDef methods[] = {
    {"read", read, METH_VARARGS, "Read file (C++)"},
    {"write", write, METH_VARARGS, "Write to file (C++)"},
    {NULL, NULL, 0, NULL} 
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "file_man",
    "Manipulation with files!",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_file_man(void) {
    return PyModule_Create(&module);
}