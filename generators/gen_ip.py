#!/usr/bin/env python

import uuid
import csv
import constants
from faker import Faker

fake = Faker()
is_sus = lambda: 1 if fake.random_int(0,99) < constants.SUS_PERCENT else 0

with open("../data/IP.csv", "w") as csvfile:
    fieldnames = ["id", "ip", "sus"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(constants.RECORD_COUNT):
        writer.writerow(
            {
                "id": uuid.UUID(int=i),
                "ip": fake.ipv4(),
                "sus":  is_sus()
            }
        )
