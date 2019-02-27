import math

from vector import Vector2D

class Fish:

    def __init__(self):
        # distances in pixels
        self.sight_dist = 500
        # turning speed in radians/sec
        self.turn_speed = 50 * math.pi / 180
        # swimming speed in pixels/sec
        self.swim_speed = 100

        # size (radius) in pixels
        self.size = 5

        # current pos
        self.pos = Vector2D()
        # current velocity
        self.vel = Vector2D()

        # list of fish within sight
        self.nearby_fish = list()

    # in radians
    def getAngle(self):
        return self.vel.angle()

    def swim(self, time_passed):
        self.pos += self.vel * time_passed

    """Returns the average angle of velocity of nearby fish """
    def findAngle_AvgDir(self):
        averageAngle = 0
        for fish in self.nearby_fish:
            averageAngle += fish.getAngle()
        averageAngle /= len(self.nearby_fish)
        return self.fixAngle(averageAngle)


    """Returns the angle to the COM from the current pos"""
    def findAngle_COM(self):
        angle = self.getAngle()

        # find COM of nearby_fish
        com = Vector2D()
        for fish in self.nearby_fish:
            com += fish.pos
        com /= len(self.nearby_fish)
       
        vector_to_com = com - self.pos
        # dont need to change angle if already there
        if not vector_to_com.magnitude() == 0:
            #print(self.vel.angleBetween(vector_to_com))
            angle += self.vel.angleBetween(vector_to_com)
            #print(com)

        #print(self.fixAngle(angle))
        return self.fixAngle(angle)

    """Returns what angle the fish should be at given its desired angle"""
    def getNewAngle(self, desired_angle, delta_t):
        angle = self.getAngle()

        # if the angle can be reached then just set it to that
        if abs(desired_angle - angle) <= self.turn_speed * delta_t:
            angle = desired_angle
        else:
            # 1 is counterclockwise, -1 is clockwise
            direction = 1
            
            # if desired_angle behind current angle then swap
            if desired_angle - angle < 0:
                direction *= -1

            # direction needs to be flipped if absolute difference is greater then pi
            # b/c it would be quicker to go around the other way
            if abs(desired_angle - angle) > math.pi:
                direction *= -1

            angle += self.turn_speed * delta_t * direction


        return self.fixAngle(angle)

    
    def school(self, delta_t):
        pass


    def updateVel(self, angle):
        self.vel.x = self.swim_speed * math.cos(angle)
        self.vel.y = self.swim_speed * math.sin(angle)

    def fixAngle(self, angle):
        # keep angles within 0 to 2*pi
        if angle < 0:
            angle += 2 * math.pi
        elif angle >= 2 * math.pi:
            angle -= 2 * math.pi
        return angle

    """Returns a list of nearby fish"""
    def findNearbyFish(self, fish_list):
        self.nearby_fish = list()
        for fish in fish_list:
            if fish.pos.cartesianDistance(self.pos) <= self.sight_dist:
                self.nearby_fish.append(fish)

    """Returns a list of tuples, first entry distance to fish, second entry is other fish object"""
    def findNearbyFishInfo(self, fish_list):
        self.nearby_fish = list()
        for fish in fish_list:
            if fish.pos.cartesianDistance(self.pos) <= self.sight_dist:
                self.nearby_fish.append((self.pos.cartesianDistance(fish.pos), fish))

        
