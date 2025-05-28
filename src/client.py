from exceptions import WrongDataError
from http_error_handler import dogapi_error_handler
from httpx import Client, HTTPStatusError
from models import BreedModel, BreedModelList, Facts, Group, Groups
from pydantic_settings import BaseSettings, SettingsConfigDict


class DogApiClientSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    base_url: str = ""


class DogApiClient:
    def __init__(self) -> None:
        self.settings = DogApiClientSettings()
        self.client = Client(base_url=self.settings.base_url)

    def get_breeds(self) -> BreedModelList:
        try:
            response = self.client.get("/breeds")
            response.raise_for_status()
        except HTTPStatusError as e:
            return dogapi_error_handler(e)
        return BreedModelList.model_validate_json(response.content)

    def get_breed(self, uid: str) -> BreedModel:
        if isinstance(uid, str):
            try:
                response = self.client.get(f"/breeds/{uid}")
                response.raise_for_status()
            except HTTPStatusError as e:
                return dogapi_error_handler(e)
            return BreedModel.model_validate_json(response.content)
        return WrongDataError()

    def get_facts(self, limit: int | None = None) -> Facts:
        if isinstance(limit, int | None):
            if not limit:
                response = self.client.get("/facts")
            else:
                response = self.client.get("/facts", params={"limit": limit})
            try:
                response.raise_for_status()
            except HTTPStatusError as e:
                return dogapi_error_handler(e)
            return Facts.model_validate_json(response.content)
        return WrongDataError()

    def get_groups(self) -> Groups:
        try:
            response = self.client.get("/groups")
            response.raise_for_status()
        except HTTPStatusError as e:
            return dogapi_error_handler(e)
        return Groups.model_validate_json(response.content)

    def get_group(self, uid: str) -> Group:
        if isinstance(uid, str):
            try:
                response = self.client.get(f"/groups/{uid}")
                response.raise_for_status()
            except HTTPStatusError as e:
                return dogapi_error_handler(e)
            return Group.model_validate_json(response.content)
        return WrongDataError()
