from nltk import sent_tokenize, word_tokenize,download
from nltk.corpus import stopwords
#download ('punkt')
#download ('stopwords')
from nltk.corpus import stopwords

#1
# text= " kirill and kirill freinds. Liza zhadina govydina!"
# sents= sent_tokenize(text)
# print(sents)
# 2
# sents="Были закреплены теоретические знания, полученные при изучении предметов «Компьютерный практикум», «Основы информатики», «Языки программирования и методы трансляции»; изучена деятельность по анализу литературы, сбору данных и построению алгоритмов решения практических задач; проверена степень готовности будущего бакалавра к самостоятельной работе; приобретены практические навыки  (опыт практической деятельности) в получении знаний, умения и навыки по программированию; был воспитан устойчивый интерес к профессии, убежденность в правильности ее выбора; было овладение методов приобретения профессиональных навыков работы; собрана необходимая для выполнения данной работы информация по месту прохождения практики, а также при изучении литературных и иных источников; приобретен опыт работы в коллективе."
# print(word_tokenize(sents))
# 4
# print(stopwords.words('russian'))
# 5
stop_words = set(stopwords.words('russian'))
sentence = 'Нарды - одна из старейших (старейшая) известных настольных игр.'

words = word_tokenize(sentence)
without_stop_words = [word for word in words if not word in stop_words]
print(without_stop_words)
