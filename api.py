import json.decoder
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = {
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')
            }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet_from_database(self, auth_key: json, pet_id: str) -> json:
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_new_pet_missing_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:

        """ Метод создает питомца в базе данных без фото """
        headers = {
            "auth_key": auth_key['key']
        }

        data = {
            "name": name,
            "animal_type": animal_type,
            "age": age
        }
        res = requests.post(self.base_url + 'api/create_pet_simple', headers= headers, data= data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_add_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:

        headers = {
           "auth_key": auth_key['key']}
        data = {
            "pet_photo": (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpeg')}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data, files=file)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
