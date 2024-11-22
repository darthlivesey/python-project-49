from brain_games.games.brain_progression import brain_progression_logic, TEXT
from brain_games.game_logic import game_cycle


def main():
    game_cycle(TEXT, brain_progression_logic)
