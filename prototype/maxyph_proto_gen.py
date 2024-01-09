import random
import string


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

if __name__ == "__main__":
  for _ in range(100):
      print(generate_puzzle())


