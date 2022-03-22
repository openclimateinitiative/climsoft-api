import climsoft_api.api.instrument.schema as instrument_schema
from climsoft_api.api import deps
from climsoft_api.services import instrument_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema


router = APIRouter()


@router.get("/")
def get_instruments(
    instrument_id: str = None,
    instrument_name: str = None,
    serial_number: str = None,
    abbreviation: str = None,
    model: str = None,
    manufacturer: str = None,
    instrument_uncertainty: float = None,
    installation_datetime: str = None,
    uninstallation_datetime: str = None,
    height: str = None,
    station_id: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, instruments = instrument_service.query(
            db_session=db_session,
            instrument_id=instrument_id,
            instrument_name=instrument_name,
            serial_number=serial_number,
            abbreviation=abbreviation,
            model=model,
            manufacturer=manufacturer,
            instrument_uncertainty=instrument_uncertainty,
            installation_datetime=installation_datetime,
            uninstallation_datetime=uninstallation_datetime,
            height=height,
            station_id=station_id,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=instruments,
            message=_("Successfully fetched instruments."),
            schema=translate_schema(
                _,
                instrument_schema.InstrumentQueryResponse.schema()
            )
        )
    except instrument_service.FailedGettingInstrumentList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{instrument_id}"
)
def get_instrument_by_id(
    instrument_id: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                instrument_service.get(
                    db_session=db_session, instrument_id=instrument_id
                )
            ],
            message=_("Successfully fetched instrument."),
            schema=translate_schema(
                _,
                instrument_schema.InstrumentWithStationResponse.schema()
            )
        )
    except instrument_service.FailedGettingInstrument as e:
        return get_error_response(message=str(e))


@router.post("/")
def create_instrument(
    data: instrument_schema.CreateInstrument,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[instrument_service.create(
                db_session=db_session,
                data=data
            )],
            message=_("Successfully created instrument."),
            schema=translate_schema(
                _,
                instrument_schema.InstrumentResponse.schema()
            )
        )
    except instrument_service.FailedCreatingInstrument as e:
        return get_error_response(message=str(e))


@router.put(
    "/{instrument_id}"
)
def update_instrument(
    instrument_id: str,
    data: instrument_schema.UpdateInstrument,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                instrument_service.update(
                    db_session=db_session,
                    instrument_id=instrument_id,
                    updates=data
                )
            ],
            message=_("Successfully updated instrument."),
            schema=translate_schema(
                _,
                instrument_schema.InstrumentResponse.schema()
            )
        )
    except instrument_service.FailedUpdatingInstrument as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{instrument_id}"
)
def delete_instrument(
    instrument_id: str, db_session: Session = Depends(deps.get_session)
):
    try:
        instrument_service.delete(
            db_session=db_session,
            instrument_id=instrument_id
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted instrument."),
            schema=translate_schema(
                _,
                instrument_schema.InstrumentResponse.schema()
            )
        )
    except instrument_service.FailedDeletingInstrument as e:
        return get_error_response(message=str(e))
