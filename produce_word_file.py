import os
import argparse


def length_filtered_word_generator(input_file, length):
    with open(input_file, 'r') as dictionary:
        words = dictionary.readlines()
        for word in words:
            if len(word) == length + 1:
                yield word


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input', default='/usr/share/dict/words', help='newline-delimited list of words')
    arg_parser.add_argument('--output', required=True, help='newline-delimited list of filtered words')
    arg_parser.add_argument('--length', required=True, type=int, help='desired length of the output words')
    args = arg_parser.parse_args()

    input_file_path = os.path.expanduser(args.input)
    output_file_path = os.path.expanduser(args.output)

    with open(output_file_path, 'w') as new_dictionary:
        count = 0
        for wanted_word in length_filtered_word_generator(input_file=input_file_path, length=args.length):
            new_dictionary.write(wanted_word)
            count += 1

    print('{} {}-character words have been saved to: {}'.format(count, args.length, output_file_path))
