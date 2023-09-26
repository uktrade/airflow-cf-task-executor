# dynamic-runner

Python command line appliction that accepts Python code via a pointer to external storage and runs it. At the time of writing the only storage accepted is Redis.

> **SECURITY** This application offers a way of running arbitrary Python code - very little is offered in the way of limiting what the code can do. Any sandboxing or other protections must be in place external to this application.


## Usage

To generate the code

```python
from dynamic_runner import serialize

serialized = serialize(my_func, *args, **kwargs)
# Then store serialized in Redis
```

Then to run it

```shell
python -m dynamic_runner run my-redis-instance my-redis-key
```
