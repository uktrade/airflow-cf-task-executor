import json
import sys

import subprocess

import base64

import pickle
import redis


def hello_world():
    print("hello world")

def runner(packed_function):
    import os
    print("VCAP_SERVICES" in os.environ)
    unpacked_function = pickle.loads(packed_function)
    unpacked_function()

if __name__ == '__main__':
    if sys.argv[1] == "run":
        import os
        credentials = json.loads(os.environ["VCAP_SERVICES"])["redis"][0]["credentials"]

        r = redis.Redis(
            host=credentials["host"], port=credentials["port"],
            username="",
            password=credentials["password"],
            ssl=True,
        )
        r.set('key', pickle.dumps(hello_world))

        key = sys.argv[2]

        packed_function = r.get(key)
        p = subprocess.Popen([sys.executable, __file__, "_run", base64.b64encode(packed_function)], env={"LD_LIBRARY_PATH": os.environ["LD_LIBRARY_PATH"]})
        p.wait(timeout=30)
        print(key)
    
    if sys.argv[1] == "_run":
        runner(base64.b64decode(sys.argv[2]))