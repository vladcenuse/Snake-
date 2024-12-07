import time
import tkinter as tk
import ttkbootstrap as ttk
from Elements.Snake import Snake
import random


class Table:
    def __init__(self):
        self.snake = Snake()
        self.speed = 150
        self.showGUI()


    def showGUI(self):
        window = tk.Tk()
        window.title("Snake")
        window.geometry('1290x790')

        board = tk.Canvas(master=window,bg="green",height=790,width=1290)
        board.pack()

        upper_border = board.create_line(0,0,1290,0,width=20,fill="black")
        right_border = board.create_line(1290,0,1290,790, width=14, fill="black")
        lower_border = board.create_line(1290, 790,0,790, width=14, fill="black")
        left_border = board.create_line(0, 790,0, 0, width=20, fill="black")


        apple_coord = self.spawn_initial_apple(self.snake.head) # 25 x 25
        apple = board.create_oval(apple_coord[0] - 12.5, apple_coord[1] - 12.5, apple_coord[0] + 12.5,apple_coord[1] + 12.5, fill="red")

        def change_up(event):
            self.snake.direction = "up"
        def change_down(event):
            self.snake.direction = "down"
        def change_right(event):
            self.snake.direction = "right"
        def change_left(event):
            self.snake.direction = "left"

        window.bind("<KeyPress-w>", change_up)
        window.bind("<KeyPress-a>", change_left)
        window.bind("<KeyPress-s>", change_down)
        window.bind("<KeyPress-d>", change_right)

        head_display = None
        body_parts = []

        def game_loop():
            nonlocal head_display, body_parts, apple, apple_coord
            self.snake.move()

            # delete old head and body parts
            if head_display is not None:
                board.delete(head_display)
            for part in body_parts:
                board.delete(part)

            # reset body_parts list
            body_parts = []

            # create new head
            head_display = board.create_oval(self.snake.head[0] - 12.5, self.snake.head[1] - 12.5, self.snake.head[0] + 12.5,
                                             self.snake.head[1] + 12.5, fill="black")

            # create new body parts
            for i in range(self.snake.length - 1):
                part = board.create_oval(self.snake.body[i][0] - 12.5, self.snake.body[i][1] - 12.5, self.snake.body[i][0] + 12.5,
                                         self.snake.body[i][1] + 12.5, fill="grey")
                body_parts.append(part)

            if self.snake.check_if_apple(apple_coord) == True:
                board.delete(apple)
                apple_coord = self.spawn_initial_apple(self.snake.head)  # 25 x 25
                apple = board.create_oval(apple_coord[0] - 12.5, apple_coord[1] - 12.5, apple_coord[0] + 12.5,
                                          apple_coord[1] + 12.5, fill="red")

            if self.snake.check_if_hit_wall() == False:
                game_end()
                return None

            if self.snake.check_if_hit_self() == True:
                game_end()
                return None
            self.game_speed()
            window.after(self.speed, game_loop)

        game_loop()

        def game_end():
            print("L")

        window.mainloop()

    def spawn_initial_apple(self, head_coords):

        good = False
        while good == False :
            good = True
            x = random.randint(2, 50) * 25 + 20
            y = random.randint(2, 30) * 25 + 20
            if x > head_coords[0] - 50 and x < head_coords[0] + 50:
                good = False
            if y > head_coords[1] - 50 and y < head_coords[1] + 50:
                good = False

        return [x,y]

    def spawn_apple(self,snake: Snake):
        while good == False :
            good = True
            x = random.randint(2, 50) * 25 + 20
            y = random.randint(2, 30) * 25 + 20
            if x == snake.head[0] and y == snake.head[1]:
                good = False
            for i in range(snake.length) :
                if x == snake.body[i][0] and y == snake.body[i][1]:
                    good = False

        return [x,y]

    def game_speed(self):
        if self.snake.length < 6 :
            self.speed = 150
            return
        if self.snake.length < 11 :
            self.speed = 100
            return
        if self.snake.length < 16 :
            self.speed = 75
            return
        if self.snake.length < 21 :
            self.speed = 50
            return
        self.speed = 35





if __name__ == "__main__":
    gui = Table()


