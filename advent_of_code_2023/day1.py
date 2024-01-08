

import re


def replace_words_with_numbers(line, word_to_num, substitutions):
    # Perform specific substitutions
    for old, new in substitutions.items():
        line = line.replace(old, new)

    # Replace words with numbers using regex
    word_re = re.compile(r'one|two|three|four|five|six|seven|eight|nine')
    return re.sub(word_re, lambda match: word_to_num[match.group(0)], line)



def process_line(line, word_to_num, substitutions):
    # Perform specific substitutions and replace words with numbers
    new_line = replace_words_with_numbers(line, word_to_num, substitutions)
    digits = re.findall(r"[1-9]", new_line)
    return int(digits[0] + digits[-1])


def main():
    filepath = "/Users/rebeccasansale/Documents/advent_of_code_2023/day_1.txt"
    print("Adventing the code: Day 1")
    final_sum = 0
    linecount = 0
    nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    substitutions = {"oneight":"oneeight",
                     "twone": "twoone",
                     "threeight": "threeeight",
                     "fiveight": "fiveeight",
                     "sevenine": "sevennine", 
                     "eightwo": "eighttwo",
                     "eighthree": "eightthree",
                     "nineight": "nineeight"}  # Add more substitutions as needed

    with open(filepath, 'r') as f:
        for line in f:
            try: #using try since i dont know how errors will be handled
                a = process_line(line, nums, substitutions)
                final_sum += a
                linecount += 1
            except Exception as e:
                print(f"Error processing line: {line.strip()}. Error: {e}")

    print(f"FINAL SUM: {final_sum}, processed {linecount} lines.")

main()