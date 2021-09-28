from nltk import sent_tokenize, word_tokenize,download
from nltk.corpus import stopwords

# Example 3
#download ('punkt')
#download ('stopwords')


# Example 1
# text= " kirill and kirill freinds. Liza zhadina govyadina!"
# sents= sent_tokenize(text)
# print(sents)

# Example 2
# sents="Были закреплены теоретические знания, полученные при изучении предметов «Компьютерный практикум», «Основы информатики», «Языки программирования и методы трансляции»; изучена деятельность по анализу литературы, сбору данных и построению алгоритмов решения практических задач; проверена степень готовности будущего бакалавра к самостоятельной работе; приобретены практические навыки  (опыт практической деятельности) в получении знаний, умения и навыки по программированию; был воспитан устойчивый интерес к профессии, убежденность в правильности ее выбора; было овладение методов приобретения профессиональных навыков работы; собрана необходимая для выполнения данной работы информация по месту прохождения практики, а также при изучении литературных и иных источников; приобретен опыт работы в коллективе."
# print(word_tokenize(sents))

# Example 4
# print(stopwords.words('russian'))

# Example 5
# stop_words = set(stopwords.words('russian'))
# sentence = 'Нарды - одна из старейших (старейшая) известных настольных игр.'
#
# words = word_tokenize(sentence)
# without_stop_words = [word for word in words if not word in stop_words]
# print(without_stop_words)

# Graphematic analyzer (Task 2)
f = open('sample_text.txt', 'r')

text = f.read()
print("Открыт файл sample_text.txt... Что для вас сделать?\n1 - разбить текст на предложения;\n2 - разбить текст на слова\n3 - разбить текст на слова, удалив стоп-слова")
choice = int(input())
if choice == 1:
    print('\nМинуту, сейчас сделаю...')
    print(sent_tokenize(text))
elif choice == 2:
    print('\nМинуту, сейчас сделаю...')
    print(word_tokenize(text))
elif choice == 3:
    print('\nМинуту, сейчас сделаю...')
    stop_words = set(stopwords.words('russian'))
    words = word_tokenize(text)
    print([word for word in words if not word in stop_words])
else:
    print('\nТакой команды я не знаю ＞﹏＜')
f.close()
