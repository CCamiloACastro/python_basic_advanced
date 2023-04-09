# csv file
import csv

csv_file = open("csv_handling.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Camilo", "CCamiloACastro", 24, "Python", "https://github.com/ccamiloacastro"])
csv_writer.writerow(["nn", "avatar", 25, "COBOL", ""])

csv_file.close()

with open("csv_handling.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
