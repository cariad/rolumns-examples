# Rolumns examples

Full code examples of the [Rolumns](https://rolumns.dev) Python package.

## Setup

```console
pipenv install
```

## Examples

### neo.py

[neo.py](https://github.com/cariad/rolumns-examples/blob/main/neo.py) calls NASA's [Near-Earth Objects](https://api.nasa.gov/) API and uses [Rolumns](https://rolumns.dev) to present a list of all near-Earth objects whose nearest approach to Earth will be within the coming week.

The script uses a demo NASA API key by default, and will respond much faster if you use your own.

```console
$ python neo.py YOUR_API_KEY_IF_YOU_HAVE_ONE
Requesting near-earth objects from NASA...

| Name                          | Size (metres) | Potentially Hazardous | When              | Miss By (km) |
| ----------------------------- | ------------: | --------------------: | ----------------- | -----------: |
| 4034 Vishnu (1986 PA)         |   552 - 1,237 |                    🔥 | 2022-Oct-25 19:57 |   49,934,636 |
| (1999 SE10)                   |     265 - 595 |                       | 2022-Oct-25 10:14 |   57,772,242 |
| (2012 UU68)                   |      63 - 142 |                       | 2022-Oct-25 20:51 |   11,880,954 |
| (2014 KP84)                   |     185 - 415 |                    🔥 | 2022-Oct-25 19:57 |   60,714,066 |
| (2016 TH94)                   |       31 - 72 |                       | 2022-Oct-25 21:45 |    7,305,745 |
| (2017 RH16)                   |       15 - 35 |                       | 2022-Oct-25 08:09 |   39,382,505 |
| (2017 TZ5)                    |       11 - 26 |                       | 2022-Oct-25 12:36 |   14,075,238 |
```

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
