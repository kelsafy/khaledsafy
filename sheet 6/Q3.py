
My_file = open("Sheet 6.txt", "a")
for S in range(1, 101):
    My_file.write(f"{S}\n")
My_file.close()