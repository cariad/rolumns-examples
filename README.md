# Rolumns examples

Full code examples of the [Rolumns](https://rolumns.dev) Python package.

## Setup

```console
pipenv install
```

## Examples

### who_in_space.py

[who_in_space.py](https://github.com/cariad/rolumns-examples/blob/main/who_in_space.py) calls [Open Notify](http://open-notify.org)'s [How Many People Are In Space Right Now?](http://open-notify.org/Open-Notify-API/People-In-Space/) API and uses [Rolumns](https://rolumns.dev) to present the result in a Markdown table.

```console
$ python who_in_space.py

| Name                   | Craft    |
| ---------------------- | -------- |
| Kjell Lindgren         | ISS      |
| Bob Hines              | ISS      |
| Samantha Cristoforetti | ISS      |
| Jessica Watkins        | ISS      |
| Cai Xuzhe              | Tiangong |
| Chen Dong              | Tiangong |
| Liu Yang               | Tiangong |
| Sergey Prokopyev       | ISS      |
| Dmitry Petelin         | ISS      |
| Frank Rubio            | ISS      |
| Nicole Mann            | ISS      |
| Josh Cassada           | ISS      |
| Koichi Wakata          | ISS      |
| Anna Kikina            | ISS      |
```

### who_in_space_xlsx.py

[who_in_space_xlsx.py](https://github.com/cariad/rolumns-examples/blob/main/who_in_space_xlsx.py)  calls [Open Notify](http://open-notify.org)'s [How Many People Are In Space Right Now?](http://open-notify.org/Open-Notify-API/People-In-Space/) API then uses [Rolumns](https://rolumns.dev) with [openpyxl](https://openpyxl.readthedocs.io/) to export the result to an XLSX spreadsheet.

```console
$ python who_in_space_xlsx.py
Exported to /home/cariad/rolumns-examples/who_in_space.xlsx
```
