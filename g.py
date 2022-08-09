
import random
class game:
    def __init__(self) -> None:
        self.game = False
        print("Welcome")
        self.w()
    def w(self):
        while self.game == False:
            n = random.randint(0, 100)
            self.g(n)
            w1 = input("Try agagin? y/n")
            if w1== "n":
                break
    def g(self,n):
        gue = -1
        while gue != n:
            gue = input("Guess the number\n")
            if gue.isnumeric():
                gue= int(gue)
                if gue>n:
                    print("number is smaller than The guess\n")
                elif gue<n:
                    print("number is bigger than The guess\n")
            
        print("congratulations,you guessed the number")
game()           