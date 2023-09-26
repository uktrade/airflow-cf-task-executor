# python-runner

Python command line appliction that accepts Python code via a pointer to external storage and runs it. At the time of writing the only storage accepted is Redis.

> **SECURITY** This application offers a way of running arbitrary Python code - very little is offered in the way of limiting what the code can do. Any sandboxing or other protections must be in place external to this application.
