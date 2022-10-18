# neo.py prints a Markdown table of all known near-Earth objects that have their
# closest approach to Earth in the coming week.
#
# USAGE:
#
#     python neo.py [NASA API KEY]
#
# A restricted demo key will be used if you don't have a NASA API key. Get one
# for free at https://api.nasa.gov.

from datetime import datetime
from math import ceil, floor
from sys import argv

import requests
from rolumns import Columns, Source, TranslationState
from rolumns.enums import ColumnAlignment
from rolumns.groups import ByKey
from rolumns.renderers import MarkdownRenderer

# Translators
# -----------


def estimated_diameter(state: TranslationState) -> str:
    """
    Converts a distance dictionary into a single string representation of a
    metre range.
    """

    meters = state.value["meters"]
    est_min = "{:,}".format(floor(float(meters["estimated_diameter_min"])))
    est_max = "{:,}".format(ceil(float(meters["estimated_diameter_max"])))
    return f"{est_min} - {est_max}"


def potentially_hazardous(state: TranslationState) -> str:
    """
    Emits fire if the object is potentially hazardous.
    """

    return "🔥" if state.value else ""


def round_down(state: TranslationState) -> str:
    """
    Rounds the value down to the nearest integer.
    """

    return "{:,}".format(floor(float(state.value)))


# Main
# -----------


def main(key: str) -> None:
    # API

    api = "https://api.nasa.gov/neo/rest/v1/feed"

    args = {
        "start_date": datetime.now().strftime("%Y-%m-%d"),
        "api_key": key,
    }

    uri = api + "?" + "&".join([f"{k}={v}" for k, v in args.items()])

    print("Requesting near-earth objects from NASA...")
    data = requests.get(uri).json()
    print()

    # Columns

    root = Columns(ByKey("near_earth_objects"))

    objects_by_date = root.group(ByKey.values())
    objects_by_date.add("Name", "name")

    objects_by_date.add(
        "Size (metres)",
        Source("estimated_diameter", translator=estimated_diameter),
    )

    objects_by_date.add(
        "Potentially Hazardous",
        Source(
            "is_potentially_hazardous_asteroid",
            translator=potentially_hazardous,
        ),
    )

    approach = objects_by_date.group("close_approach_data")
    approach.add("When", "close_approach_date_full")
    approach.add(
        "Miss By (km)",
        Source("miss_distance.kilometers", translator=round_down),
    )

    # Render

    renderer = MarkdownRenderer(root)
    renderer.append("Name")
    renderer.append("Size (metres)", alignment=ColumnAlignment.RIGHT)
    renderer.append("Potentially Hazardous", alignment=ColumnAlignment.RIGHT)
    renderer.append("When")
    renderer.append("Miss By (km)", alignment=ColumnAlignment.RIGHT)

    print(renderer.render_string(data))


if __name__ == "__main__":
    key = argv[1] if len(argv) == 2 else "DEMO_KEY"
    main(key)
