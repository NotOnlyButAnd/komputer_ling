from pymorphy2 import MorphAnalyzer

# пример 1. Разбор слова
# morph = MorphAnalyzer()
# print(morph.parse('стали'))

# пример 2, 3. Получение нормальной формы и тэга
# morph = MorphAnalyzer()
# p = morph.parse('стали')[0]
# print(p.normal_form)    # нормалная
# print(p.normalized)     # форма
# print(p.tag)    # тэг. содержит инфу о слове: глагол, вид, число, время и тд - это все граммемы

# пример 4. Разбор несловарного слова
# работает на основе предсказателя, применяемого автоматически
# morph = MorphAnalyzer()
# print(morph.parse('бутявкоедами'))

# пример 5. Проверка, есть ли в теге граммема или все граммемы из сн-ва
# morph = MorphAnalyzer()
# p = morph.parse('стали')[0]
# print('VERB' in p.tag)
# print('NOUN' in p.tag)
# print({'plur', 'past'} in p.tag)
# print({'NOUN', 'plur'} in p.tag)

# пример 6. Получение характеристик слова. (None если не определена)
morph = MorphAnalyzer()
p = morph.parse('стали')[0]
# часть речи
print(p.tag.POS) # VERB
# одушевленность
print(p.tag.animacy) # None
# вид: совершенный или несовершенный
print(p.tag.aspect) # perf
# падеж
print(p.tag.case) # None
# род (мужской, женский, средний)
print(p.tag.gender) # None
# включенность говорящего в действие
print(p.tag.involvement) # None
# наклонение (повелительное, изъявительное)
print(p.tag.mood) # indc
# число (единственное, множественное)
print(p.tag.number) # plur
# лицо (1, 2, 3)
print(p.tag.person) # None
# время (настоящее, прошедшее, будущее)
print(p.tag.tense) # past
# переходность (переходный, непереходный)
print(p.tag.transitivity) # intr
# залог (действительный, страдательный)
print(p.tag.voice) # None
