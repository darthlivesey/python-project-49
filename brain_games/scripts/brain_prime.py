from brain_games.games.brain_prime import brain_prime_logic, TEXT
from brain_games.game_logic import game_cycle


def main():
    game_cycle(TEXT, brain_prime_logic)
