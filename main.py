class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def play(self):
        print(f"{self.name} is playing {self.game.name}.")
        self.game.increment_score()

    def display_score(self):
        print(f"{self.name}'s score: {self.game.score}")


class Game:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_score(self):
        self.score += 1


game1 = Game("Chess")
player1 = Player("Yurii", game1)
player2 = Player("Yevhenii ", game1)

player1.play()
player2.play()
player1.display_score()
player2.display_score()
