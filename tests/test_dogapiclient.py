import pytest

from src.client import DogApiClient


def client() -> DogApiClient:
    return DogApiClient()
