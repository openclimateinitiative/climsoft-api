from pydantic import BaseModel, constr, Field, validator
from typing import Optional, List, Any
from climsoft_api.api.schema import Response

field_mapping = {
    "stationId": "station_id",
    "elementId": "element_id",
    "entryDatetime": "entry_datetime",
    "temperatureUnits": "temperature_units",
    "precipUnits": "precip_units",
    "cloudHeightUnits": "cloud_height_units",
    "visUnits": "vis_units"
}


class CreateFormDaily2(BaseModel):
    stationId: constr(max_length=50)
    elementId: int
    yyyy: int
    mm: int
    hh: int
    day01: Optional[constr(max_length=45)]
    day02: Optional[constr(max_length=45)]
    day03: Optional[constr(max_length=45)]
    day04: Optional[constr(max_length=45)]
    day05: Optional[constr(max_length=45)]
    day06: Optional[constr(max_length=45)]
    day07: Optional[constr(max_length=45)]
    day08: Optional[constr(max_length=45)]
    day09: Optional[constr(max_length=45)]
    day10: Optional[constr(max_length=45)]
    day11: Optional[constr(max_length=45)]
    day12: Optional[constr(max_length=45)]
    day13: Optional[constr(max_length=45)]
    day14: Optional[constr(max_length=45)]
    day15: Optional[constr(max_length=45)]
    day16: Optional[constr(max_length=45)]
    day17: Optional[constr(max_length=45)]
    day18: Optional[constr(max_length=45)]
    day19: Optional[constr(max_length=45)]
    day20: Optional[constr(max_length=45)]
    day21: Optional[constr(max_length=45)]
    day22: Optional[constr(max_length=45)]
    day23: Optional[constr(max_length=45)]
    day24: Optional[constr(max_length=45)]
    day25: Optional[constr(max_length=45)]
    day26: Optional[constr(max_length=45)]
    day27: Optional[constr(max_length=45)]
    day28: Optional[constr(max_length=45)]
    day29: Optional[constr(max_length=45)]
    day30: Optional[constr(max_length=45)]
    day31: Optional[constr(max_length=45)]
    flag01: Optional[constr(max_length=1)]
    flag02: Optional[constr(max_length=1)]
    flag03: Optional[constr(max_length=1)]
    flag04: Optional[constr(max_length=1)]
    flag05: Optional[constr(max_length=1)]
    flag06: Optional[constr(max_length=1)]
    flag07: Optional[constr(max_length=1)]
    flag08: Optional[constr(max_length=1)]
    flag09: Optional[constr(max_length=1)]
    flag10: Optional[constr(max_length=1)]
    flag11: Optional[constr(max_length=1)]
    flag12: Optional[constr(max_length=1)]
    flag13: Optional[constr(max_length=1)]
    flag14: Optional[constr(max_length=1)]
    flag15: Optional[constr(max_length=1)]
    flag16: Optional[constr(max_length=1)]
    flag17: Optional[constr(max_length=1)]
    flag18: Optional[constr(max_length=1)]
    flag19: Optional[constr(max_length=1)]
    flag20: Optional[constr(max_length=1)]
    flag21: Optional[constr(max_length=1)]
    flag22: Optional[constr(max_length=1)]
    flag23: Optional[constr(max_length=1)]
    flag24: Optional[constr(max_length=1)]
    flag25: Optional[constr(max_length=1)]
    flag26: Optional[constr(max_length=1)]
    flag27: Optional[constr(max_length=1)]
    flag28: Optional[constr(max_length=1)]
    flag29: Optional[constr(max_length=1)]
    flag30: Optional[constr(max_length=1)]
    flag31: Optional[constr(max_length=1)]
    period01: Optional[constr(max_length=45)]
    period02: Optional[constr(max_length=45)]
    period03: Optional[constr(max_length=45)]
    period04: Optional[constr(max_length=45)]
    period05: Optional[constr(max_length=45)]
    period06: Optional[constr(max_length=45)]
    period07: Optional[constr(max_length=45)]
    period08: Optional[constr(max_length=45)]
    period09: Optional[constr(max_length=45)]
    period10: Optional[constr(max_length=45)]
    period11: Optional[constr(max_length=45)]
    period12: Optional[constr(max_length=45)]
    period13: Optional[constr(max_length=45)]
    period14: Optional[constr(max_length=45)]
    period15: Optional[constr(max_length=45)]
    period16: Optional[constr(max_length=45)]
    period17: Optional[constr(max_length=45)]
    period18: Optional[constr(max_length=45)]
    period19: Optional[constr(max_length=45)]
    period20: Optional[constr(max_length=45)]
    period21: Optional[constr(max_length=45)]
    period22: Optional[constr(max_length=45)]
    period23: Optional[constr(max_length=45)]
    period24: Optional[constr(max_length=45)]
    period25: Optional[constr(max_length=45)]
    period26: Optional[constr(max_length=45)]
    period27: Optional[constr(max_length=45)]
    period28: Optional[constr(max_length=45)]
    period29: Optional[constr(max_length=45)]
    period30: Optional[constr(max_length=45)]
    period31: Optional[constr(max_length=45)]
    total: Optional[constr(max_length=45)]
    signature: Optional[constr(max_length=45)]
    entryDatetime: Optional[constr(max_length=45)]
    temperatureUnits: Optional[constr(max_length=45)]
    precipUnits: Optional[constr(max_length=45)]
    cloudHeightUnits: Optional[constr(max_length=45)]
    visUnits: Optional[constr(max_length=45)]

    @validator("entryDatetime", pre=True)
    def validate_time(cls, value: Any) -> Any:
        return str(value)

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping


class UpdateFormDaily2(BaseModel):
    day01: Optional[constr(max_length=45)]
    day02: Optional[constr(max_length=45)]
    day03: Optional[constr(max_length=45)]
    day04: Optional[constr(max_length=45)]
    day05: Optional[constr(max_length=45)]
    day06: Optional[constr(max_length=45)]
    day07: Optional[constr(max_length=45)]
    day08: Optional[constr(max_length=45)]
    day09: Optional[constr(max_length=45)]
    day10: Optional[constr(max_length=45)]
    day11: Optional[constr(max_length=45)]
    day12: Optional[constr(max_length=45)]
    day13: Optional[constr(max_length=45)]
    day14: Optional[constr(max_length=45)]
    day15: Optional[constr(max_length=45)]
    day16: Optional[constr(max_length=45)]
    day17: Optional[constr(max_length=45)]
    day18: Optional[constr(max_length=45)]
    day19: Optional[constr(max_length=45)]
    day20: Optional[constr(max_length=45)]
    day21: Optional[constr(max_length=45)]
    day22: Optional[constr(max_length=45)]
    day23: Optional[constr(max_length=45)]
    day24: Optional[constr(max_length=45)]
    day25: Optional[constr(max_length=45)]
    day26: Optional[constr(max_length=45)]
    day27: Optional[constr(max_length=45)]
    day28: Optional[constr(max_length=45)]
    day29: Optional[constr(max_length=45)]
    day30: Optional[constr(max_length=45)]
    day31: Optional[constr(max_length=45)]
    flag01: Optional[constr(max_length=1)]
    flag02: Optional[constr(max_length=1)]
    flag03: Optional[constr(max_length=1)]
    flag04: Optional[constr(max_length=1)]
    flag05: Optional[constr(max_length=1)]
    flag06: Optional[constr(max_length=1)]
    flag07: Optional[constr(max_length=1)]
    flag08: Optional[constr(max_length=1)]
    flag09: Optional[constr(max_length=1)]
    flag10: Optional[constr(max_length=1)]
    flag11: Optional[constr(max_length=1)]
    flag12: Optional[constr(max_length=1)]
    flag13: Optional[constr(max_length=1)]
    flag14: Optional[constr(max_length=1)]
    flag15: Optional[constr(max_length=1)]
    flag16: Optional[constr(max_length=1)]
    flag17: Optional[constr(max_length=1)]
    flag18: Optional[constr(max_length=1)]
    flag19: Optional[constr(max_length=1)]
    flag20: Optional[constr(max_length=1)]
    flag21: Optional[constr(max_length=1)]
    flag22: Optional[constr(max_length=1)]
    flag23: Optional[constr(max_length=1)]
    flag24: Optional[constr(max_length=1)]
    flag25: Optional[constr(max_length=1)]
    flag26: Optional[constr(max_length=1)]
    flag27: Optional[constr(max_length=1)]
    flag28: Optional[constr(max_length=1)]
    flag29: Optional[constr(max_length=1)]
    flag30: Optional[constr(max_length=1)]
    flag31: Optional[constr(max_length=1)]
    period01: Optional[constr(max_length=45)]
    period02: Optional[constr(max_length=45)]
    period03: Optional[constr(max_length=45)]
    period04: Optional[constr(max_length=45)]
    period05: Optional[constr(max_length=45)]
    period06: Optional[constr(max_length=45)]
    period07: Optional[constr(max_length=45)]
    period08: Optional[constr(max_length=45)]
    period09: Optional[constr(max_length=45)]
    period10: Optional[constr(max_length=45)]
    period11: Optional[constr(max_length=45)]
    period12: Optional[constr(max_length=45)]
    period13: Optional[constr(max_length=45)]
    period14: Optional[constr(max_length=45)]
    period15: Optional[constr(max_length=45)]
    period16: Optional[constr(max_length=45)]
    period17: Optional[constr(max_length=45)]
    period18: Optional[constr(max_length=45)]
    period19: Optional[constr(max_length=45)]
    period20: Optional[constr(max_length=45)]
    period21: Optional[constr(max_length=45)]
    period22: Optional[constr(max_length=45)]
    period23: Optional[constr(max_length=45)]
    period24: Optional[constr(max_length=45)]
    period25: Optional[constr(max_length=45)]
    period26: Optional[constr(max_length=45)]
    period27: Optional[constr(max_length=45)]
    period28: Optional[constr(max_length=45)]
    period29: Optional[constr(max_length=45)]
    period30: Optional[constr(max_length=45)]
    period31: Optional[constr(max_length=45)]
    total: Optional[constr(max_length=45)]
    signature: Optional[constr(max_length=45)]
    entryDatetime: Optional[constr(max_length=45)]
    temperatureUnits: Optional[constr(max_length=45)]
    precipUnits: Optional[constr(max_length=45)]
    cloudHeightUnits: Optional[constr(max_length=45)]
    visUnits: Optional[constr(max_length=45)]

    @validator("entryDatetime", pre=True)
    def validate_time(cls, value: Any) -> Any:
        return str(value)

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping


class FormDaily2(CreateFormDaily2):

    @validator("entryDatetime", pre=True)
    def validate_time(cls, value: Any) -> Any:
        return str(value)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = field_mapping


class FormDaily2Response(Response):
    result: List[FormDaily2] = Field(title="Result")


class FormDaily2QueryResponse(FormDaily2Response):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
