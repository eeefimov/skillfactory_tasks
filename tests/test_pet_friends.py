import os.path

import pytest
from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password

Pet = PetFriends()


def test_get_api_key_valid(email=valid_email, password=valid_password):
    """positive test. return code 200"""
    status, result = Pet.get_api_key(valid_email, valid_password)
    assert status == 200
    assert "key" in result


def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """positive"""
    status, result = Pet.get_api_key(email, password)
    assert status == 400 or 401 or 402 or 403 or 404 or 405


def test_get_api_key_invalid(email=invalid_email, password=invalid_password):
    """negative"""
    status, result = Pet.get_api_key(invalid_email, invalid_password)
    assert status == 200
    assert "key" in result


def test_get_all_pets_with_valid_key(filter=''):
    """positive test, return pets list"""
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    status, result = Pet.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0


def test_post_add_new_pet_with_valid_data(name='Doggo', animal_type='dog', age='10',
                                          pet_photo='images/corgi.jpeg'):
    """positive test add new pet"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    print(auth_key)
    status, result = Pet.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_post_add_new_pet_without_photo(name="Doggly", animal_type="dog", age=10):
    """positive"""
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    status, result = Pet.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result["name"] == name

def test_successful_delete_self_pet():
    """positive"""
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    _, my_pets = Pet.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        Pet.add_new_pet(auth_key, "Doggo", "dog", "10", "images/corgi.jpg")
        _, my_pets = Pet.get_list_of_pets(auth_key, "my_pets")
        pet_id = my_pets['pets'][0]['id']
        status, _ = Pet.delete_pet(auth_key, pet_id)
        _, my_pets = Pet.get_list_of_pets(auth_key, "my_pets")
        assert status == 200
        assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name="Dooogie", animal_type="Dog", age=10):
    """positive"""
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    _, my_pets = Pet.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = Pet.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("Wrong pets")


def test_post_add_photo_of_pet(pet_photo='images/corgi.jpeg'):
    """positive"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    _, my_pets = Pet.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = Pet.post_add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
    else:
        raise Exception("No pets")


def test_get_all_pets_with_invalid_filter(filter='not_my_pets'):
    """positive"""
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    status, result = Pet.get_list_of_pets(auth_key, filter)
    assert status == 400 or 401 or 402 or 403 or 404 or 405


def test_post_add_new_pet_with_invalid_name(name="fghfhdhds12312312312121sacsdcdsc2332332", animal_type="dog",
                                            age="1",pet_photo="images/corgi.jpeg"):
    """positive"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    status, result = Pet.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405


def test_post_add_new_pet_with_none_name(name="", animal_type="dog", age="1",
                                         pet_photo="images/corgi.jpeg"):
    """positive"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = Pet.get_api_key(valid_email, valid_password)
    status, result = Pet.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400 or 401 or 402 or 403 or 404 or 405
