import random

a = random.randint(0, 10)
b = random.randrange(9)

if a < b: text = 'проиграла'
elif a > b: text = 'выиграла у'
else: text = 'сыграла в ничью со'

print("Сегодня сборная \"Имбицилы\"", text, "сборной \"Дибилоиды\" со счетом ", a, ":", b)