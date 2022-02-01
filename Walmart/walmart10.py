## 10 : Generate Random Point in a Circle

class Solution:
    
    r, x, y = 0, 0, 0
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r=radius
        self.x=x_center
        self.y=y_center

    def randPoint(self) -> List[float]:
        theta = random.uniform(0,2*pi)
        R = self.r*sqrt(random.uniform(0,1))
        return [self.x + R*cos(theta), self.y + R*sin(theta)]
