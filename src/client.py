from httpx import Client
from models import BreedModelList


class DogApiClient:
    def __init__(self, base_url: str = "https://dogapi.dog/api/v2") -> None:
        self.base_url = base_url
        self.client = Client()

    def get_breeds(self) -> BreedModelList:
        response = self.client.get(f"{self.base_url}/breeds")
        return BreedModelList.model_validate(response.json())


client = DogApiClient()
print(client.get_breeds())
