from dataclasses import dataclass
from datetime import datetime
from models.utils import SpannerTable
import csv


@dataclass
class HasDevice:
    id: str
    to_id: str
    ts: datetime

    def __init__(self, edge):
        self.id = edge["id"]
        self.to_id = edge["to_id"]
        self.ts = datetime.fromisoformat(edge["ts"])


@dataclass
class HasDevices(SpannerTable):
    def __init__(self):
        with open("data/HasDevice.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([HasDevice(row) for row in reader])


@dataclass
class DeviceHasCC:
    id: str
    to_id: str
    ts: datetime

    def __init__(self, edge):
        self.id = edge["id"]
        self.to_id = edge["to_id"]
        self.ts = datetime.fromisoformat(edge["ts"])


@dataclass
class DeviceHasCCs(SpannerTable):
    def __init__(self):
        with open("data/DeviceHasCC.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([DeviceHasCC(row) for row in reader])


@dataclass
class EmailHasCC:
    id: str
    to_id: str
    ts: datetime

    def __init__(self, edge):
        self.id = edge["id"]
        self.to_id = edge["to_id"]
        self.ts = datetime.fromisoformat(edge["ts"])


@dataclass
class EmailHasCCs(SpannerTable):
    def __init__(self):
        with open("data/EmailHasCC.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([EmailHasCC(row) for row in reader])


@dataclass
class DeviceHasIP:
    id: str
    to_id: str
    ts: datetime

    def __init__(self, edge):
        self.id = edge["id"]
        self.to_id = edge["to_id"]
        self.ts = datetime.fromisoformat(edge["ts"])


@dataclass
class DeviceHasIPs(SpannerTable):
    def __init__(self):
        with open("data/HasIP.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([DeviceHasIP(row) for row in reader])


@dataclass
class SalesOrderHasShippingAddress:
    id: str
    to_id: str
    ts: datetime

    def __init__(self, edge):
        self.id = edge["id"]
        self.to_id = edge["to_id"]
        self.ts = datetime.fromisoformat(edge["ts"])


@dataclass
class SalesOrderHasShippingAddresss(SpannerTable):
    def __init__(self):
        with open("data/HasAddress.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([SalesOrderHasShippingAddress(row) for row in reader])


@dataclass
class SalesOrderHasEmail:
    id: str
    to_id: str
    ts: datetime

    def __init__(self, edge):
        self.id = edge["id"]
        self.to_id = edge["to_id"]
        self.ts = datetime.fromisoformat(edge["ts"])


@dataclass
class SalesOrderHasEmails(SpannerTable):
    def __init__(self):
        with open("data/HasEmail.csv") as f:
            reader = csv.DictReader(f)
            self.loadItems([SalesOrderHasEmail(row) for row in reader])
