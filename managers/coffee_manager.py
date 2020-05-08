import doctest
from models.coffee import Coffee


class CoffeeManager:

    def __init__(self):
        self.coffees = []

    def add_coffee(self, *coffee_to_add: Coffee):
        for coffee in coffee_to_add:
            self.coffees.append(coffee)

    def remove_coffee(self, *coffee_to_remove: Coffee):
        for coffee in coffee_to_remove:
            self.coffees.remove(coffee)

    def find_coffee_by_price(self, price_to_compare):
        """
        >>> americano = Coffee("Grain", 100, "Can", "Colombia", "Light", 23.5)
        >>> latte = Coffee("Ground", 250, "Packet", "Brasil", "Medium", 36.0)
        >>> cocoa = Coffee("Instant", 180, "Can", "Ethiopia", "Dark", 21.0)
        >>> order = CoffeeManager()
        >>> order.add_coffee(americano, latte, cocoa)
        >>> result = order.find_coffee_by_price(30)
        >>> [coffee.price_in_UAH for coffee in result]
        [23.5, 21.0]
        """
        result: list = []
        for coffee in self.coffees:
            if coffee.price_in_UAH < price_to_compare:
                result.append(coffee)
        return result

    def find_coffee_by_capacity(self, capacity_in_mL_to_compare):
        """
        >>> americano = Coffee("Grain", 100, "Can", "Colombia", "Light", 23.5)
        >>> latte = Coffee("Ground", 250, "Packet", "Brasil", "Medium", 36.0)
        >>> cocoa = Coffee("Instant", 180, "Can", "Ethiopia", "Dark", 21.0)
        >>> order = CoffeeManager()
        >>> order.add_coffee(americano, latte, cocoa)
        >>> result = order.find_coffee_by_capacity(200)
        >>> [coffee.capacity_in_mL for coffee in result]
        [250]
        """
        result: list = []
        for coffee in self.coffees:
            if coffee.capacity_in_mL > capacity_in_mL_to_compare:
                result.append(coffee)
        return result

    def sort_coffees_by_price(self, reverse=False):
        """
        >>> americano = Coffee("Grain", 100, "Can", "Colombia", "Light", 23.5)
        >>> latte = Coffee("Ground", 250, "Packet", "Brasil", "Medium", 36.0)
        >>> cocoa = Coffee("Instant", 180, "Can", "Ethiopia", "Dark", 21.0)
        >>> order = CoffeeManager()
        >>> order.add_coffee(americano, latte, cocoa)
        >>> order.sort_coffees_by_price()
        >>> [coffee.price_in_UAH for coffee in order.coffees]
        [21.0, 23.5, 36.0]
        >>> order.sort_coffees_by_price(reverse=True)
        >>> [coffee.price_in_UAH for coffee in order.coffees]
        [36.0, 23.5, 21.0]
        """
        self.coffees.sort(reverse=reverse, key=lambda coffee: coffee.price_in_UAH)

    def sort_coffees_by_capacity(self, reverse=True):
        """
        >>> americano = Coffee("Grain", 100, "Can", "Colombia", "Light", 23.5)
        >>> latte = Coffee("Ground", 250, "Packet", "Brasil", "Medium", 36.0)
        >>> cocoa = Coffee("Instant", 180, "Can", "Ethiopia", "Dark", 21.0)
        >>> order = CoffeeManager()
        >>> order.add_coffee(americano, latte, cocoa)
        >>> order.sort_coffees_by_capacity(reverse=False)
        >>> [coffee.capacity_in_mL for coffee in order.coffees]
        [100, 180, 250]
        >>> order.sort_coffees_by_capacity(reverse=True)
        >>> [coffee.capacity_in_mL for coffee in order.coffees]
        [250, 180, 100]
        """
        self.coffees.sort(reverse=reverse, key=lambda coffee: coffee.capacity_in_mL)


if __name__ == "__main__":
    doctest.testmod(verbose=False, extraglobs={"order": CoffeeManager()})
