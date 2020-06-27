t1_txt = open("HW_1.txt", "w", encoding="utf-8")
while True:
    info = input("Введите ваши данные - ")
    if info == "":
        break
    t1_txt.write(info + '\n')
t1_txt.close()

t2_txt = open("HW_1.txt", "r", encoding="utf-8")
for el_t2 in t2_txt:
    print(el_t2, end="")
t2_txt.close()
