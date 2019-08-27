from importlib import reload
from helper import run
import ecc
import helper

from ecc import FieldElement, Point

prime = 223

print(prime)

a = FieldElement(num=0, prime=223)git
b = FieldElement(num=7, prime=223)
x = FieldElement(num=192, prime=223)
y = FieldElement(num=105, prime=223)
p1 = Point(x, y, a, b)
print(p1)
