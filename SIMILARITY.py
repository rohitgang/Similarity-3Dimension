import math
def distanceBetween(one, two):
    product= math.sqrt((two[0]-one[0])**2 + (two[1]-one[1])**2 + (two[2]-one[2])**2)
    return product
def closestPair(arr):
    pair= []
    minimumDist= 10000
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j :
                pointOne= arr[i]
                pointTwo= arr[j]
                dist= distanceBetween(pointOne, pointTwo)
                if minimumDist > dist:
                    pair= [pointOne,pointTwo]
                    minimumDist= dist
    return pair

a= [(6,7,3),(1,9,3),(4,9,5),(3,8,7),(10,2,3)]
pair= closestPair(a)
print(pair)