# Playground

Coding experiments

## Python MATLAB Socket Communication

Socket communication between a Python server and MATLAB client.

A simple Python server using **Flask** to provide some basic functions to handle some basic requests.

A Python and a MATLAB client with same HTTP requests, including sending `Python dictionary / MATLAB struct` and `Numpy array / MATLAB matrix` in request body to test server function.

### Run python server

```bash
export FLASK_APP=python_server.py
flask run
```
