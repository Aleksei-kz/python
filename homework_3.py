t1_text = open('text_3.txt', 'r', encoding='utf-8')
workers = {}
sum_zp = 0
people = 0
for el_t1 in t1_text:
    key, value = el_t1.split()
    workers[key] = value
    sum_zp += float(value)
    people +=1
    if float(value) < 20000:
        print(f'{key}:{value} зарплата меньше 20000')
print(f"Средняя величина дохода сотрудников : {sum_zp / people:.2f}")
t1_text.close()