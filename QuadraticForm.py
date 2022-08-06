import math,cmath

def quadRoot(a,b,c):
    d=(b*b)-(4*a*c)
    Magnitude = {}
    if d<0:
        z1=(complex(-b, math.sqrt(-d)))/(2*a)
        z2=(complex(-b, math.sqrt(-d)))/(2*a)
        complexNum=(math.sqrt((z1.real**2) + (z1.imag**2)), 2)
        Magnitude['complexNum'] = [round(math.degrees(cmath.phase(z2)), 2),
                      round(cmath.phase(z2), 2),
                      round(math.degrees(cmath.phase(z1)), 2),
                      round((cmath.phase(z1)), 2)]
        return(Magnitude)
    else:
        r1=round((-b + math.sqrt(d))/(2*a),2)
        r2=round((-b + math.sqrt(d))/(2*a),2)
        Magnitude['realNum']=[r1,r2]
        return(Magnitude)
a=input('input the value for ax^2 for the quadratic equation:')
b=input('input the value for bx for the quadratic equation:')
c=input('input the value for c for the quadratic eqaution:')

if a.isnumeric() and b.isnumeric() and c.isnumeric() and a!=0:
    a=int(a)
    b=int(b)
    c=int(c)
    t=quadRoot(a,b,c)
    print(t)
    
    
        
