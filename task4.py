import os
import sys

a = 0
b = 0
c = 0
d = 0

root_dict = {100: a, 1000: b, 10000: c, 10000: d}

for root,dirs, files in os.walk(sys.argv[0]):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size <= 100:
            a += 1
            root_dict[100] = a

        if 100 < os.stat(os.path.join(root, file)).st_size <= 1000:
            b += 1
            root_dict[1000] = b

        if 1000 < os.stat(os.path.join(root, file)).st_size <= 10000:
            c += 1
            root_dict[10000] = c

        if 10000 < os.stat(os.path.join(root, file)).st_size <= 100000:
            d += 1
            root_dict[100000] = d

print(root_dict)