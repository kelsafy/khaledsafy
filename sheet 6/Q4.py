My_file = open("Sheet 6.txt", "r")
X = My_file.readlines()  
My_file.close()

for Z in X[49:60]:  
    print(Z.strip())  