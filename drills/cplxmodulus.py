import math
c1 = math.pow(abs((5+2j)/math.sqrt(30)), 2)
print(c1)  # correct
c2 = math.pow(abs((-2-(math.sqrt(5)*1j))/math.sqrt(30)), 2)
print(c2)
c3 = math.pow(abs((math.sqrt(2/5)*1j)), 2)
print(c3)
c4 = c1 + c2 + c3
print(c4)
