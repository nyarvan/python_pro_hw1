class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}\nЦена: {self.price}\nОписание: {self.description}, Габариты: {self.dimensions}\n"


class Client:
    def __init__(self, surname, name, patronymic, phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone


class Order:

    def __init__(self, client, product):
        self.info_about_client = {"surname": client.surname, "name": client.name, "patronymic": client.patronymic,
                                  "phone": client.phone}
        self.info_about_product = {
            f"{product.name}": {"Название": product.name, "Цена": product.price, "Описание": product.description,
                                "Габариты": product.dimensions}}

    def push_product(self, product):
        product_name = product.name
        self.info_about_product[product_name] = {"Название": product.name, "Цена": product.price,
                                                 "Описание": product.description, "Габариты": product.dimensions}

    def __total_cost(self):
        total_cost = 0
        for item in self.info_about_product:
            total_cost += self.info_about_product[item]["Цена"]
        return total_cost

    def __str__(self):
        products = ""
        for item in self.info_about_product:
            for element in self.info_about_product[item]:
                products += f"{element}: {self.info_about_product[item][element]}\n"
        return "Покупатель {0} {1}.{2} (тел. {3}):\n{4}Суммарная стоимость: {5}".format(self.info_about_client["surname"],
                                                                                        self.info_about_client["name"][0],
                                                                                        self.info_about_client["patronymic"][0],
                                                                                        self.info_about_client["phone"],
                                                                                        products, self.__total_cost())

if __name__ == '__main__':
        iphone12 = Product("Iphone 12", 26000, "Смартфон от компании Apple", "Масса: 164 грамм, Размеры: 146,7х71,5х7,4 мм")
        watch = Product("Apple Watch Series 6", 11500, "Смарт-часы от компании Apple",
                        "Масса: 48 г, Размеры: 44×38×10,7 мм")
        airpods_pro = Product("Apple AirPods Pro", 7500, "Безпроводные наушники от компании Apple",
                              "Масса: 45,6 г, Размеры: 60,6 x 45,2 x 21,7 мм")

        rybak_ivan = Client("Рыбак", "Иван", "Андреевич", "+380667899504")
        order1 = Order(rybak_ivan, iphone12)
        order1.push_product(watch)
        print(order1)

        print("\nВведите свою фамилию, имя, отчество и номер телефона:")
        surname = input("Фамилия: ")
        name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone = input("Номер телефона: ")
        client2 = Client(surname, name, patronymic, phone)
        print("\nКаталог:")
        print(iphone12)
        print(watch)
        print(airpods_pro)

        print("\nВыберите товар из каталога")
        product = input("Название товара: ")
        if product == "Iphone 12":
            order2 = Order(client2, iphone12)
        elif product == "Apple Watch Series 6":
            order2 = Order(client2, watch)
        elif product == "Apple AirPods Pro":
            order2 = Order(client2, airpods_pro)
        else:
            print("Проверьте введенное название товара")

        print("Добавить товар в каталог (введите название товара либо напишите Нет)")
        product = input("Название товара: ")
        if product == "Iphone 12":
            order2.push_product(iphone12)
        elif product == "Apple Watch Series 6":
            order2.push_product(watch)
        elif product == "Apple AirPods Pro":
            order2.push_product(airpods_pro)

        print("\nВаша корзина:")
        print(order2)