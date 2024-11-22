from brain_games.games.brain_gcd import brain_gcd_logic, TEXT
from brain_games.game_logic import game_cycle


def main():
    game_cycle(TEXT, brain_gcd_logic)
