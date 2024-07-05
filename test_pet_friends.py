import os.path

from api import PetFriends
from settings import valid_email, valid_password, name, animal_type, age, pet_photo, email_invalid, password_invalid, \
    name_very_long, name_space, dog_photo, dog_photo_gif, pet_txt, valid_email_1, valid_password_1

pf = PetFriends()

#  1. User invalid
def test_get_api_key_invalid_user(email = email_invalid, password = password_invalid):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' is not result

# 2. Password invalid, email valid
def test_get_api_key_password_invalid(email = valid_email, password = password_invalid):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' is not result

# 3. email invalid, password valid
def test_get_api_key_email_invalid(email = email_invalid, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' is not result

# 4 another users auth_key
def test_get_all_pest_with_invalid_auth_key(filter= ''):
    _, auth_key = pf.get_api_key(valid_email_1, valid_password_1)
    status = pf.get_list_of_pets(auth_key, filter)
    assert status != 200

# 5 get my pets with filter 'my pets'
def test_get_my_pets_with_valid_auth_key(filter = 'my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200


# 6 post a new pet with a very long name
def test_post_new_pet_with_very_lond_name(name = name_very_long, animal_type = animal_type, age = age, pet_photo = pet_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

# 7 post a new pet with a space in name
def test_post_new_pet_with_space_name(name = name_space, animal_type=animal_type, age = age, pet_photo = pet_photo):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status != 200
    assert result['name'] == name


# 8 post a new pet with image in the format .png
def test_post_new_pet_with_image_png(name = name, animal_type = animal_type, age = age, pet_photo = dog_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

# 9 post a new pet with image in the format .gif
def test_post_new_pet_with_image_gif(name = name, animal_type = animal_type, age = age, pet_photo = dog_photo_gif):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key,name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

# 10 post a new pet with pet_photo = txt doc
def test_post_new_pet_with_missing_photo(name = name, animal_type = animal_type, age = age, pet_photo = pet_txt):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status != 200
    assert result['name'] is not name
