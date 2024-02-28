import requests
import datetime
import json

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
    def gettraindelayinfo(self):
        for i in Train.gettrainlivestatus()["days_schedule"]:
            if i["station_code"] == Train.gettrainlivestatus()["curStn"]:
                return i["delay_in_arrival"]
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
    3. Full json response
            '''
    inputnumber = input(inputno)
    if inputnumber == '1':
        print(f'''
        Train Name : {train.gettrainlivestatus()["train_name"]}
        Train Type : {train.gettrainlivestatus()["train_type"]}
        Source Station : {stations[train.gettrainlivestatus()["source_station"]]} {train.gettrainlivestatus()["source_station"]}
        Current Station : {stations[train.gettrainlivestatus()["curStn"]]} {train.gettrainlivestatus()["curStn"]}
        Next Station -- {train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]} {stations[train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]]}
        Destination Station : {stations[train.gettrainlivestatus()["destination_station"]]} {train.gettrainlivestatus()["destination_station"]}
        ''')
        
        # working on Train is running late by {train.gettraindelayinfo()} minutes
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
        print(train.gettrainlivestatus())
if __name__ == "__main__":
    main()