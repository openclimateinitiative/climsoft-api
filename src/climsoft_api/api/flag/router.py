import climsoft_api.api.flag.schema as flag_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import flag_service
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


@router.get("/flags")
@handle_exceptions
def get_flags(
    character_symbol: str = None,
    num_symbol: int = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, flags = flag_service.query(
        db_session=db_session,
        character_symbol=character_symbol,
        num_symbol=num_symbol,
        description=description,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=flags,
        message=_("Successfully fetched flags."),
        schema=translate_schema(
            _,
            flag_schema.FlagQueryResponse.schema()
        )
    )


@router.get("/flags/{character_symbol}")
@handle_exceptions
def get_flag_by_id(
    character_symbol: str, db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            flag_service.get(
                db_session=db_session,
                character_symbol=character_symbol
            )
        ],
        message=_("Successfully fetched flag."),
        schema=translate_schema(
            _,
            flag_schema.FlagResponse.schema()
        )
    )


@router.post("/flags")
@handle_exceptions
def create_flag(
    data: flag_schema.CreateFlag,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[flag_service.create(db_session=db_session, data=data)],
        message=_("Successfully created flag."),
        schema=translate_schema(
            _,
            flag_schema.FlagResponse.schema()
        )
    )


@router.put("/flags/{character_symbol}")
@handle_exceptions
def update_flag(
    character_symbol: str,
    data: flag_schema.UpdateFlag,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            flag_service.update(
                db_session=db_session,
                character_symbol=character_symbol,
                updates=data,
            )
        ],
        message=_("Successfully updated flag."),
        schema=translate_schema(
            _,
            flag_schema.FlagResponse.schema()
        )
    )


@router.delete("/flags/{character_symbol}")
@handle_exceptions
def delete_flag(
    character_symbol: str,
    db_session: Session = Depends(deps.get_session)
):
    flag_service.delete(
        db_session=db_session,
        character_symbol=character_symbol
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted flag."),
        schema=translate_schema(
            _,
            flag_schema.FlagResponse.schema()
        )
    )
