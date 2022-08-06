import math
d=float(input("Enter Diameter of the circle and the Side of the Square"))
shapeOfOverlapped="Semi Circle"
radius=float(d/2)
area=round(float(math.pi*(radius**2)),2)
overlap_area=round(float(area/2),2)
print(overlap_area)
radian=math.pi/4
coordinates = [[round(radius*math.cos(i*radian), 2), round(radius*math.sin(i*radian), 2)] for i in range(5)]
print([shapeOfOverlapped,{overlap_area:coordinates}])
