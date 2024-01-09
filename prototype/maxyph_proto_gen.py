import datetime as dt
import json
import random
import string

# globals
DATETIME_FORMAT = "%Y-%m-%d"

with open('guesswords.txt', 'r') as guesswords:
    guess_words = [line.rstrip() for line in guesswords]

def generate_puzzle() -> list:
    puzzle_state = []
    for i in range(6):
        if i == 0:
            while puzzle_state == []:
                seed_letter = random.choice(string.ascii_uppercase)
                seed_placement = random.choice(range(5))
                valid_count = 0
                for word in guess_words:
                    if word[seed_placement] == seed_letter.lower():
                        valid_count += 1
                    if valid_count > 4:
                        puzzle_state.append((seed_placement, seed_letter))
                        break
                else:
                    # puzzle generation failed to find 5 valid words for the first row
                    # trying again
                    pass
        else:
            valid_placements = list(range(5))
            valid_placements.remove(puzzle_state[i-1][0])
            seed_placement = random.choice(valid_placements)
            puzzle_state.append((seed_placement, ''))
    return puzzle_state


def solve_puzzle(puzzle: list) -> list():
    pass

def jsonify_puzzle_for_john(quantity: int) -> None:
    puzzle_dicts = []
    now = dt.datetime.now()
    delta = dt.timedelta(days=1)
    for _ in range(quantity):
        puzzle_vals = {}
        puzzle = generate_puzzle()
        puzzle_vals['date'] = now.strftime(DATETIME_FORMAT)
        puzzle_vals['puzzle'] = puzzle
        puzzle_dicts.append(puzzle_vals)
        now += delta
    json_puzzle_dicts = {'puzzles' : puzzle_dicts}

    with open('puzzles.json', 'w') as file:
        json.dump(json_puzzle_dicts, file)


if __name__ == '__main__':
    jsonify_puzzle_for_john(100)


