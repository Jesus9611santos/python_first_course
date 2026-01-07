# =========================
# ABSTRACCIÓN + ENCAPSULACIÓN
# =========================
class Vehicle:
    def __init__(self,brand,model,price):
        # ENCAPSULACIÓN:
        # Estos atributos representan el estado interno del objeto
        # y deben ser accedidos/modificados mediante métodos.
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        # ENCAPSULACIÓN:
        # El estado 'is_available' solo se modifica a través de este método,
        # no directamente desde fuera del objeto.
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible")

    def check_available(self):
        # ENCAPSULACIÓN:
        # Método que expone el estado interno de forma controlada.
        return self.is_available
    
    def get_price(self):
        # ENCAPSULACIÓN:
        # Acceso controlado al atributo price.
        return self.price
    
    def start_engine(self):
        # ABSTRACCIÓN:
        # Se define el comportamiento esperado para todo Vehicle,
        # pero se oculta la implementación concreta.
        raise NotImplementedError("El metodo debe ser implementado por la clase hija")
    
    def stop_engine(self):
        # ABSTRACCIÓN:
        # Obliga a las clases hijas a implementar este comportamiento.
        raise NotImplementedError("El metodo debe ser implementado por la clase hija")


# =========================
# HERENCIA + POLIMORFISMO
# =========================
class Car(Vehicle):
    # HERENCIA:
    # Car hereda atributos y métodos de Vehicle.

    def start_engine(self):
        # POLIMORFISMO:
        # Implementación específica del mismo método definido en Vehicle.
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"
    
    def stop_engine(self):
        # POLIMORFISMO:
        # Mismo método, comportamiento distinto según la clase.
        if not self.is_available:
            return f"El motor del coche {self.brand} está apagado"
        else:
            return f"El coche {self.brand} no está disponible"
        

class Bike(Vehicle):
    # HERENCIA:
    # Bike reutiliza la estructura definida en Vehicle.

    def start_engine(self):
        # POLIMORFISMO:
        # Bike implementa el comportamiento a su manera.
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"
    
    def stop_engine(self):
        # POLIMORFISMO:
        if not self.is_available:
            return f"La bicicleta {self.brand} está apagado"
        else:
            return f"La bicicleta {self.brand} no está disponible"
        

class Truck(Vehicle):
    # HERENCIA:
    # Truck es un Vehicle con comportamiento específico.

    def start_engine(self):
        # POLIMORFISMO:
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
    
    def stop_engine(self):
        # POLIMORFISMO:
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} No está disponible"
        

# =========================
# POLIMORFISMO + ENCAPSULACIÓN
# =========================
class Customer:
    def __init__(self, name):
        # ENCAPSULACIÓN:
        # Estado interno del cliente.
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        # POLIMORFISMO:
        # El cliente no sabe si recibe Car, Bike o Truck,
        # solo sabe que es un Vehicle.
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento,{vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        # POLIMORFISMO + ENCAPSULACIÓN:
        # Usa métodos del Vehicle sin acceder directamente a sus atributos.
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}")


# =========================
# ABSTRACCIÓN + POLIMORFISMO
# =========================
class Dealership:
    def __init__(self):
        # ENCAPSULACIÓN:
        # Inventario y clientes gestionados internamente.
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        # POLIMORFISMO:
        # El concesionario acepta cualquier objeto de tipo Vehicle.
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        # ABSTRACCIÓN:
        # Se trabaja con la idea de "vehículos", sin importar el tipo concreto.
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")


# =========================
# USO DE HERENCIA
# =========================
# Nunca se crean objetos de la clase padre “a través” de las hijas.
# Se crean instancias de las clases hijas que heredan de Vehicle.
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()