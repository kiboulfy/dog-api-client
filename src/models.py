from pydantic import BaseModel, HttpUrl


class Weight(BaseModel):
    min: int
    max: int


class Life(BaseModel):
    min: int
    max: int


class Attributes(BaseModel):
    name: str
    description: str
    hypoallergenic: bool
    life: Life
    male_weight: Weight
    female_weight: Weight


class Data(BaseModel):
    id: str
    type: str
    attributes: Attributes


class Pagination(BaseModel):
    current: int
    records: int


class Meta(BaseModel):
    pagination: Pagination


class Links(BaseModel):
    self: HttpUrl
    current: HttpUrl | None = None
    next: HttpUrl | None = None
    last: HttpUrl | None = None


class BreedModel(BaseModel):
    data: Data
    meta: Meta | None = None
    links: Links


class BreedModelList(BaseModel):
    data: list[Data]
    meta: Meta | None = None
    links: Links


class RelationshipsInfo(BaseModel):
    id: str
    type: str


class DataForRelationships(BaseModel):
    data: list[RelationshipsInfo]


class Relationships(BaseModel):
    breeds: DataForRelationships


class DataGroupOrFacts(BaseModel):
    id: str
    type: str
    attributes: dict[str, str]
    relationships: Relationships | None = None


class Facts(BaseModel):
    data: list[DataGroupOrFacts]


class Group(BaseModel):
    data: DataGroupOrFacts
    links: Links


class Groups(BaseModel):
    data: list[DataGroupOrFacts]
    links: Links
