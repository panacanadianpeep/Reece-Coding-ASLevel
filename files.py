import csv

with open("testing.txt", mode="a") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    csv_writer.writerow(['Hello', 'Sebastian'])

with open("testing.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Column names are: ", row)
        else:
            print(row)
        line_count+=1
    print("Processed", line_count, "lines")