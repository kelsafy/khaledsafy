file_name = "/home/user/projects/my_project/file.txt"
X = file_name.split('/')[-1]
name , file_type = X.split('.')
print("File Name:", name)
print("File Type:", file_type)