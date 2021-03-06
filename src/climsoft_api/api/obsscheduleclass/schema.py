from typing import List

import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateObsScheduleClass(BaseSchema):
    scheduleClass: constr(max_length=255) = Field(title="Schedule Class")
    description: constr(max_length=255) = Field(title="Description")
    refersTo: constr(max_length=255) = Field(title="Refers To")

    class Config:
        fields = {
            "scheduleClass": "schedule_class",
            "refersTo": "refers_to"
        }


class UpdateObsScheduleClass(BaseSchema):
    description: constr(max_length=255) = Field(title="Description")
    refersTo: constr(max_length=255) = Field(title="Refers To")

    class Config:
        fields = {
            "refersTo": "refers_to"
        }


class ObsScheduleClass(CreateObsScheduleClass):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "scheduleClass": "schedule_class",
            "refersTo": "refers_to"
        }


class ObsScheduleClassResponse(Response):
    result: List[ObsScheduleClass] = Field(title="Result")


class ObsScheduleClassWithStation(ObsScheduleClass):
    station: station_schema.Station = Field(title="Station")


class ObsScheduleClassWithStationResponse(Response):
    result: List[ObsScheduleClassWithStation] = Field(title="Result")


class ObsScheduleClassQueryResponse(ObsScheduleClassResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
