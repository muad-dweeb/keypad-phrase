def length_filtered_word_generator(input_file, length):
    with open(input_file, 'r') as dictionary:
        words = dictionary.readlines()
        for word in words:
            if len(word) == length + 1:
                yield word
