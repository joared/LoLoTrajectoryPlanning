class Pose:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

class AUV:
    def __init__(self, pose):
        self.pose = pose


if __name__ == "__main__":
    print("My name is LoLo")