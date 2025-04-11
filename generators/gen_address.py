#!/usr/bin/env python

from faker import Faker
import csv, uuid
import constants

fake = Faker()
is_sus = lambda: 1 if fake.random_int(0,99) < constants.SUS_PERCENT else 0

with open("../data/ShippingAddress.csv", "w") as csvfile:
    fieldnames = ["id", "address", "sus"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(constants.RECORD_COUNT):
        writer.writerow(
            {
                "id": uuid.UUID(int=i),
                "address": fake.address().replace("\n", ""),
                "sus": is_sus()
            }
        )
