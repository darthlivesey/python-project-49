from brain_games.games.brain_calc import brain_calc_logic, TEXT
from brain_games.game_logic import game_cycle


def main():
    game_cycle(TEXT, brain_calc_logic)
