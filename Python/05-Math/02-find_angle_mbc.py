from cmath import phase
from math import degrees

AB = int(input())
BC = int(input())

mbc = round(degrees(phase(complex(BC, AB))))

print(str(mbc) + '°')
