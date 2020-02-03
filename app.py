#!/usr/bin/python3

from modules.board import Board
from modules.player import Player

def main():
    p1 = Player("X")
    p2 = Player("Y")
    players = [p1, p2]
    p1.has_turned = False

    b = Board()
    b.draw()

    game = True
    while game:
        for i, player in enumerate(players):
            if player.has_turned == False:
                val = input(f"{player.char}s Turn. Specify the Field on the Board you want to change: ")
                if b.check_val(val) == "0":
                    b.set_val(player, val)
                    player.has_turned = True
                    if i == 0:
                        players[1].has_turned = False
                    elif i == 1:
                        players[0].has_turned = False
                    b.draw()
                    ret = b.check_if_won(player)
                    if ret == player.char:
                        print(f"Player {player.char} has won!")
                        game = False
                        break
                    elif ret == "Tie":
                        print("Tie!")
                        game = False
                        break
                else:
                    val = input(f"{player.char}s Turn. Specify the Field on the Board you want to change: ")


if __name__ == "__main__":
    main()