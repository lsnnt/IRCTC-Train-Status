import requests
import datetime
import json
from pnr import getpnrdetails
class Train:
    def __init__(self, train_no='12954', date=datetime.datetime.now().strftime("%d-%m-%Y")):
        self.train_no = train_no
        self.date = date
    def gettrainlivestatus(self):
        params = {
            'train_no': str(self.train_no),
            'lang': 'en',
            'date': str(self.date),
        }

        response = requests.get('https://whereismytrain.in/cache/live_status', params=params)
        return response.json()
def gettraindelayinfo(stations, train):
    for i in range(0,len(train.gettrainlivestatus()["days_schedule"])):
        if train.gettrainlivestatus()["days_schedule"][i]["station_code"] == train.gettrainlivestatus()["curStn"]:
            return str(train.gettrainlivestatus()["days_schedule"][i-1]["delay_in_arrival"])+' minutes at station '+stations[train.gettrainlivestatus()["days_schedule"][i-1]["station_code"]]+" "+train.gettrainlivestatus()["days_schedule"][i-1]["station_code"]
    # return 'No delay info'
def main():
    tno = input('Enter the train number: ')
    date = input('Enter the date (dd-mm-yyyy) with dash or leave for today: ')
    if date == '':
        date = datetime.datetime.now().strftime("%d-%m-%Y")
    train = Train(tno, date)
    with open('stations.json', 'r') as f:
        stations = json.load(f)
        print('Fetching the live status of train...')
    inputno = '''
    1. Source Station current station next station destination station
    2. Train will come on which platform
    3. Print Delay info
    4. Get PNR details
    5. Full json response
    Enter the number:
> '''
    inputnumber = input(inputno)
    if inputnumber == '1':
        try:
            print(f'''
            Train Name : {train.gettrainlivestatus()["train_name"]}
            Train Type : {train.gettrainlivestatus()["train_type"]}
            Source Station : {stations[train.gettrainlivestatus()["source_station"]]} {train.gettrainlivestatus()["source_station"]}
            Current Station : {stations[train.gettrainlivestatus()["curStn"]]} {train.gettrainlivestatus()["curStn"]}
            Next Station -- {train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]} {stations[train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]]}
            Destination Station : {stations[train.gettrainlivestatus()["destination_station"]]} {train.gettrainlivestatus()["destination_station"]}
            ''')
        except:
            print(f'''
            Train Name : {train.gettrainlivestatus()["train_name"]}
            Train Type : {train.gettrainlivestatus()["train_type"]}
            Source Station : {stations[train.gettrainlivestatus()["source_station"]]} {train.gettrainlivestatus()["source_station"]}
            Current Station : {stations[train.gettrainlivestatus()["curStn"]]} {train.gettrainlivestatus()["curStn"]}
            Next Station -- {train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]}
            Destination Station : {stations[train.gettrainlivestatus()["destination_station"]]} {train.gettrainlivestatus()["destination_station"]}
            ''')
    elif inputnumber == '2':
        print(f'enter the short code of the stations from the given list')
        for i in train.gettrainlivestatus()["days_schedule"]:
            print(f'{i["station_code"]} {stations[i["station_code"]]}')
        station = input('Enter the station code: ')
        for i in train.gettrainlivestatus()["days_schedule"]:
            if i["station_code"] == station:
                print(f'Train will come on platform {i["platform"]}')
            # print(f'Train will come on platform {train.gettrainlivestatus()["days_schedule"][station]["platform"]}')
    elif inputnumber == '3':
        print(gettraindelayinfo(stations, train))
    elif inputnumber == '4':
        pnrno = input("input the pnr number:")
        print(getpnrdetails(pnrno))
    elif inputnumber == '5':
        print(train.gettrainlivestatus())
if __name__ == "__main__":
    main()