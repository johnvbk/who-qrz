#!/usr/bin/env python3
from qrz import QRZ, CallsignNotFound, QRZsessionNotFound
import argparse

qrz = QRZ('./settings.cfg')

parser = argparse.ArgumentParser(prog='who-qrz', description='Callsign Lookup')
parser.add_argument('callsign', help='The callsign you wish to lookup.')
args = parser.parse_args()
cs = vars(args)['callsign']

try:
    result = qrz.callsign(cs)
    print(f"{result['call']} - {result['fname']} {result['name']}")
    print(f"{result['addr2']}, {result['state']} {result['country']}")
except CallsignNotFound as e:
    print(f"callsign {cs} not found")
except QRZsessionNotFound as e:
    print(f"could not obtain session from qrz, check credentials config or environment vars")
except Exception as e:
    print(f"Unknown error: {e}")
