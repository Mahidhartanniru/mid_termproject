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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input JSON file with orders')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as file:
            orders = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: JSON decoding failed for file '{args.input_file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    items = process_items(orders)

    output_file = "items.json"
    try:
        with open(output_file, 'w') as file:
            json.dump(items, file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred while saving items: {e}")

    print(f"Items information has been saved to '{output_file}'.")

if __name__ == "__main__":
    main()
