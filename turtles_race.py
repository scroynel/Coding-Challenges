import turtle
import random
import time

class TurtleApp:
    WIDTH, HEIGHT = 1000, 1000
    COLORS = ['red', 'green', 'yellow', 'gray', 'pink', 'blue', 'black', 'orange', 'brown', 'purple']

    def __init__(self):
        self.racers = self.get_numbers_of_racers()
        self.createScreen()
        random.shuffle(self.COLORS)
        self.colors = self.COLORS[:self.racers]
        self.winner = self.race(self.colors)
        print(f"The winner is the turtle with color: {self.winner}")
        time.sleep(5)


    def createScreen(self):
        screen = turtle.Screen()
        screen.setup(self.WIDTH, self.HEIGHT)
        screen.title("Turtle racing")


    def get_numbers_of_racers(self):
        racers = 0
        while True:
            racers = input("Enter number of racers from 2 - 10: ")
            if racers.isdigit():
                racers = int(racers)
            else:
                print("Input must be digit!")
                continue

            if 2 <= racers <= 10:
                return racers
            else:
                print("Input is not in range 2 - 10!")


    def create_turtles(self, colors):
        turtles = []
        spacingX = self.WIDTH // (len(colors) + 1)
        for i, color in enumerate(colors):
            t = turtle.Turtle()
            t.color(color)
            t.shape('turtle')
            t.left(90)
            t.penup()
            t.setpos(-self.WIDTH//2 + (i+1) * spacingX, -self.HEIGHT//2 + 20)
            turtles.append(t)

        return turtles
    

    def race(self, colors):
        turtles = self.create_turtles(colors)
        
        while True:
            for turtle in turtles:
                distance = random.randint(1, 20)
                turtle.forward(distance)

                x, y = turtle.pos()
                if y >= self.HEIGHT//2 - 20:
                    turtle.left(720)
                    return colors[turtles.index(turtle)]



if __name__ == '__main__':
    t = TurtleApp()
