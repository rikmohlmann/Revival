
class Player:
    def __init__(self, name="", age=0, gender=None, politics=None, 
                 health=70, talent=None, social=None):
        self.name = ""
        self.age = age
        self.gender = gender
        self.politics = politics
        self.health = health
        self.talent = talent
        self.social = social
        self.art_career = False

    def set_attributes(self):
        self.name = input("What's your name, adventurer? ")
        self.age = int(input("How old are you? "))
        self.gender = input("What gender do you identify with? ")
        self.politics = input("What are your political views? ")
        self.health = int(input("How would you rate your health on a scale of 0 to 100? "))
        self.talent = input("What is your talent? ")
        self.social = input("How would you describe your social skills? ")
       
    def revive_art_career(self):
        self.art_career = True

class Game:
    def __init__(self):
        self.player = Player()
        self.player.set_attributes()

    def start(self):
        print("Welcome to the Dutch coast!")
        print(f"Hello, {self.player.name}! It's time to revive your crumbled art career.")
        self.main_quest()

    def main_quest(self):
        print("You find yourself in a bustling art scene. The city's art scene has crumbled, but you have a chance to revive it.")
        print("You see a painting that seems to be missing a piece. You can either fix it or leave it.")
        choice = input("What do you do? (fix/leave) ")
        if choice.lower() == "fix":
            self.fix_painting()
        else:
            self.leave_painting()

    def fix_painting(self):
        print("You decide to fix the painting. It's a challenging task, but you manage to complete it.")
        print("The painting is now complete and you've revived your art career!")
        self.player.revive_art_career()
        self.end_game()

    def leave_painting(self):
        print("You decide to leave the painting alone. It's a shame, but you've learned a valuable lesson.")
        self.end_game()

    def end_game(self):
        if self.player.art_career:
            print(f"Congratulations, {self.player.name}! You've successfully revived your art career.")
        else:
            print(f"Sorry, {self.player.name}, but you didn't manage to revive your art career.")
        print("Thanks for playing!")

game = Game()
game.start()