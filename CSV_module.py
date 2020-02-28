import csv

with open("oscar_age_male.csv", "r") as f:
    csv_read = csv.reader(f)
    with open("csv_writer.csv", "w") as new_f:
        csv_write = csv.writer(new_f, delimiter = "\t")
        for line in csv_read:
            csv_write.writerow(line)
            
with open("csv_writer.csv", "r") as f:
    csv_read = csv.DictReader(f, delimiter = "\t")
    with open("csv_DictWriter", "w") as new_f:
        fields = ["Year", "Age", "Name", "Movie"]
        csv_write = csv.DictWriter(new_f, fieldnames = fields, delimiter = "\t")
        csv_write.writeheader() #This writes the fieldnames as a row
        for line in csv_read:
            del(line['Index'])
            csv_write.writerow(line)