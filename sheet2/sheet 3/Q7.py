Numbers_1 = [10, 20, 30]
Numbers_2 = [10, 20, 30, 10, 40,  20, 30, 20, 30 , 10] #[10, 20, 30, 40]

unique_X = len(set(Numbers_1))
unique_Y = len(set(Numbers_2))

print(f"Unique numbers in Numbers_1: {unique_X} , Unique numbers in Numbers_2: {unique_Y}")