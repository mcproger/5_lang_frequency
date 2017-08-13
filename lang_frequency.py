import string
import os
import collections


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as myfile:
        text = myfile.read()
        return text


def delete_punctuation_from_text(text):
    text = [word.replace(string.punctuation, '') for word in text]
    return text


def get_words_frequency(text):
    words_frequency = collections.Counter()
    for word in text:
        words_frequency[word.capitalize()] += 1
    return words_frequency


def get_most_frequent_words(text):
    filtered_text = delete_punctuation_from_text(text)
    words_frequency = get_words_frequency(filtered_text)
    most_frequent_words = words_frequency.most_common(10)
    return most_frequent_words


if __name__ == '__main__':
    filepath = input('Enter path to file with text: ')
    if load_data(filepath):
        text = load_data(filepath).split()
        most_frequent_words = get_most_frequent_words(text)
        for word, count in most_frequent_words:
            print(word, count)
    else:
        print('No such file in directory')
