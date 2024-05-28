import csv

with open('security_incidents_modified.csv', mode = 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("CSV file has been read.")