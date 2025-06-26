#!/usr/bin/env python

from faker import Faker
import csv, re
import constants

def extract_numbers_regex(input_string):
    return re.sub(r'[^0-9]', '', input_string)

fake = Faker()
rows = []

with open("../data/Device.csv") as inputfile:
    reader = csv.DictReader(inputfile)
    for row in reader:
        row['phone'] = extract_numbers_regex(fake.basic_phone_number())
        rows.append(row)

        

with open("../data/DevicewithPhone.csv", "w") as csvfile:
    fieldnames = ["id", "sus", "phone"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        writer.writerow(row)
