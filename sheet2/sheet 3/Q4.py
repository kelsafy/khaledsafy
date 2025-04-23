Sequence = [10, 20, 30, 40, 50, 60]

even_sum = 0
odd_sum = 0
X = 0

while X < len(Sequence):
    if X % 2 == 0:  
        even_sum += Sequence[X]
    else:  
        odd_sum += Sequence[X]
        X += 1

print(f" The of evens is: {even_sum} , and the sum of odds is: {odd_sum} .")