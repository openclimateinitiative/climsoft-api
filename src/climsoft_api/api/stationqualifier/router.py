import climsoft_api.api.stationqualifier.schema as stationqualifier_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import stationqualifier_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging
from climsoft_api.utils.exception import handle_exceptions


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get(
    "/station-qualifiers",
)
@handle_exceptions
def get_station_qualifier(
    qualifier: str = None,
    qualifier_begin_date: str = None,
    qualifier_end_date: str = None,
    station_timezone: int = None,
    station_network_type: str = None,
    belongs_to: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, station_qualifier = stationqualifier_service.query(
        db_session=db_session,
        belongs_to=belongs_to,
        qualifier=qualifier,
        qualifier_begin_date=qualifier_begin_date,
        qualifier_end_date=qualifier_end_date,
        station_timezone=station_timezone,
        station_network_type=station_network_type,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=station_qualifier,
        message=_("Successfully fetched station qualifier."),
        schema=translate_schema(
            _,
            stationqualifier_schema.StationQualifierQueryResponse.schema()
        )
    )


@router.get(
    "/station-qualifiers/{qualifier}/{qualifier_begin_date}/{qualifier_end_date}/{belongs_to}"
)
@handle_exceptions
def get_station_qualifier_by_id(
    qualifier: str,
    qualifier_begin_date: str,
    qualifier_end_date: str,
    belongs_to: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            stationqualifier_service.get(
                db_session=db_session,
                qualifier=qualifier,
                qualifier_begin_date=qualifier_begin_date,
                qualifier_end_date=qualifier_end_date,
                belongs_to=belongs_to,
            )
        ],
        message=_("Successfully fetched station qualifier."),
        schema=translate_schema(
            _,
            stationqualifier_schema.StationQualifierWithStationResponse.schema()
        )
    )


@router.post(
    "/station-qualifiers"
)
@handle_exceptions
def create_station_qualifier(
    data: stationqualifier_schema.CreateStationQualifier,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[stationqualifier_service.create(db_session=db_session,
                                                data=data)],
        message=_("Successfully created station qualifier."),
        schema=translate_schema(
            _,
            stationqualifier_schema.StationQualifierResponse.schema()
        )
    )


@router.put(
    "/station-qualifiers/{qualifier}/{qualifier_begin_date}/{qualifier_end_date}/{belongs_to}"
)
@handle_exceptions
def update_station_qualifier(
    qualifier: str,
    qualifier_begin_date: str,
    qualifier_end_date: str,
    belongs_to: str,
    data: stationqualifier_schema.UpdateStationQualifier,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            stationqualifier_service.update(
                db_session=db_session,
                qualifier=qualifier,
                qualifier_begin_date=qualifier_begin_date,
                qualifier_end_date=qualifier_end_date,
                belongs_to=belongs_to,
                updates=data,
            )
        ],
        message=_("Successfully updated station qualifier."),
        schema=translate_schema(
            _,
            stationqualifier_schema.StationQualifierResponse.schema()
        )
    )


@router.delete(
    "/station-qualifiers/{qualifier}/{qualifier_begin_date}/{qualifier_end_date}/{belongs_to}"
)
@handle_exceptions
def delete_station_qualifier(
    qualifier: str,
    qualifier_begin_date: str,
    qualifier_end_date: str,
    belongs_to: str,
    db_session: Session = Depends(deps.get_session),
):
    stationqualifier_service.delete(
        db_session=db_session,
        qualifier=qualifier,
        qualifier_begin_date=qualifier_begin_date,
        qualifier_end_date=qualifier_end_date,
        belongs_to=belongs_to,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted station qualifier."),
        schema=translate_schema(
            _,
            stationqualifier_schema.StationQualifierResponse.schema()
        )
    )
