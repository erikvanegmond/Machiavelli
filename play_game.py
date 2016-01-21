from game import Game

while True:
    n_players = input("How many players?")
    try:
        n_players = int(n_players)
    except ValueError:
        print("Entered value %s is not a number, try again" % n_players)
        continue

    if 2 <= n_players <= 7:
        break
    print("you can only play with 2 to 7 players")

game = Game(n_players)
while True:
    game.run()
