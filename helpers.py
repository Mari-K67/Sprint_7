import random
import string

def generate_random_string_EN(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


#универсальный метод для создания body для запросов про курьера 
def create_courier_payload(**fields):
    payload = {}

    if "login" in fields:
        payload["login"] = fields["login"] if fields["login"] is not None else generate_random_string_EN()
    if "password" in fields:
        payload["password"] = fields["password"] if fields["password"] is not None else generate_random_string_EN()
    if "firstName" in fields:
        payload["firstName"] = fields["firstName"] if fields["firstName"] is not None else generate_random_string_EN()

    return payload

#универсальный метод для создания body для заказа 
def create_oder_payload(color): 
    payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": color
    }

    return payload