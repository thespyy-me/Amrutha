import math

def cal_dist(x1,y1,x2,y2):
    """
    cal dist btw two points (x1,y1) nd (x2,y2).

    :param x1: x-coordinate of first point (float or int).
    :param y1: y-coordinate of first point (float or int).
    :param x2: x-coordinate of secound point (float or int).
    :param y2: y-coordinate of secound point (float or int).
    :return: the dist btw the two points (float).
    """

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

#input values

x1 = float(input("enter x-coordinate of first point"))
y1 = float(input("enter y-coordinate of first point"))
x2 = float(input("enter x-coordinate of secound point"))
y2 = float(input("enter y-coordinate of secound point"))


#cal dist

dist = cal_dist(x1,y1,x2,y2)

#output result

print(f"the dist is: {dist:.2f}")
print ("the diatnace is ",dist)
