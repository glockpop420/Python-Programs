import cmath
import math
x=5
y=2
#z=5+2i
z=complex(x,y)
print(z)
p=8
q=3
r=complex(p,q)
print(r)
w=z*r
print(w)
print(z.real)
print(z.imag)
#angleR=math.atan(z.imag/z.real)
angleR=cmath.phase(z)
print(angleR)
angleD=math.degrees(angleR)
print(round(angleD))
Magnitude=math.sqrt(z.real**2+z.imag**2)
print(Magnitude)
print({Magnitude:[angleR,angleD]})
