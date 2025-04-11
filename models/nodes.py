from dataclasses import dataclass
from datetime import datetime
from models.utils import SpannerTable
import csv


@dataclass
class Device:
    id: str
    sus: int

    def __init__(self, item):
        self.id = item["id"]
        self.sus = item["sus"]


@dataclass
class Devices(SpannerTable):

    def __init__(self):
        with open("data/Device.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([Device(row) for row in reader])


@dataclass
class Email:
    id: str
    email: str
    sus: int

    def __init__(self, item):
        self.id = item["id"]
        self.item = item["email"]
        self.sus = item["sus"]


@dataclass
class Emails(SpannerTable):

    def __init__(self):
        with open("data/Email.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([Email(row) for row in reader])


@dataclass
class IP:
    id: str
    ip: str
    sus: int

    def __init__(self, item):
        self.id = item["id"]
        self.ip = item["ip"]
        self.sus = item["sus"]


@dataclass
class IPs(SpannerTable):

    def __init__(self):
        with open("data/IP.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([IP(row) for row in reader])


@dataclass
class CC:
    id: str
    last4: str
    zip: str
    sus: int

    def __init__(self, item):
        self.id = item["id"]
        self.last4 = item["last4"]
        self.sus = item["sus"]
        self.zip = item["zip"]


@dataclass
class CCs(SpannerTable):

    def __init__(self):
        with open("data/CC.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([CC(row) for row in reader])


@dataclass
class ShippingAddress:
    id: str
    address: str
    sus: int

    def __init__(self, item):
        self.id = item["id"]
        self.address = item["address"]
        self.sus = item["sus"]


@dataclass
class ShippingAddresss(SpannerTable):

    def __init__(self):
        with open("data/ShippingAddress.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([ShippingAddress(row) for row in reader])


@dataclass
class SalesOrder:
    id: str
    sus: int

    def __init__(self, item):
        self.id = item["id"]
        self.sus = item["sus"]


@dataclass
class SalesOrders(SpannerTable):

    def __init__(self):
        with open("data/SalesOrder.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([SalesOrder(row) for row in reader])
