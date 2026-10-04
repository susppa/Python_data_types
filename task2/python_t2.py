def count_words_frequency(text):
    words = [word.strip('.,!?;:-') for word in text.lower().split()]
    return {word: words.count(word) for word in words}


def top_5_most_frequent(words_frequency):
    sorted_pairs = sorted(words_frequency.items(), key=lambda x: x[1], reverse=True)
    top_words = [word for word, count in sorted_pairs[:5]]
    return top_words


text = input('Enter text for word count: ')

print(f'Top 5 most frequent words (descending): {top_5_most_frequent(count_words_frequency(text))}')

# print(count_words_frequency(text))
# Кот сидит на окне и смотрит на улицу. Котик тоже сидит на окне. Кот любит рыбу, а котик любит молоко. На улице идёт дождь, и кот смотрит на дождь. КОТ спит, а котик играет. На окне тепло, на улице холодно.
