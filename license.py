from licensing.models import *
from licensing.methods import Key, Helpers

def create_key(token, product_id):
    # Create a Cryptolense object
    cryptolens_object = cryptolens.Cryptolens()

    # Authenticate with your access tokenpip install cryptolens
    cryptolens_object.access_token = token

    # Create a key for the specified product
    result = cryptolens_object.key.create_key(product_id=product_id, period=30, f1=True)

    # Check if the key was created successfully
    if result[0]:
        print("Key created successfully:", result[1].key)
    else:
        print("Failed to create key:", result[1])

# Replace with your access token and product ID
access_token = "WyI1NjM3ODAzMCIsIkp3MGo3MkFROVBKVUt0amRET1hzT1F4cFNBcEIzaHNhaEtEM3plVHEiXQ== "
product_id = 1234

create_key(access_token, product_id)