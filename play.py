import gettext
import json
import os.path

from climsoft_api.api.stationelement.schema import StationElementWithStation
from climsoft_api.utils.response import translate_schema


ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


LOCALE_DIR = os.path.join(
    ROOT_DIR,
    "src/climsoft_api/locale"
)


if __name__ == "__main__":
    fr = gettext.translation(
        domain="climsoft_messages",
        localedir=LOCALE_DIR,
        languages=["fr"],
    )

    fr.install()
    translated_schema = translate_schema(
        fr.gettext,
        StationElementWithStation.schema()
    )

    assert translated_schema[
               "definitions"
           ][
               "Station"
           ][
               "properties"
           ][
               "station_name"
           ][
               "title"
           ] == "Nom de la station"


