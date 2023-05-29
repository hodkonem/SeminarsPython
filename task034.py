# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам

def has_same_rhythm(text):
    
    words = text.split()
    
    syllables_per_word = []
   
    for word in words:
        
        syllable_count = 0
       
        for letter in word:
           
            if letter in 'аеёиоуыэюя':
                syllable_count += 1
        
        syllables_per_word.append(syllable_count)
    
    return len(syllables_per_word) == syllables_per_word.count(syllables_per_word[0])


text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if has_same_rhythm(text):
    print('Парам пам-пам')
else:
    print('Пам парам')