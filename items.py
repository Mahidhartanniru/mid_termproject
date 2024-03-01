import argparse
import json

def process_items(orders):
    items = {}
    for order in orders:
        for item in order.get('items', []):
            item_name = item.get('name')
            item_price = item.get('price')
            if item_name:
                if item_name not in items:
                    items[item_name] = {
                        "price": item_price,
                        "orders": 1
                    }
                else:
                    items[item_name]["orders"] += 1
    return items

