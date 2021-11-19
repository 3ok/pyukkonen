import timeit
from ukkonen import distance
from pyukkonen import ukkonen


with open("apache2.txt", "r") as f:
    apache2 = f.read()

with open("gpl.txt", "r") as f:
    gpl = f.read()


t_anthonk = timeit.timeit(lambda: distance(gpl, apache2, 1757), number=10**6)
t_bel = timeit.timeit(lambda: ukkonen(gpl, apache2, 1757), number=10**6)

print(f"Took {t_anthonk} for the first implementation")
print(f"Took {t_bel} for the second implementation")
