class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        import math
        max_area = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: 
                    continue
                for k in range(len(points)):
                    if k == i or k == j: 
                        continue
                    a = math.sqrt((points[j][0] - points[i][0] )**2 + (points[j][1] - points[i][1] )**2)
                    b = math.sqrt((points[k][0] - points[j][0] )**2 + (points[k][1] - points[j][1] )**2)
                    c = math.sqrt((points[i][0] - points[k][0] )**2 + (points[i][1] - points[k][1] )**2)
                    p = (a+b+c) / 2
                    if a + b > c and a + c > b and b + c > a:
                        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
                        if area > max_area:
                            max_area = area
        return max_area


