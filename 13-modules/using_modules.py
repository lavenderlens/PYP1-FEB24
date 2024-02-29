import platform

print(platform.architecture())
print(platform.platform())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.python_implementation())
print(platform.python_version())

import os
print("no. CPUs:", os.cpu_count())
print("encoding:", os.device_encoding(0))
print("encoding:", os.get_terminal_size())

import sys
for path in sys.path:
    print(path)
