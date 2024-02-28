# get pnr status
import requests

pnrno = input("input the pnr number:")
# pnrno = 2638967619 # for testing
def getpnrdetails(pnrno):
    cookies = {
        'PNRViewed': '5',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.confirmtkt.com/pnr-status/'+str(pnrno), cookies=cookies, headers=headers)
    responsetext = response.text
    # print(responsetext)
    data = splitted = responsetext.split('data = {\"')[1].split('};')[0]
    jsonformatted = '{\"'+data+'}'
    def getdetails(jsonformatted):
            import json
            data = json.loads(jsonformatted)
            dat = f'''
        Pnr : {data["Pnr"]}
        Train Name : {data["TrainName"]}
        Train Number : {data["TrainNo"]}
        Boarding Date : {data["Doj"]}
        From : {data["From"]}
        To : {data["To"]}
        Reservation Upto : {data["ReservationUptoName"]}
        Boarding Point : {data["BoardingPoint"]}
        Class : {data["Class"]}
        Chart Prepared : {data["ChartPrepared"]}
        Boarding Station Name : {data["BoardingStationName"]}
        Train Status : {data["TrainStatus"]}
        Train Cancelled Flag : {data["TrainCancelledFlag"]}
        Passenger Count : {data["PassengerCount"]}
        Departure Time : {data["DepartureTime"]}
        Arrival Time : {data["ArrivalTime"]}
        Expected Platform No : {data["ExpectedPlatformNo"]}
        Booking Fare : {data["BookingFare"]}
        Ticket Fare : {data["TicketFare"]}
        Coach Position : {data["CoachPosition"]}
        Rating : {data["Rating"]}
        Food Rating : {data["FoodRating"]}
        Punctuality Rating : {data["PunctualityRating"]}
        Cleanliness Rating : {data["CleanlinessRating"]}
        Source Name : {data["SourceName"]}
        Destination Name : {data["DestinationName"]}
        Duration : {data["Duration"]}
        Rating Count : {data["RatingCount"]}
        Has Pantry : {data["HasPantry"]}
        '''
            for i in data["PassengerStatus"]:
                dat += f'''
        Reference Id : {i["ReferenceId"]}
        Pnr : {i["Pnr"]}
        Number : {i["Number"]}
        Prediction : {i["Prediction"]}
        Prediction Percentage : {i["PredictionPercentage"]}
        Confirm Tkt Status : {i["ConfirmTktStatus"]}
        Coach : {i["Coach"]}
        Berth : {i["Berth"]}
        Booking Status : {i["BookingStatus"]}
        Current Status : {i["CurrentStatus"]}
        Coach Position : {i["CoachPosition"]}
        Booking Berth No : {i["BookingBerthNo"]}
        Booking Coach Id : {i["BookingCoachId"]}
        Booking Status New : {i["BookingStatusNew"]}
        Booking Status Index : {i["BookingStatusIndex"]}
        Current Berth No : {i["CurrentBerthNo"]}
        Current Coach Id : {i["CurrentCoachId"]}
        Booking Berth Code : {i["BookingBerthCode"]}
        Current Berth Code : {i["CurrentBerthCode"]}
        Current Status New : {i["CurrentStatusNew"]}
        Current Status Index : {i["CurrentStatusIndex"]}
        '''
            return dat
    return getdetails(jsonformatted)