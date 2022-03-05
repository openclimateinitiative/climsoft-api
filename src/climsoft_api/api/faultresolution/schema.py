import datetime
from typing import List

import \
    climsoft_api.api.instrumentfaultreport.schema as instrumentfaultreport_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateFaultResolution(BaseSchema):
    resolvedDatetime: constr(max_length=50)
    associatedWith: constr(max_length=255)
    resolvedBy: constr(max_length=255)
    remarks: constr(max_length=255)

    class Config:
        fields = {
            "resolvedDatetime": "resolved_datetime",
            "associatedWith": "associated_with",
            "resolvedBy": "resolved_by"
        }


class UpdateFaultResolution(BaseSchema):
    resolvedBy: constr(max_length=255)
    remarks: constr(max_length=255)

    class Config:
        fields = {
            "resolvedBy": "resolved_by"
        }


class FaultResolution(CreateFaultResolution):
    resolvedDatetime = datetime.datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "resolvedDatetime": "resolved_datetime",
            "associatedWith": "associated_with",
            "resolvedBy": "resolved_by"
        }


class FaultResolutionWithInstrumentFaultReport(FaultResolution):
    instrumentfaultreport: instrumentfaultreport_schema.InstrumentFaultReport


class FaultResolutionResponse(Response):
    result: List[FaultResolution] = Field(title=_("Result"))


class FaultResolutionWithInstrumentFaultReportResponse(Response):
    result: List[FaultResolutionWithInstrumentFaultReport] = Field(title=_("Result"))


class FaultResolutionQueryResponse(FaultResolutionResponse):
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
