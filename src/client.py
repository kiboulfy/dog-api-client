from httpx import Client
from models import BreedModel, BreedModelList, Facts, Group, Groups


class DogApiClient:
    def __init__(self, base_url: str = "https://dogapi.dog/api/v2") -> None:
        self.base_url = base_url
        self.client = Client()

    def get_breeds(self) -> BreedModelList:
        response = self.client.get(f"{self.base_url}/breeds")
        return BreedModelList.model_validate(response.json())

    def get_breed(self, id: str) -> BreedModel:
        self.id: str = id
        response = self.client.get(f"{self.base_url}/breeds/{self.id}")
        return repr(BreedModel.model_validate(response.json()))

    def get_facts(self, limit: int | None = None) -> Facts:
        if not limit:
            response = self.client.get(f"{self.base_url}/facts")
        else:
            response = self.client.get(f"{self.base_url}/facts?limit={limit}")
        return Facts.model_validate(response.json())

    def get_groups(self) -> Groups:
        response = self.client.get(f"{self.base_url}/groups")
        return Groups.model_validate(response.json())

    def get_group(self, id: str) -> Group:
        self.id: str = id
        response = self.client.get(f"{self.base_url}/groups/{self.id}")
        return Group.model_validate(response.json())


client = DogApiClient()

# print(client.get_breeds() #test get_breeds
# print(client.get_breed("8355b9c9-3724-477d-858a-c1c1c0f1743f")) #test get_breed
# print(client.get_facts(2)) #test get_facts
# print(client.get_groups())  # test get_groups
print(client.get_group("8000793f-a1ae-4ec4-8d55-ef83f1f644e5"))
