l = [25, 10, 1995, "Tushar", "Gohel"]
d = {"tushar": 8866387371, "vatsal": 9408377888, "dapu": 940967101}
main_list = []
main_list.append(l)
main_list.append(d)
print(main_list)

for x in range(0, 2):
    if type(x) == dict:
        print(main_list[x].keys())
        print(main_list[x].values())
