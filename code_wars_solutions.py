import re
import string


# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"
# Write function bmi that calculates body mass index (bmi = weight / height ^ 2).


def order(words: str) -> str:
    if not words:
        return ""
    words_split = words.split()
    new_list = [0] * len(words_split)
    for word in words_split:
        for character in word:
            if character.isdigit():
                character_num = int(character)
                new_list[character_num - 1] = str(word)
    return " ".join(new_list)


def bmi(weight: int, height: int) -> str:
    bmi = weight / pow(height, 2)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25:
        return "Normal"
    if bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


def valid_spacing2(s):
    s_split = s.split()
    join_s_split = " ".join(s_split)
    if s == join_s_split:
        return True
    else:
        return False


def valid_spacing(s):
    if s == "":
        return True

    if s[0] == " ":
        print("space at beginning")
        return False

    if s[-1] == " ":
        print("space at end")
        return False

    if "  " in s:
        return False

    else:
        return True
        print("I returned True!")


def rotateleft(d, arr):
    while d != 0:
        arr.append(arr.pop(0))
        d -= 1
    return arr


def count_ways(n, k):
    if n > k:
        return k


def pig_it(sentence):
    sentence_split = sentence.split(" ")
    pig_sentence = []
    for word in sentence_split:
        if word in string.punctuation:
            pig_sentence.append(word)
        else:
            pig_sentence.append(f"{word[1:]}{word[0]}ay")
    return " ".join(pig_sentence)


def solve_element_parity(arr):
    for number in arr:
        if (number * -1) not in arr:
            return number


def fake_binary(input_string):
    def convert_num(number):
        below = ["0", "1", "2", "3", "4"]

        if number in below:
            return "0"
        return "1"

    new_string = [convert_num(number) for number in input_string]
    return "".join(new_string)


def weather_info(f_temp):
    c_temp = convert_to_celsius(f_temp)
    if c_temp > 0:
        return f"{c_temp} is above freezing temperature"
    else:
        return f"{c_temp} is freezing temperature"


def convert_to_celsius(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp


def remove_leftmost_duplicates(array_obj):
    array_obj.reverse()

    new_list = []

    for element in array_obj:
        if element not in new_list:
            new_list.append(element)

    new_list.reverse()

    return new_list


class User:
    ranks = [rank for rank in range(-8, 9) if rank != 0]

    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.level_index = User.ranks.index(self.rank)

    def check_level(self):
        while self.progress >= 100 and self.rank != User.ranks[-1]:
            self.rank = User.ranks[self.level_index + 1]
            self.level_index += 1
            self.progress -= 100

        if self.rank == 8:
            self.progress = 0

    def inc_progress(self, rank_of_activity):
        activity_level = User.ranks.index(rank_of_activity)
        rank_difference = abs(User.ranks.index(rank_of_activity) - self.level_index)

        if rank_of_activity not in User.ranks:
            raise ValueError

        elif self.rank == User.ranks[-1]:
            return

        elif activity_level < (self.level_index - 1):
            return

        elif rank_difference == 0:
            self.progress += 3

        elif activity_level == (self.level_index - 1):
            self.progress += 1

        else:
            self.progress += 10 * rank_difference * rank_difference

        self.check_level()


def parse_molecule(formula):
    def add_to_element_dict(dict_obj, element, atoms=1) -> dict:
        try:
            dict_obj[element] += int(atoms)
        except KeyError:
            dict_obj[element] = int(atoms)

        return dict_obj

    def smart_combine_dicts(dict_objs: list):
        base_dict = dict_objs[0]

        for dict_obj in dict_objs:
            for element, atoms in dict_obj.items():
                add_to_element_dict(base_dict, element, atoms)

        return base_dict

    def parse_standalone_molecules(formula) -> dict:
        temp_dict = {}
        two_character_molecule_pattern = re.compile("([A-Z][a-z]\d*)")
        matches = two_character_molecule_pattern.findall(formula)
        if matches:
            try:
                add_to_element_dict(temp_dict, matches[0], matches[1])
            except IndexError:
                add_to_element_dict(temp_dict, matches[0])

        single_character_molecule_pattern = re.compile("([A-Z]\d*)")
        matches = single_character_molecule_pattern.findall(formula)
        if matches:
            for match in matches:
                if len(match) > 1:
                    add_to_element_dict(temp_dict, element=match[0], atoms=match[1])
                else:
                    add_to_element_dict(temp_dict, element=match)

        return temp_dict

    def parse_brackets(formula):
        temp_dict = {}
        non_capture_open_bracket = "(?:\[)"
        non_capture_close_bracket = "(?:\])"
        bracket_pattern = re.compile(
            f"{non_capture_open_bracket}(.+){non_capture_close_bracket}(\d+)"
        )

        matches = bracket_pattern.findall(formula)
        for match in matches:
            sub_formula = match[0]
            count = int(match[1])
            for i in range(count):
                sub_dict = parse_molecule(sub_formula)
                temp_dict = smart_combine_dicts(temp_dict, sub_dict)

        return temp_dict

    def parse_parentheses(formula):
        non_capture_open_parenthesis = "(?:\()"
        non_capture_close_parenthesis = "(?:\))"
        parenthesis_pattern = re.compile(
            f"{non_capture_open_parenthesis}(.+){non_capture_close_parenthesis}(\d*)"
        )
        matches = parenthesis_pattern.findall(formula)

        for match in matches:
            multiplier = int(match[1])
            temp_molecule_dict = parse_standalone_molecules(match[0])
            temp_molecule_dict = {
                key: value * multiplier for key, value in temp_molecule_dict.items()
            }

        return temp_molecule_dict

    if "[" in formula:
        bracket_molecules = parse_brackets(formula)

    if "(" in formula:
        parentheses_molecules = parse_parentheses(formula)

    standalone_molecules = parse_standalone_molecules(formula)

    return True


def rgb(r, g, b):
    def get_hex_from_RGB_val(val):
        hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        if val <= 0:
            return "00"

        elif val > 255:
            return "FF"

        elif 0 < val < 10:
            return f"{val:02}"

        else:
            floor_division_by_16 = val // 16
            remainder = val % 16
            if 10 <= remainder <= 15:
                remainder = hex_dict[remainder]

            if 10 <= floor_division_by_16 <= 15:
                result = f"{hex_dict[floor_division_by_16]}{remainder}"

            elif floor_division_by_16 < 10:
                result = f"{floor_division_by_16}{remainder}"

            return result

    convert = get_hex_from_RGB_val
    return f"{convert(r)}{convert(g)}{convert(b)}"


def is_pangram(s):
    s = s.lower()
    alphabet = string.ascii_lowercase

    if len(set(alphabet).intersection(s)) == 26:
        return True

    return False


def valid_parentheses(s):
    if not s:
        return True
    elif s.count("(") != s.count(")"):
        return False

    parentheses_string = "".join([character for character in s if character in "()"])
    while True:
        parentheses_string = parentheses_string.replace("()", "")
        if parentheses_string == ")(":
            return False
        if parentheses_string == "":
            return True


def solution(s):
    if not s:
        return []

    split_string = [(s[index : index + 2]) for index in range(0, len(s), 2)]

    if len(split_string[-1]) == 1:
        split_string[-1] += "_"
    return split_string


def make_readable(seconds):
    whole_hours = seconds // 3600 if seconds >= 3600 else 0
    remainder_seconds = seconds % 3600
    whole_minutes = remainder_seconds // 60 if 0 < remainder_seconds < 3600 else 0
    whole_seconds = remainder_seconds % 60

    return f"{whole_hours:02}:{whole_minutes:02}:{whole_seconds:02}"


def create_phone_number(numbers: list):
    number_string = "".join(str(digit) for digit in numbers)

    return f"({number_string[:3]}) {number_string[3:6]}-{number_string[6:10]}"


def comp(array1, array2):
    if not array1 and not array2:
        return False

    a_squared = [pow(number, 2) for number in array1]
    if set(a_squared) == set(array2):
        return True
    return False


def decode_morse(code):
    morse_code_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "--..--": ", ",
        ".-.-.-": ".",
        "..--..": "?",
        "-..-.": "/",
        "-....-": "-",
        "-.--.": "(",
        "-.--.-": ")",
    }

    translated_message = " ".join(
        [
            "".join(
                [morse_code_dict[morse_letter] for morse_letter in morse_word.split()]
            )
            for morse_word in code.split("   ")
        ]
    )

    return translated_message.strip()


def find_outlier(integers: list):
    def check_int_type(integer, int_type):
        remainder = integer % 2
        if remainder == 1 and int_type == "even":
            return False

        elif remainder == 0 and int_type == "odd":
            return False

        else:
            return True

    even_count = 0
    current_type = "even"
    for i in integers[:3]:
        if check_int_type(i, current_type):
            even_count += 1

    current_type = current_type if even_count >= 2 else "odd"

    for number in integers:
        if not check_int_type(number, current_type):
            return number


def song_decoder(song: str):
    removed_wubs = [word for word in song.split("WUB") if word != "WUB"]
    while "" in removed_wubs:
        removed_wubs.remove("")
    final_string = " ".join(removed_wubs)
    return final_string


def digital_root_sum(n):
    while n > 10:
        n = sum((int(n) for n in str(n)))
    return n


def fizz_buzz(num):
    if num == 0:
        return 0

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    elif num % 3 == 0:
        return "Fizz"

    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def fibonacci(num):
    a, b = 0, 1

    for i in range(0, num):
        print(a)
        a, b = b, a + b


# Generator examples
def fibonacci_generator(num):
    a, b = 0, 1

    for i in range(0, num):
        yield a
        a, b = b, a + b


def sentence_gen_func(sentence):
    for word in sentence.split():
        yield word


class Sentence1:
    def __init__(self, sentence):
        self.sentence_iterator = iter(sentence.split())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.sentence_iterator)


class Sentence2:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current_index = self.index
        self.index += 1
        return self.words[current_index]
