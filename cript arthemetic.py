def solve_cryptarithmetic(puzzle):
    # Extracting unique characters from the puzzle
    unique_chars = set()
    for word in puzzle.split():
        unique_chars.update(word)
    unique_chars = sorted(list(unique_chars))

    # Generating permutations of digits from 0 to 9 for unique characters
    for perm in generate_permutations(range(10), len(unique_chars)):
        digit_map = {char: digit for char, digit in zip(unique_chars, perm)}
        if is_valid_solution(puzzle, digit_map):
            return digit_map
    return None

def generate_permutations(elements, length):
    if length == 0:
        yield []
        return
    for element in elements:
        for sub_perm in generate_permutations(elements, length - 1):
            yield [element] + sub_perm

def is_valid_solution(puzzle, digit_map):
    words = puzzle.split()
    translated_words = []
    for word in words:
        translated_word = ""
        for char in word:
            translated_word += str(digit_map[char])
        translated_words.append(translated_word)

    if sum(int(word) for word in translated_words[:-1]) == int(translated_words[-1]):
        return True
    return False

if __name__ == "__main__":
    puzzle = "SEND + MORE == MONEY"
    solution = solve_cryptarithmetic(puzzle)
    if solution:
        print("Solution found:")
        for char, digit in solution.items():
            print(f"{char}: {digit}")
    else:
        print("No solution exists.")
