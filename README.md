# IRCTC Train Status
This project mainly try something new to get juicy info out of Api provided by google {Whereismytrain}
### How to use it
For termux users we have dedicated documentation [here](https://github.com/lsnnt/IRCTC-Train-Status/blob/main/docs/fortermux.md)

Make sure you have python3 and pip3 installed
- Run ```pip3 install -r requirements.txt```
- Run ```python3 main.py```
### Apis used for fetching station data
* https://api.railyatri.in/api/common_city_station_search.json
### Api used for train details
* https://whereismytrain.in/cache/live_status?train_no=TRAINNO&date=DATE(in dd-mm-yyyy format)&lang=hi
### Url used for pnr status
* https://www.confirmtkt.com/pnr-status/YOURPNRNum
for more info see code
### Contributing
Want to contribute to this project not limit the project to this and take it to even more heights 

You are Welcome to open a PR :smiley:
