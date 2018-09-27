import file1.F as file_utils

csv = "/Users/saikris/Downloads/persondata20151016.txt"
file_utils.read(csv, "")

option = "y"
while option == "y":
    row_num = int(input("Enter the rownum: "))
    print(file_utils.readRow(csv, row_num))
    option = input("Continue? y/n: ")
