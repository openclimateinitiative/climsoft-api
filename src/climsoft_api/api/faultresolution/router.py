import climsoft_api.api.faultresolution.schema as faultresolution_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import faultresolution_service
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
    "/fault-resolutions"
)
@handle_exceptions
def get_instrument_inspection(
    resolved_datetime: str = None,
    associated_with: str = None,
    resolved_by: str = None,
    remarks: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, instrument_inspection = faultresolution_service.query(
        db_session=db_session,
        resolved_datetime=resolved_datetime,
        associated_with=associated_with,
        resolved_by=resolved_by,
        remarks=remarks,
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
            faultresolution_schema.FaultResolutionQueryResponse.schema()
        )
    )


@router.get(
    "/fault-resolutions/{resolved_datetime}/{associated_with}"
)
@handle_exceptions
def get_instrument_inspection_by_id(
    resolved_datetime: str,
    associated_with: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            faultresolution_service.get(
                db_session=db_session,
                resolved_datetime=resolved_datetime,
                associated_with=associated_with,
            )
        ],
        message=_("Successfully fetched instrument inspection."),
        schema=translate_schema(
            _,
            faultresolution_schema.FaultResolutionWithInstrumentFaultReportResponse.schema(),
        )
    )


@router.post(
    "/fault-resolutions"
)
@handle_exceptions
def create_instrument_inspection(
    data: faultresolution_schema.CreateFaultResolution,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[faultresolution_service.create(
            db_session=db_session,
            data=data
        )],
        message=_("Successfully created instrument inspection."),
        schema=translate_schema(
            _,
            faultresolution_schema.FaultResolutionResponse.schema()
        )
    )


@router.put(
    "/fault-resolutions/{resolved_datetime}/{associated_with}"
)
@handle_exceptions
def update_instrument_inspection(
    resolved_datetime: str,
    associated_with: str,
    data: faultresolution_schema.UpdateFaultResolution,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            faultresolution_service.update(
                db_session=db_session,
                resolved_datetime=resolved_datetime,
                associated_with=associated_with,
                updates=data,
            )
        ],
        message=_("Successfully updated instrument inspection."),
        schema=translate_schema(
            _,
            faultresolution_schema.FaultResolutionResponse.schema()
        )
    )


@router.delete(
    "/fault-resolutions/{resolved_datetime}/{associated_with}"
)
@handle_exceptions
def delete_instrument_inspection(
    resolved_datetime: str,
    associated_with: str,
    db_session: Session = Depends(deps.get_session),
):
    faultresolution_service.delete(
        db_session=db_session,
        resolved_datetime=resolved_datetime,
        associated_with=associated_with,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted instrument inspection."),
        schema=translate_schema(
            _,
            faultresolution_schema.FaultResolutionResponse.schema()
        )
    )
