import json

#Lectura del archivos
with open('./products.json', mode='r') as file:
        products = json.load(file)

#Mostrar el contenido
for product in products:
        #print(product)
        print(f"Nombre: {product['name']} Producto: {product['price']}")