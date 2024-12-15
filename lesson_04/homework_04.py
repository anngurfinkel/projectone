adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")
"""

adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but .... remained to whitewash. .... \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""

new_line = adwentures_of_tom_sawer.replace("\n", " ")

print(new_line)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but .... remained to whitewash. .... \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""

new_line = adwentures_of_tom_sawer.replace("....", " ")

print(new_line)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his   face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked   and sweated in the sun, the retired artist sat on a barrel in the   shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but   remained to whitewash.   \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the   morning, Tom was literally rolling in wealth."""
import re

new_line = re.sub(r'\s+', ' ', adwentures_of_tom_sawer)
print(new_line)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but remained to whitewash. \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth."""

x = adwentures_of_tom_sawer.count("h")
print(x) # 40

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but .... remained to whitewash. .... \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""
print(adwentures_of_tom_sawer.split())

capitalized_words_count = sum(1 for word in adwentures_of_tom_sawer.split() if word[0].isupper())
print(capitalized_words_count) # 13

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but .... remained to whitewash. .... \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""

Tom_appeares_first_time = adwentures_of_tom_sawer.find("Tom")
print(Tom_appeares_first_time)

Tom_appeares_second_time = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)
print(Tom_appeares_second_time) # 469

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but .... remained to whitewash. .... \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""

import re

adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in re.split(r'[.!?]', adwentures_of_tom_sawer) if sentence.strip()]
print(adwentures_of_tom_sawer_sentences) 


** Process exited - Return Code: 0 **
Press Enter to exit terminal

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences = 'Tom gave up the brush with reluctance in his', 'face but alacrity in his heart', 'And while the late steamer "Big Missouri" worked', 'and sweated in the sun, the retired artist sat on a barrel in the', 'shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents', 'There was no lack of material; \nboys happened along every little while; \nthey came to jeer, but', 'remained to whitewash', 'By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour', 'And when the middle of the afternoon came, from being a poor poverty, stricken boy in the', 'morning, Tom was literally rolling in wealth'

four_sentence_lower = adwentures_of_tom_sawer_sentences[3].lower()
print(four_sentence_lower) #and sweated in the sun, the retired artist sat on a barrel in the

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his face but alacrity in his heart. \nAnd while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. \nThere was no lack of material; \nboys happened along every little while; \nthey came to jeer, but remained to whitewash. \nBy the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. \nAnd when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth."""

x = adwentures_of_tom_sawer.count("By the time")
print(x) # 1

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences = 'Tom gave up the brush with reluctance in his', 'face but alacrity in his heart', 'And while the late steamer "Big Missouri" worked', 'and sweated in the sun, the retired artist sat on a barrel in the', 'shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents', 'There was no lack of material; \nboys happened along every little while; \nthey came to jeer, but', 'remained to whitewash', 'By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; \nand when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour', 'And when the middle of the afternoon came, from being a poor poverty, stricken boy in the', 'morning, Tom was literally rolling in wealth'

last_sentence_word_count = len(adwentures_of_tom_sawer_sentences[-1].split())
print(last_sentence_word_count) #7