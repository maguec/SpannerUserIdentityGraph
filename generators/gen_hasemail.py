#!/usr/bin/env python

from faker import Faker
import csv, uuid
import constants

fake = Faker()

with open("../data/HasEmail.csv", "w") as csvfile:
    fieldnames = ["id", "to_id", "ts"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(constants.RECORD_COUNT):
        writer.writerow(
            {
                "id": uuid.UUID(int=i),
                "to_id": uuid.UUID(int=fake.random_int(0, constants.RECORD_COUNT-1)),
                "ts": fake.date_time_this_year(),
            }
        )
