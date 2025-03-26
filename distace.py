import math

def cal_dist(x1,y1,x2,y2):
    """

    cal dist btw two points (x1,y2) and (x2,y2).

    :param x1: x-coordinate of first point (float or int).
    :param y1: y-coordinate of first point (float or int).
    :param x2: x-coordinate of second point (float or int).
    :param y2: Y-coordinate of second point (float or int).
    """
    
    dist=math.sqrt((x2-x1)**2+ (y2-y1)**2)
    return dist






a1=float(input("enter x-coordinate of first point"))
b1=float(input("enter y-coordinate of first point"))
a2=float(input("enter x-coordinate of second point"))
b2=float(input("enter Y-coordinate of second point"))



d = cal_dist(a1,b1,a2,b2)



print(f"the dist is: {d:.2f}")
