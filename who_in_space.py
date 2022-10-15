import requests
from rolumns import Columns
from rolumns.renderers import MarkdownRenderer


def main() -> None:
    columns = Columns("people")
    columns.add("Name", "name")
    columns.add("Craft", "craft")

    data = requests.get("http://api.open-notify.org/astros.json").json()

    print()
    print(MarkdownRenderer(columns).render_string(data))


if __name__ == "__main__":
    main()
