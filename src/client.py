from httpx import Client
from pydantic_settings import BaseSettings, SettingsConfigDict

from .models import BreedModel, BreedModelList, Facts, Group, Groups


class DogApiClientSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    base_url: str = ""


class DogApiClient:
    def __init__(self) -> None:
        self.settings = DogApiClientSettings()
        self.client = Client(base_url=self.settings.base_url)

    def get_breeds(self) -> BreedModelList:
        response = self.client.get("/breeds")
        return BreedModelList.model_validate_json(response.content)

    def get_breed(self, uid: str) -> BreedModel:
        response = self.client.get(f"/breeds/{uid}")
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

    def get_group(self, uid: str) -> Group:
        response = self.client.get(f"/groups/{uid}")
        return Group.model_validate_json(response.content)


client = DogApiClient()
