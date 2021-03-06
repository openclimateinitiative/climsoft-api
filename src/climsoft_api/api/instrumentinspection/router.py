import \
    climsoft_api.api.instrumentinspection.schema as instrumentinspection_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import instrumentinspection_service
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
    "/instrument-inspections",
)
@handle_exceptions
def get_instrument_inspection(
    performed_on: str = None,
    inspection_datetime: str = None,
    performed_by: str = None,
    status: str = None,
    remarks: str = None,
    performed_at: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, instrument_inspection = instrumentinspection_service.query(
        db_session=db_session,
        performed_on=performed_on,
        inspection_datetime=inspection_datetime,
        performed_by=performed_by,
        status=status,
        remarks=remarks,
        performed_at=performed_at,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=instrument_inspection,
        message=_("Successfully fetched instrument inspection."),
        schema=translate_schema(
            _,
            instrumentinspection_schema.InstrumentInspectionQueryResponse.schema()
        )
    )


@router.get(
    "/instrument-inspections/{performed_on}/{inspection_datetime}",
)
@handle_exceptions
def get_instrument_inspection_by_id(
    performed_on: str,
    inspection_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            instrumentinspection_service.get(
                db_session=db_session,
                performed_on=performed_on,
                inspection_datetime=inspection_datetime,
            )
        ],
        message=_("Successfully fetched instrument inspection."),
        schema=translate_schema(
            _,
            instrumentinspection_schema.InstrumentInspectionWithStationAndInstrumentResponse.schema()
        )
    )


@router.post(
    "/instrument-inspections"
)
@handle_exceptions
def create_instrument_inspection(
    data: instrumentinspection_schema.CreateInstrumentInspection,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            instrumentinspection_service.create(db_session=db_session,
                                                data=data)
        ],
        message=_("Successfully created instrument inspection."),
        schema=translate_schema(
            _,
            instrumentinspection_schema.InstrumentInspectionResponse.schema()
        )
    )


@router.put(
    "/instrument-inspections/{performed_on}/{inspection_datetime}"
)
@handle_exceptions
def update_instrument_inspection(
    performed_on: str,
    inspection_datetime: str,
    data: instrumentinspection_schema.UpdateInstrumentInspection,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            instrumentinspection_service.update(
                db_session=db_session,
                performed_on=performed_on,
                inspection_datetime=inspection_datetime,
                updates=data,
            )
        ],
        message=_("Successfully updated instrument inspection."),
        schema=translate_schema(
            _,
            instrumentinspection_schema.InstrumentInspectionResponse.schema()
        )
    )


@router.delete(
    "/instrument-inspections/{performed_on}/{inspection_datetime}"
)
@handle_exceptions
def delete_instrument_inspection(
    performed_on: str,
    inspection_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    instrumentinspection_service.delete(
        db_session=db_session,
        performed_on=performed_on,
        inspection_datetime=inspection_datetime,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted instrument inspection."),
        schema=translate_schema(
            _,
            instrumentinspection_schema.InstrumentInspectionResponse.schema()
        )
    )
