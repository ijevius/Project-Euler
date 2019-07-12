import decimal
import numpy

f = numpy.math.factorial(1000000000000)
s = str(decimal.Decimal(f) / 1)
pos = s.find("E")
print(s[pos-5:pos])
