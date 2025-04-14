#!/usr/bin/env python

import uuid
import csv
import constants
from faker import Faker

fake = Faker()
is_sus = lambda: 1 if fake.random_int(0,99) < constants.SUS_PERCENT else 0

with open("../data/CC.csv", "w") as csvfile:
    fieldnames = ["id", "last4", "zip", "sus"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(constants.RECORD_COUNT):
        ccid = fake.credit_card_number(card_type="visa")[-4:]
        pc = fake.postcode()
        writer.writerow(
            {
                "id": uuid.UUID(int=i),
                "last4": ccid,
                "zip": pc,
                "sus":  is_sus()
            }
        )
