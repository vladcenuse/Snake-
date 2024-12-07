class Snake:
    def __init__(self):
        self.length = 3
        #self.head = [400,250]
        #self.body = [[375,250],[350,250],[325,250]]
        self.head = [420,270]
        self.body = [[395, 270], [370, 270], [345, 270]]

        self.direction = "down"


    def move(self):
        if self.direction == "up":

            new_coords_head = [self.head[0],self.head[1]-25]
            for i in range(self.length - 1, 0, -1 ):
                self.body[i] = self.body[i - 1]
            self.body[0] = self.head
            self.head = new_coords_head

        if self.direction == "down":

            new_coords_head = [self.head[0],self.head[1]+25]
            for i in range(self.length - 1, 0, -1 ):
                self.body[i] = self.body[i - 1]
            self.body[0] = self.head
            self.head = new_coords_head

        if self.direction == "left":

            new_coords_head = [self.head[0]-25,self.head[1]]
            for i in range(self.length - 1, 0, -1 ):
                self.body[i] = self.body[i - 1]
            self.body[0] = self.head
            self.head = new_coords_head

        if self.direction == "right":

            new_coords_head = [self.head[0]+25,self.head[1]]
            for i in range(self.length - 1, 0, -1 ):
                self.body[i] = self.body[i - 1]
            self.body[0] = self.head
            self.head = new_coords_head

    def eat_apple(self):
        if self.direction == "up":
            new_coords_head = [self.head[0],self.head[1]-25]
            self.body.insert(0,self.head)
            self.length+=1
            self.head = new_coords_head
        if self.direction == "down":
            new_coords_head = [self.head[0],self.head[1]+25]
            self.body.insert(0,self.head)
            self.head = new_coords_head
            self.length += 1
        if self.direction == "left":
            new_coords_head = [self.head[0]-25,self.head[1]]
            self.body.insert(0,self.head)
            self.head = new_coords_head
            self.length += 1
        if self.direction == "right":
            new_coords_head = [self.head[0]+25,self.head[1]]
            self.body.insert(0,self.head)
            self.length += 1
            self.head = new_coords_head

    def check_if_apple(self,apple: list):
        if self.head[0] == apple[0] and self.head[1] == apple[1] :
            self.eat_apple()
            return True
        return False

    def check_if_hit_wall(self):
        #1290x790
        if self.head[0] < 13 or self.head[0] > 1270:
            return False

        if self.head[1] < 13 or self.head[1] > 770:
            return False

        return True

    def check_if_hit_self(self):
        for i in range(self.length - 1) :
            if self.head == self.body[i]:
                return True
        return False