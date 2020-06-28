import argparse
import re
from copy import deepcopy

from util import length_filtered_word_generator

KEYPAD_MAPPING = {'0': [],
                  '1': [],
                  '2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}


def get_matching_words(code_segment):
    # Hold all available words in memory and filter as we go
    all_words = list(length_filtered_word_generator(input_file=full_words, length=len(code_segment)))

    # Make a copy
    matching_words = deepcopy(all_words)

    for index in range(0, len(code_segment)):

        # Sync up the two lists
        all_words = deepcopy(matching_words)

        digit = code_segment[index]
        chars = KEYPAD_MAPPING[digit]
        # print('Digit: {}'.format(digit))

        for word in all_words:
            if word.lower()[index] not in chars:
                matching_words.remove(word)

    return [x.strip() for x in matching_words]


def get_matching_code(word):

    number_string = ''

    for character in word:
        for key, values in KEYPAD_MAPPING.items():
            if character in values:
                number_string += key

    return number_string


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input', required=True,
                            help='Numeric security code OR word')
    arg_parser.add_argument('--word-dictionary', default='/usr/share/dict/words',
                            help='newline-delimited list of words')
    args = arg_parser.parse_args()

    full_words = args.word_dictionary

    print('Input sequence: {}\n'.format(args.input))

    is_int = False
    try:
        int(args.input)
        is_int = True
    except ValueError:
        pass

    if is_int:
        code_string = str(args.input)

        # split on the unmapped integers
        delimiter_indexes = dict()
        delimiter_found = False
        for index in range(0, len(code_string)):
            if code_string[index] in ['0', '1']:
                delimiter_indexes[code_string[index]] = index
                delimiter_found = True

        code_segments = re.split('[01]', code_string)

        if delimiter_found:
            for digit, index in delimiter_indexes.items():
                print('Disregarding un-mappable digit \'{}\' at index {}'.format(digit, index))

        for segment in code_segments:
            matches = get_matching_words(segment)
            print(matches)

    else:
        code = get_matching_code(args.input)
        print('Your code is: {}'.format(code))
