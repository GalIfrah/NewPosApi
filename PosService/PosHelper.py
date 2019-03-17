import requests
from pytest_testconfig import config


def open(client_code, bid, station_name, order_num):

        request = {

            "ClientCode": client_code,
            "BID": bid,
            "StationName": station_name,
            "OrderNum": order_num
        }

        response = requests.post(config['POS_ENDPOINT'] + '/api/table/act/open', params=request)

        response_object = response.json()

        return response_object
