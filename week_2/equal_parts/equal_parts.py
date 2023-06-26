import itertools
from itertools import batched
for batch in batched("ABCDEFGHIJ", 4):
    print(batch)
