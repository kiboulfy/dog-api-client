from src.client import DogApiClient

client = DogApiClient()

# print(client.get_breeds())  # test get_breeds
# print(client.get_breed("8355b9c9-3724-477d-858a-c1c1c0f1743f"))  # test get_breed
# print(client.get_facts(2))  # test get_facts
# print(client.get_groups())  # test get_groups
print(client.get_group("8000793f-a1ae-4ec4-8d55-ef83f1f644e5"))  # test get_groop


def test_get_group() -> None:
    print(client.get_group("8000793f-a1ae-4ec4-8d55-ef83f1f644e5"))


test_get_group()
