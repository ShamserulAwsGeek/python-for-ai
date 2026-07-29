# The time module provides functions for working with time — getting the current time,
# measuring durations, pausing execution, and formatting timestamps. 
# It's part of Python's standard library, so no installation needed.

# time.time() returns a float representing seconds since the epoch. 
# It's commonly used for timing code or logging.

import time

def usingwhile():
    i = 0
    while i < 50000:
        i += 1
        print(i)


def usingfor():
    for i in range(50000):
        print(i)


init = time.time()

usingwhile()
print(time.time() - init)
usingfor()
print(time.time() - init)

-----------------------------
-----------------------------
import time

t = time.time()
print(t)  # 1753776000.123456 (seconds since Jan 1, 1970 - the "epoch")

-----------------------------
-----------------------------





