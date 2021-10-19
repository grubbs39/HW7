coloumn1 = []
coloumn2 = []
coloumn3 = []
coloumn4 = []

print("input the file you want checked: ")
input_file_name = input()
f = open(input_file_name)

for row in f:
    fields = row[:-1].split('\t')
    coloumn1.append(fields[0])
    coloumn2.append(fields[1])
    coloumn3.append(fields[2])
    coloumn4.append(fields[3])


for row in range(len(coloumn4)):
    if coloumn4[row] == "Available":
        print(coloumn2[row] + " (" + coloumn1[row] + ") --" + coloumn3[row])
