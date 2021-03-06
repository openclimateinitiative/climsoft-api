from pydantic import BaseModel, Field, constr
import datetime
from climsoft_api.api.schema import Response
from typing import Optional, List


field_mapping = {
    "stationId": "station_id",
    "entryDatetime": "entry_datetime",
    "Val_Elem106": "val_elem106",
    "Val_Elem107": "val_elem107",
    "Val_Elem400": "val_elem400",
    "Val_Elem814": "val_elem814",
    "Val_Elem399": "val_elem399",
    "Val_Elem301": "val_elem301",
    "Val_Elem185": "val_elem185",
    "Val_Elem101": "val_elem101",
    "Val_Elem102": "val_elem102",
    "Val_Elem103": "val_elem103",
    "Val_Elem105": "val_elem105",
    "Val_Elem192": "val_elem192",
    "Val_Elem110": "val_elem110",
    "Val_Elem114": "val_elem114",
    "Val_Elem112": "val_elem112",
    "Val_Elem111": "val_elem111",
    "Val_Elem167": "val_elem167",
    "Val_Elem197": "val_elem197",
    "Val_Elem193": "val_elem193",
    "Val_Elem115": "val_elem115",
    "Val_Elem168": "val_elem168",
    "Val_Elem169": "val_elem169",
    "Val_Elem170": "val_elem170",
    "Val_Elem171": "val_elem171",
    "Val_Elem119": "val_elem119",
    "Val_Elem116": "val_elem116",
    "Val_Elem117": "val_elem117",
    "Val_Elem118": "val_elem118",
    "Val_Elem123": "val_elem123",
    "Val_Elem120": "val_elem120",
    "Val_Elem121": "val_elem121",
    "Val_Elem122": "val_elem122",
    "Val_Elem127": "val_elem127",
    "Val_Elem124": "val_elem124",
    "Val_Elem125": "val_elem125",
    "Val_Elem126": "val_elem126",
    "Val_Elem131": "val_elem131",
    "Val_Elem128": "val_elem128",
    "Val_Elem129": "val_elem129",
    "Val_Elem130": "val_elem130",
    "Val_Elem002": "val_elem002",
    "Val_Elem003": "val_elem003",
    "Val_Elem099": "val_elem099",
    "Val_Elem018": "val_elem018",
    "Val_Elem084": "val_elem084",
    "Val_Elem132": "val_elem132",
    "Val_Elem005": "val_elem005",
    "Val_Elem174": "val_elem174",
    "Val_Elem046": "val_elem046",
    "Flag106": "flag106",
    "Flag107": "flag107",
    "Flag400": "flag400",
    "Flag814": "flag814",
    "Flag399": "flag399",
    "Flag301": "flag301",
    "Flag185": "flag185",
    "Flag101": "flag101",
    "Flag102": "flag102",
    "Flag103": "flag103",
    "Flag105": "flag105",
    "Flag192": "flag192",
    "Flag110": "flag110",
    "Flag114": "flag114",
    "Flag112": "flag112",
    "Flag111": "flag111",
    "Flag167": "flag167",
    "Flag197": "flag197",
    "Flag193": "flag193",
    "Flag115": "flag115",
    "Flag168": "flag168",
    "Flag169": "flag169",
    "Flag170": "flag170",
    "Flag171": "flag171",
    "Flag119": "flag119",
    "Flag116": "flag116",
    "Flag117": "flag117",
    "Flag118": "flag118",
    "Flag123": "flag123",
    "Flag120": "flag120",
    "Flag121": "flag121",
    "Flag122": "flag122",
    "Flag127": "flag127",
    "Flag124": "flag124",
    "Flag125": "flag125",
    "Flag126": "flag126",
    "Flag131": "flag131",
    "Flag128": "flag128",
    "Flag129": "flag129",
    "Flag130": "flag130",
    "Flag002": "flag002",
    "Flag003": "flag003",
    "Flag099": "flag099",
    "Flag018": "flag018",
    "Flag084": "flag084",
    "Flag132": "flag132",
    "Flag005": "flag005",
    "Flag174": "flag174",
    "Flag046": "flag046",
}


class CreateFormSynoptic2Ra1(BaseModel):
    stationId: constr(max_length=50)
    yyyy: int
    mm: int
    dd: int
    hh: int
    Val_Elem106: Optional[constr(max_length=6)]
    Val_Elem107: Optional[constr(max_length=6)]
    Val_Elem400: Optional[constr(max_length=6)]
    Val_Elem814: Optional[constr(max_length=6)]
    Val_Elem399: Optional[constr(max_length=6)]
    Val_Elem301: Optional[constr(max_length=6)]
    Val_Elem185: Optional[constr(max_length=6)]
    Val_Elem101: Optional[constr(max_length=6)]
    Val_Elem102: Optional[constr(max_length=6)]
    Val_Elem103: Optional[constr(max_length=6)]
    Val_Elem105: Optional[constr(max_length=6)]
    Val_Elem192: Optional[constr(max_length=6)]
    Val_Elem110: Optional[constr(max_length=6)]
    Val_Elem114: Optional[constr(max_length=6)]
    Val_Elem112: Optional[constr(max_length=6)]
    Val_Elem111: Optional[constr(max_length=6)]
    Val_Elem167: Optional[constr(max_length=6)]
    Val_Elem197: Optional[constr(max_length=6)]
    Val_Elem193: Optional[constr(max_length=6)]
    Val_Elem115: Optional[constr(max_length=6)]
    Val_Elem168: Optional[constr(max_length=6)]
    Val_Elem169: Optional[constr(max_length=6)]
    Val_Elem170: Optional[constr(max_length=6)]
    Val_Elem171: Optional[constr(max_length=6)]
    Val_Elem119: Optional[constr(max_length=6)]
    Val_Elem116: Optional[constr(max_length=6)]
    Val_Elem117: Optional[constr(max_length=6)]
    Val_Elem118: Optional[constr(max_length=6)]
    Val_Elem123: Optional[constr(max_length=6)]
    Val_Elem120: Optional[constr(max_length=6)]
    Val_Elem121: Optional[constr(max_length=6)]
    Val_Elem122: Optional[constr(max_length=6)]
    Val_Elem127: Optional[constr(max_length=6)]
    Val_Elem124: Optional[constr(max_length=6)]
    Val_Elem125: Optional[constr(max_length=6)]
    Val_Elem126: Optional[constr(max_length=6)]
    Val_Elem131: Optional[constr(max_length=6)]
    Val_Elem128: Optional[constr(max_length=6)]
    Val_Elem129: Optional[constr(max_length=6)]
    Val_Elem130: Optional[constr(max_length=6)]
    Val_Elem002: Optional[constr(max_length=6)]
    Val_Elem003: Optional[constr(max_length=6)]
    Val_Elem099: Optional[constr(max_length=6)]
    Val_Elem018: Optional[constr(max_length=6)]
    Val_Elem084: Optional[constr(max_length=6)]
    Val_Elem132: Optional[constr(max_length=6)]
    Val_Elem005: Optional[constr(max_length=6)]
    Val_Elem174: Optional[constr(max_length=6)]
    Val_Elem046: Optional[constr(max_length=6)]
    Flag106: Optional[constr(max_length=1)]
    Flag107: Optional[constr(max_length=1)]
    Flag400: Optional[constr(max_length=1)]
    Flag814: Optional[constr(max_length=1)]
    Flag399: Optional[constr(max_length=1)]
    Flag301: Optional[constr(max_length=1)]
    Flag185: Optional[constr(max_length=1)]
    Flag101: Optional[constr(max_length=1)]
    Flag102: Optional[constr(max_length=1)]
    Flag103: Optional[constr(max_length=1)]
    Flag105: Optional[constr(max_length=1)]
    Flag192: Optional[constr(max_length=1)]
    Flag110: Optional[constr(max_length=1)]
    Flag114: Optional[constr(max_length=1)]
    Flag112: Optional[constr(max_length=1)]
    Flag111: Optional[constr(max_length=1)]
    Flag167: Optional[constr(max_length=1)]
    Flag197: Optional[constr(max_length=1)]
    Flag193: Optional[constr(max_length=1)]
    Flag115: Optional[constr(max_length=1)]
    Flag168: Optional[constr(max_length=1)]
    Flag169: Optional[constr(max_length=1)]
    Flag170: Optional[constr(max_length=1)]
    Flag171: Optional[constr(max_length=1)]
    Flag119: Optional[constr(max_length=1)]
    Flag116: Optional[constr(max_length=1)]
    Flag117: Optional[constr(max_length=1)]
    Flag118: Optional[constr(max_length=1)]
    Flag123: Optional[constr(max_length=1)]
    Flag120: Optional[constr(max_length=1)]
    Flag121: Optional[constr(max_length=1)]
    Flag122: Optional[constr(max_length=1)]
    Flag127: Optional[constr(max_length=1)]
    Flag124: Optional[constr(max_length=1)]
    Flag125: Optional[constr(max_length=1)]
    Flag126: Optional[constr(max_length=1)]
    Flag131: Optional[constr(max_length=1)]
    Flag128: Optional[constr(max_length=1)]
    Flag129: Optional[constr(max_length=1)]
    Flag130: Optional[constr(max_length=1)]
    Flag002: Optional[constr(max_length=1)]
    Flag003: Optional[constr(max_length=1)]
    Flag099: Optional[constr(max_length=1)]
    Flag018: Optional[constr(max_length=1)]
    Flag084: Optional[constr(max_length=1)]
    Flag132: Optional[constr(max_length=1)]
    Flag005: Optional[constr(max_length=1)]
    Flag174: Optional[constr(max_length=1)]
    Flag046: Optional[constr(max_length=1)]
    signature: Optional[constr(max_length=45)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping


class UpdateFormSynoptic2Ra1(BaseModel):
    Val_Elem106: Optional[constr(max_length=6)]
    Val_Elem107: Optional[constr(max_length=6)]
    Val_Elem400: Optional[constr(max_length=6)]
    Val_Elem814: Optional[constr(max_length=6)]
    Val_Elem399: Optional[constr(max_length=6)]
    Val_Elem301: Optional[constr(max_length=6)]
    Val_Elem185: Optional[constr(max_length=6)]
    Val_Elem101: Optional[constr(max_length=6)]
    Val_Elem102: Optional[constr(max_length=6)]
    Val_Elem103: Optional[constr(max_length=6)]
    Val_Elem105: Optional[constr(max_length=6)]
    Val_Elem192: Optional[constr(max_length=6)]
    Val_Elem110: Optional[constr(max_length=6)]
    Val_Elem114: Optional[constr(max_length=6)]
    Val_Elem112: Optional[constr(max_length=6)]
    Val_Elem111: Optional[constr(max_length=6)]
    Val_Elem167: Optional[constr(max_length=6)]
    Val_Elem197: Optional[constr(max_length=6)]
    Val_Elem193: Optional[constr(max_length=6)]
    Val_Elem115: Optional[constr(max_length=6)]
    Val_Elem168: Optional[constr(max_length=6)]
    Val_Elem169: Optional[constr(max_length=6)]
    Val_Elem170: Optional[constr(max_length=6)]
    Val_Elem171: Optional[constr(max_length=6)]
    Val_Elem119: Optional[constr(max_length=6)]
    Val_Elem116: Optional[constr(max_length=6)]
    Val_Elem117: Optional[constr(max_length=6)]
    Val_Elem118: Optional[constr(max_length=6)]
    Val_Elem123: Optional[constr(max_length=6)]
    Val_Elem120: Optional[constr(max_length=6)]
    Val_Elem121: Optional[constr(max_length=6)]
    Val_Elem122: Optional[constr(max_length=6)]
    Val_Elem127: Optional[constr(max_length=6)]
    Val_Elem124: Optional[constr(max_length=6)]
    Val_Elem125: Optional[constr(max_length=6)]
    Val_Elem126: Optional[constr(max_length=6)]
    Val_Elem131: Optional[constr(max_length=6)]
    Val_Elem128: Optional[constr(max_length=6)]
    Val_Elem129: Optional[constr(max_length=6)]
    Val_Elem130: Optional[constr(max_length=6)]
    Val_Elem002: Optional[constr(max_length=6)]
    Val_Elem003: Optional[constr(max_length=6)]
    Val_Elem099: Optional[constr(max_length=6)]
    Val_Elem018: Optional[constr(max_length=6)]
    Val_Elem084: Optional[constr(max_length=6)]
    Val_Elem132: Optional[constr(max_length=6)]
    Val_Elem005: Optional[constr(max_length=6)]
    Val_Elem174: Optional[constr(max_length=6)]
    Val_Elem046: Optional[constr(max_length=6)]
    Flag106: Optional[constr(max_length=1)]
    Flag107: Optional[constr(max_length=1)]
    Flag400: Optional[constr(max_length=1)]
    Flag814: Optional[constr(max_length=1)]
    Flag399: Optional[constr(max_length=1)]
    Flag301: Optional[constr(max_length=1)]
    Flag185: Optional[constr(max_length=1)]
    Flag101: Optional[constr(max_length=1)]
    Flag102: Optional[constr(max_length=1)]
    Flag103: Optional[constr(max_length=1)]
    Flag105: Optional[constr(max_length=1)]
    Flag192: Optional[constr(max_length=1)]
    Flag110: Optional[constr(max_length=1)]
    Flag114: Optional[constr(max_length=1)]
    Flag112: Optional[constr(max_length=1)]
    Flag111: Optional[constr(max_length=1)]
    Flag167: Optional[constr(max_length=1)]
    Flag197: Optional[constr(max_length=1)]
    Flag193: Optional[constr(max_length=1)]
    Flag115: Optional[constr(max_length=1)]
    Flag168: Optional[constr(max_length=1)]
    Flag169: Optional[constr(max_length=1)]
    Flag170: Optional[constr(max_length=1)]
    Flag171: Optional[constr(max_length=1)]
    Flag119: Optional[constr(max_length=1)]
    Flag116: Optional[constr(max_length=1)]
    Flag117: Optional[constr(max_length=1)]
    Flag118: Optional[constr(max_length=1)]
    Flag123: Optional[constr(max_length=1)]
    Flag120: Optional[constr(max_length=1)]
    Flag121: Optional[constr(max_length=1)]
    Flag122: Optional[constr(max_length=1)]
    Flag127: Optional[constr(max_length=1)]
    Flag124: Optional[constr(max_length=1)]
    Flag125: Optional[constr(max_length=1)]
    Flag126: Optional[constr(max_length=1)]
    Flag131: Optional[constr(max_length=1)]
    Flag128: Optional[constr(max_length=1)]
    Flag129: Optional[constr(max_length=1)]
    Flag130: Optional[constr(max_length=1)]
    Flag002: Optional[constr(max_length=1)]
    Flag003: Optional[constr(max_length=1)]
    Flag099: Optional[constr(max_length=1)]
    Flag018: Optional[constr(max_length=1)]
    Flag084: Optional[constr(max_length=1)]
    Flag132: Optional[constr(max_length=1)]
    Flag005: Optional[constr(max_length=1)]
    Flag174: Optional[constr(max_length=1)]
    Flag046: Optional[constr(max_length=1)]
    signature: Optional[constr(max_length=45)]
    entryDatetime: Optional[datetime.datetime]

    class Config:
        allow_population_by_field_name = True
        fields = field_mapping


class FormSynoptic2Ra1(CreateFormSynoptic2Ra1):
    class Config:
        allow_population_by_field_name = True
        fields = field_mapping
        orm_mode = True


class FormSynoptic2Ra1Response(Response):
    result: List[FormSynoptic2Ra1] = Field(title="Result")


class FormSynoptic2Ra1QueryResponse(FormSynoptic2Ra1Response):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
