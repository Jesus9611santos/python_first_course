import json 

file_path = 'products.json'

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open(file_path, 'r') as file:
    products = json.load(file)
    
products.append(new_product)

with open(file_path, 'w') as file:
    json.dump(products,file, indent=4)