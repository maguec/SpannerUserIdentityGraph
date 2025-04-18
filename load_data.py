#!/usr/bin/env python

from models.nodes import *
from models.edges import *
from google.cloud import spanner

def LoadData():

    s = spanner.Client()
    instance = s.instance("useridentity")
    client = instance.database("useridentitydb")

    print("Loading Data...")

    emails = Emails()
    emails.load(client)

    ccs = CCs()
    ccs.load(client)

    addresses = ShippingAddresss()
    addresses.load(client)

    orders = SalesOrders()
    orders.load(client)

    devices = Devices()
    devices.load(client)

    device_has_ccs = DeviceHasCCs()
    device_has_ccs.load(client)

    email_has_ccs = EmailHasCCs()
    email_has_ccs.load(client)

    has_devices = HasDevices()
    has_devices.load(client)

    ips = IPs()
    ips.load(client)

    has_ips = DeviceHasIPs()
    has_ips.load(client)

    has_addresses = SalesOrderHasShippingAddresss()
    has_addresses.load(client)

    has_emails = SalesOrderHasEmails()
    has_emails.load(client)

    print("Loading Complete...")

if __name__ == "__main__":
    LoadData()
