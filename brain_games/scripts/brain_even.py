from brain_games.games.brain_even import brain_even_logic, TEXT
from brain_games.game_logic import game_cycle


def main():
    game_cycle(TEXT, brain_even_logic)
