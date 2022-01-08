from fastapi import APIRouter, Depends
from climsoft_api.services import synopfeature_service
import climsoft_api.api.synopfeature.schema as synopfeature_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get("/", response_model=synopfeature_schema.SynopFeatureResponse)
def get_qc_types(
    abbreviation: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        qc_types = synopfeature_service.query(
            db_session=db_session,
            abbreviation=abbreviation,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response(
            result=qc_types, message="Successfully fetched qc_types."
        )
    except synopfeature_service.FailedGettingSynopFeatureList as e:
        return get_error_response(message=str(e))


@router.get("/{abbreviation}", response_model=synopfeature_schema.SynopFeatureResponse)
def get_qc_type_by_id(
    abbreviation: str, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                synopfeature_service.get(
                    db_session=db_session, abbreviation=abbreviation
                )
            ],
            message="Successfully fetched qc_type.",
        )
    except synopfeature_service.FailedGettingSynopFeature as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=synopfeature_schema.SynopFeatureResponse)
def create_qc_type(
    data: synopfeature_schema.CreateSynopFeature,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[synopfeature_service.create(db_session=db_session, data=data)],
            message="Successfully created qc_type.",
        )
    except synopfeature_service.FailedCreatingSynopFeature as e:
        return get_error_response(message=str(e))


@router.put("/{abbreviation}", response_model=synopfeature_schema.SynopFeatureResponse)
def update_qc_type(
    abbreviation: str,
    data: synopfeature_schema.UpdateSynopFeature,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                synopfeature_service.update(
                    db_session=db_session, abbreviation=abbreviation, updates=data
                )
            ],
            message="Successfully updated qc_type.",
        )
    except synopfeature_service.FailedUpdatingSynopFeature as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{abbreviation}", response_model=synopfeature_schema.SynopFeatureResponse
)
def delete_qc_type(abbreviation: str, db_session: Session = Depends(deps.get_session)):
    try:
        synopfeature_service.delete(db_session=db_session, abbreviation=abbreviation)
        return get_success_response(result=[], message="Successfully deleted qc_type.")
    except synopfeature_service.FailedDeletingSynopFeature as e:
        return get_error_response(message=str(e))
