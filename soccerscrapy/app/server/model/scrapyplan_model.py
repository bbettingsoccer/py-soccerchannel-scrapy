from typing import Optional
from pydantic import BaseModel, Field, constr, conint, create_model
from typing import (List)

class ScrapyplanModel(BaseModel):
    scrapy: constr(strict=True) = Field(...)
    championship: constr(strict=True) = Field(...)
    country: constr(strict=True) = Field(...)
    timezones: constr(strict=True) = Field(...)
    domain: constr(strict=True) = Field(...)
    url: constr(strict=True) = Field(...)
    datetime_start: constr(strict=True) = Field(...)
    datetime_end: constr(strict=True) = Field(...)
    collection: constr(strict=True) = Field(...)
    status: constr(strict=True) = Field(...)

    class config:
        scrapy = "scrapy"
        championship = "championship"
        country = "country"
        timezones = "timezones"
        domain = "domain"
        url = "url"
        datetime_start = "datetime_start"
        datetime_end = "datetime_end"
        collection = "collection_name"
        status = "status"

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        OptionalModel = create_model(
            f"Optional{cls.__name__}",
            __base__=ScrapyplanModel,
            **{
                k: (v.annotation, None) for k, v in ScrapyplanModel.model_fields.items()
            })
        return OptionalModel

    def ResponseModel(data, message):
        return {
            "data": [data],
            "code": 200,
            "message": message,
        }

    def ErrorResponseModel(error, code, message):
        return {"error": error, "code": code, "message": message}

    @staticmethod
    def data_helper(data) -> dict:
        return {
            "_id": str(data['_id']),
            "scrapy": str(data["scrapy"]),
            "championship":  str(data["championship"]),
            "country": str(data["country"]),
            "timezones": str(data["timezones"]),
            "domain": str(data["domain"]),
            "url": str(data["url"]),
            "datetime_start": str(data["datetime_start"]),
            "datetime_end": str(data["datetime_end"]),
            "collection": str(data["collection"]),
            "status": str(data["status"]),
        }
