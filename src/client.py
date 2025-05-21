from httpx import Client
from models import BreedModel, BreedModelList


class DogApiClient:
    def __init__(self, base_url: str = "https://dogapi.dog/api/v2") -> None:
        self.base_url = base_url
        self.client = Client()

    def get_breeds(self) -> BreedModelList:
        response = self.client.get(f"{self.base_url}/breeds")
        return BreedModelList.model_validate(response.json())

    def get_breed(self, id) -> BreedModel:
        self.id = id
        response = self.client.get(f"{self.base_url}/breeds/{self.id}")
        return repr(BreedModel.model_validate(response.json()))


client = DogApiClient()
print(client.get_breed("8355b9c9-3724-477d-858a-c1c1c0f1743f"))
