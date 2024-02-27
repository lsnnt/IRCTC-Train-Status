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
def main():
    tno = input('Enter the train number: ')
    date = input('Enter the date (dd-mm-yyyy) with dash or leave for today: ')
    if date == '':
        date = datetime.datetime.now().strftime("%d-%m-%Y")
    train = Train(tno, date)
    with open('stations.json', 'r') as f:
        stations = json.load(f)
        print('Fetching the live status of train...')
    print(f'''
    source station : {stations[train.gettrainlivestatus()["source_station"]]} {train.gettrainlivestatus()["source_station"]}
    current station : {stations[train.gettrainlivestatus()["curStn"]]} {train.gettrainlivestatus()["curStn"]} next stn -- {train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]} {stations[train.gettrainlivestatus()["pitstop_next_to_curstn"]["station_code"]]}
    destination station : {stations[train.gettrainlivestatus()["destination_station"]]} {train.gettrainlivestatus()["destination_station"]}
    ''')
        # print(train.gettrainlivestatus()["curStn"])



if __name__ == "__main__":
    # train = Train(12345, '27-02-2024', 'NDLS', 'BCT')
    # print(train.gettrainlivestatus())
    # print(Train.gettrainroute(12345))
    # print(datetime.datetime.now().strftime("%d-%m-%Y"))
    main()