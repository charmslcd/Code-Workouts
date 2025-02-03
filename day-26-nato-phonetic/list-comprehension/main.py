
with open("file1.txt") as file1:
    file1_data = file1.readlines()
    file1_list = [int(line.strip()) for line in file1_data]

with open("file2.txt") as file2:
    file2_data = file2.readlines()
    file2_list = [int(line.strip()) for line in file2_data]

print(file1_list)
print(file2_list)

result = [num for num in file1_list if num in file2_list]

print(result)