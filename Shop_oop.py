Вы создаете интернет-магазин. Для этого нужно объявить два класса:

Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара.

Объекты класса Shop следует создавать командой:

shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:

goods - список товаров (изначально список пустой).

А также в классе объявить методы:

add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка goods);

Объекты класса Product следует создавать командой:

p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:

id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).

В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.). Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id. При попытке это сделать генерировать исключение:

raise AttributeError("Атрибут id удалять запрещено.")





class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []
    
    def add_product(self, product):
        self.goods.append(product)
    
    def remove_product(self, product):
        if product in self.goods:
             self.goods.remove(product)

class Product:
    _id_instance = 1
    attrs = {'name' : (str, ), 'weight' : (int, float), 'price' : (int, float)}    
    def __init__(self, name, weight, price):
            self.id = Product._id_instance 
            Product._id_instance += 1
            self.name = name
            self.weight = weight
            self.price = price
    def __setattr__(self, key, value):
            if key in self.attrs and type(value) in self.attrs[key]:
                if (key == 'price' or key == 'weight') and value <= 0:
                     raise TypeError("Неверный тип присваиваемых данных.")
            elif key in self.attrs:
                 raise TypeError("Неверный тип присваиваемых данных.")

            object.__setattr__(self, key, value)
    
    def __delattr__(self, item):
            if item == "id":
                raise AttributeError("Атрибут id удалять запрещено.") 
            object.__delattr__(self, item)

shop = Shop("Pyterochka")
game = Product("chips", 1000, 1000)
shop.add_product(game)
shop.add_product(Product("water", 1, 20))

