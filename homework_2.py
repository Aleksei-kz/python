t1_txt = open("HW_2.txt", "r")
len_t1 = 0
len_el_t1 = 0
for el_t1 in t1_txt:
    len_t1 += 1
    for el in el_t1:
        if el == " " or el == "\n":
            len_el_t1 += 1
    print(el_t1, end="")

print(f"Количество строк в тексте : {len_t1}, количество слов {len_el_t1}.")
t1_txt.close()