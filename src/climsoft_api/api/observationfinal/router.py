import climsoft_api.api.observationfinal.schema as observationfinal_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import observationfinal_service
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
    "/observation-finals"
)
@handle_exceptions
def get_observation_finals(
    recorded_from: str = None,
    described_by: int = None,
    obs_datetime: str = None,
    qc_status: int = None,
    acquisition_type: int = None,
    obs_level: int = None,
    obs_value: float = None,
    flag: str = None,
    period: int = None,
    qc_type_log: str = None,
    data_form: str = None,
    captured_by: str = None,
    mark: bool = None,
    temperature_units: str = None,
    precipitation_units: str = None,
    cloud_height_units: str = None,
    vis_units: str = None,
    data_source_timezone: int = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, observation_finals = observationfinal_service.query(
        db_session=db_session,
        recorded_from=recorded_from,
        obs_datetime=obs_datetime,
        qc_status=qc_status,
        described_by=described_by,
        acquisition_type=acquisition_type,
        obs_value=obs_value,
        obs_level=obs_level,
        flag=flag,
        period=period,
        qc_type_log=qc_type_log,
        data_form=data_form,
        captured_by=captured_by,
        mark=mark,
        temperature_units=temperature_units,
        precipitation_units=precipitation_units,
        cloud_height_units=cloud_height_units,
        vis_units=vis_units,
        data_source_timezone=data_source_timezone,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=observation_finals,
        message=_("Successfully fetched observation finals."),
        schema=translate_schema(
            _,
            observationfinal_schema.ObservationFinalQueryResponse.schema()
        )
    )


@router.get(
    "/observation-finals/{recorded_from}/{described_by}/{obs_datetime}"
)
@handle_exceptions
def get_observation_final_by_id(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            observationfinal_service.get(
                db_session=db_session,
                recorded_from=recorded_from,
                described_by=described_by,
                obs_datetime=obs_datetime,
            )
        ],
        message=_("Successfully fetched observation final."),
        schema=translate_schema(
            _,
            observationfinal_schema.ObservationFinalWithChildrenResponse.schema()
        )
    )


@router.post(
    "/observation-finals",
)
@handle_exceptions
def create_observation_final(
    data: observationfinal_schema.CreateObservationFinal,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[observationfinal_service.create(
            db_session=db_session,
            data=data
        )],
        message=_("Successfully created observation final."),
        schema=translate_schema(
            _,
            observationfinal_schema.ObservationFinalResponse.schema()
        )
    )


@router.put(
    "/observation-finals/{recorded_from}/{described_by}/{obs_datetime}"
)
@handle_exceptions
def update_observation_final(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    data: observationfinal_schema.UpdateObservationFinal,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            observationfinal_service.update(
                db_session=db_session,
                recorded_from=recorded_from,
                described_by=described_by,
                obs_datetime=obs_datetime,
                updates=data,
            )
        ],
        message=_("Successfully updated observation final."),
        schema=translate_schema(
            _,
            observationfinal_schema.ObservationFinalResponse.schema()
        )
    )


@router.delete(
    "/observation-finals/{recorded_from}/{described_by}/{obs_datetime}"
)
@handle_exceptions
def delete_observation_final(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    observationfinal_service.delete(
        db_session=db_session,
        recorded_from=recorded_from,
        described_by=described_by,
        obs_datetime=obs_datetime,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted observation final."),
        schema=translate_schema(
            _,
            observationfinal_schema.ObservationFinalResponse.schema()
        )
    )
