import string, os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as myfile:
    	text = myfile.read()
    	return text


def delete_punctuation_from_text(text):
	text = [word.replace(string.punctuation, '') for word in text]
	return text


def get_most_frequent_words(text):
    frequent_words = {}    
    for word in text:
    	frequent_words[word.capitalize()] = frequent_words.get(word.capitalize(), 0) + 1
    sorted_frequent_words = sorted(frequent_words.items(), key=lambda item: item[1], reverse=True)
    return sorted_frequent_words[:10]


if __name__ == '__main__':
    filepath = input('Enter path to file with text: ')
    text = load_data(filepath).split()
    text_without_punct = delete_punctuation_from_text(text)
    most_frequent_words = get_most_frequent_words(text_without_punct)
    for words in most_frequent_words:
        print(words[0], words[1])
    






