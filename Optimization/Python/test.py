#!/usr/bin/env python3
from itertools import *
l = ['20','1121','1121','1a2b3c','223','5595','9929','54355']

c = list(combinations(l, 2))
for i in c:
	if (len(i[0]) != len(i[1])):
		continue

	if (i[0] == i[0][::-1]):
		print('n0')