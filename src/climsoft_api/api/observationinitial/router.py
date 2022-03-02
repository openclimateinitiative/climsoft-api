from fastapi import APIRouter, Depends
from climsoft_api.services import observationinitial_service
import climsoft_api.api.observationinitial.schema as observationinitial_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps


from gettext import gettext as _

router = APIRouter()


@router.get("/", response_model=observationinitial_schema.ObservationInitialQueryResponse)
def get_observation_initials(
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
    try:
        total, observation_initials = observationinitial_service.query(
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
            result=observation_initials,
            message=_("Successfully fetched observation initials."),
        )
    except observationinitial_service.FailedGettingObservationInitialList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{recorded_from}/{described_by}/{obs_datetime}/{qc_status}/{acquisition_type}",
    response_model=observationinitial_schema.ObservationInitialWithChildrenResponse,
)
def get_observation_initial_by_id(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    qc_status: int,
    acquisition_type: int,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                observationinitial_service.get(
                    db_session=db_session,
                    recorded_from=recorded_from,
                    described_by=described_by,
                    obs_datetime=obs_datetime,
                    qc_status=qc_status,
                    acquisition_type=acquisition_type,
                )
            ],
            message=_("Successfully fetched observation initial."),
        )
    except observationinitial_service.FailedGettingObservationInitial as e:
        return get_error_response(message=str(e))


@router.post(
    "/",
    response_model=observationinitial_schema.ObservationInitialResponse
)
def create_observation_initial(
    data: observationinitial_schema.CreateObservationInitial,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                observationinitial_service.create(
                    db_session=db_session,
                    data=data
                )
            ],
            message=_("Successfully created observation initial."),
        )
    except observationinitial_service.FailedCreatingObservationInitial as e:
        return get_error_response(message=str(e))


@router.put(
    "/{recorded_from}/{described_by}/{obs_datetime}/{qc_status}/{acquisition_type}",
    response_model=observationinitial_schema.ObservationInitialResponse,
)
def update_observation_initial(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    qc_status: int,
    acquisition_type: int,
    data: observationinitial_schema.UpdateObservationInitial,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                observationinitial_service.update(
                    db_session=db_session,
                    recorded_from=recorded_from,
                    described_by=described_by,
                    obs_datetime=obs_datetime,
                    qc_status=qc_status,
                    acquisition_type=acquisition_type,
                    updates=data,
                )
            ],
            message=_("Successfully updated observation initial."),
        )
    except observationinitial_service.FailedUpdatingObservationInitial as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{recorded_from}/{described_by}/{obs_datetime}/{qc_status}/{acquisition_type}",
    response_model=observationinitial_schema.ObservationInitialResponse,
)
def delete_observation_initial(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    qc_status: int,
    acquisition_type: int,
    db_session: Session = Depends(deps.get_session),
):
    try:
        observationinitial_service.delete(
            db_session=db_session,
            recorded_from=recorded_from,
            described_by=described_by,
            obs_datetime=obs_datetime,
            qc_status=qc_status,
            acquisition_type=acquisition_type,
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted observation initial.")
        )
    except observationinitial_service.FailedDeletingObservationInitial as e:
        return get_error_response(message=str(e))
