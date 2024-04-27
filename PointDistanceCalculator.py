import math
points = [(2,5),(1,6),(-3,-4), (0,0)]  

def euclideanDistance(point1,point2):
    x1,y1 = point1
    x2,y2 =point2
    return  math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
distance = []

for  i in range(len(points)):
     for j in range(i+1,len(points)):
         distance.append(euclideanDistance(points[i], points[j]))
         
minDistance = min(distance)
print(minDistance)