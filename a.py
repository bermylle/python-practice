list = [["Name", "Age", "Sex"], ["John", 30, "Male"]]
with open("writer.csv", "w") as csv_file:
    csv_reader = writer(csv_file)
    for i in range(0, len(list)):
        csv_reader.writerow(list[i])