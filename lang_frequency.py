import string
import os
import collections
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as myfile:
        text = myfile.read()
        return text.lower()


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str,
                        help='file containing text for frequency analize')
    parser.add_argument('words_count', type=int,
                        help='The number of words that should be displayed in the console')
    args = parser.parse_args()
    return args


def delete_punctuation_from_text(text):
    text = [word.replace(string.punctuation, '') for word in text]
    return text


def get_most_frequent_words(text, words_count):
    filtered_text = delete_punctuation_from_text(text)
    words_frequency = collections.Counter(filtered_text)
    most_frequent_words = words_frequency.most_common(words_count)
    return most_frequent_words


if __name__ == '__main__':
    args = get_argparser()
    if not load_data(args.filepath):
        print('No such file in directory')
    else:
        text = load_data(args.filepath).split()
        most_frequent_words = get_most_frequent_words(text, args.words_count)
        for word, count in most_frequent_words:
            print(word, count)      