def popular_words (text, words):
    words_in_text = []
    population_of_words = {}
# Наступний алгоритм дозволить виконати поставлене завдання,
# навіть якщо в тексті будуть розділові знаки
    for i in text.lower().split(' '):
        word = []
        for j in i:
            if j.isalpha():
                word.extend(j)
        words_in_text.append(''.join(word))
    for i in words:
        population_of_words[i] = words_in_text.count(i)
    return population_of_words


assert popular_words('''When I was One I, had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# Додаткові перевірки
assert popular_words('''When (I) was One I, had just begun When ^I wAs Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test2'
assert popular_words('''Небо, край (Земля), земля - то край''', ['небо', 'земля', 'пайтон', 'near']) == { 'небо': 1, 'земля': 2, 'пайтон': 0, 'near': 0 }, 'Test3'
print('OK')