import sys

import time
import random

f = sys.argv[1]

for l in open(f, "r"):
    print l.strip()
    time.sleep(random.randint(0, 2))

