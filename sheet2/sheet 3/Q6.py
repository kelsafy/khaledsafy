X1 = {'A': 1}
X2 = {'A': 2}
X3 = {'B': 3}
all_dicts = [X1, X2, X3]

fin_di = {}

for D in all_dicts:
    fin_di.update(D)

print(fin_di)