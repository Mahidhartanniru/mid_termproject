import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?', default='example_orders.json')
args = parser.parse_args()

customer = {}
with open (args.filename,'r') as f:
    data = json.load(f)
    for order in data:
        name =order["name"]
        phone = order ["phone"]
        customer[name]=phone
with open('customers.json','w') as f:
    json.dump(customer,f)
