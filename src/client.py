from httpx import Client
from pydantic import UUID4

from .models import BreedModel, BreedModelList, Facts, Group, Groups


class DogApiClient:
    def __init__(self) -> None:
        self.client = Client(base_url="https://dogapi.dog/api/v2")

    def get_breeds(self) -> BreedModelList:
        response = self.client.get("/breeds")
        return BreedModelList.model_validate_json(response.content)

    def get_breed(self, id: UUID4) -> BreedModel:
        response = self.client.get(f"/breeds/{id}")
        return BreedModel.model_validate_json(response.content)

    def get_facts(self, limit: int | None = None) -> Facts:
        if not limit:
            response = self.client.get("/facts")
        else:
            response = self.client.get("/facts", params={"limit": limit})
        return Facts.model_validate_json(response.content)

    def get_groups(self) -> Groups:
        response = self.client.get("/groups")
        return Groups.model_validate_json(response.content)

    def get_group(self, id: UUID4) -> Group:
        response = self.client.get(f"/groups/{id}")
        return Group.model_validate_json(response.content)


client = DogApiClient()
