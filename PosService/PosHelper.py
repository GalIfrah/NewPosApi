
import requests
from pytest_testconfig import config


def open(client_code, bid, station_name, order_num):

        request_params = {

            "ClientCode": client_code,
            "BID": bid,
            "StationName": station_name,
            "OrderNum": order_num
        }

        response = requests.post(config['POS_ENDPOINT'] + '/api/table/act/open', params=request_params)

        response_object = response.json()

        return response_object


"""
Response:

                {
                "Success": true// required bool
                "OrderID": INT // required, order id in mycheck
                "CustomerWeight": "", // not required
                "CustomerName": "", // required STRING
                "Reward" : array // need to check if required, probably yes.
                }
                
Failed response:

                {
                  "Success": false // required
                  "ReturnString": STRING // required only on error
                  "ErrorCode": INT // required only on error not in use in positouch
                }

1 - "error" 
125  - "Sorry, the tab is closed or cancelled."
144 - "This order is already open. No need to re-open it."
425 - "Code is incorrect or out of date. Please try again and if the problem continues, ask your friend to generate a new code."
711 - "Sorry, the tab is already open."
712 - "This ClientCode has expired. The MyCheck user must generate a new one"

"""


def posAuthorize():

        request_headers = {

            "content-type": "form-url-endcoded",
            "ContentLength": 1000,
            "KeepAlive": False,
            "OS - Version": "xxxxxxxxxxx",
            "Agent-Version": "xxxxxxxxxxx"


        }

        payload = {

            "refresh_token": "need to get it from yaron"
        }

        # need to decide what comes from outside

        response = requests.post(config['POS_ENDPOINT'] + '/api/PosAuthorize', headers=request_headers, data=payload)

        response_object = response.json()

        return response_object


"""
Response:

                {
                  "Success": true
                  "valid_time": 300
                  "access_token": STRING
                }
                
Failed:

                {
                  "Success": false
                }

"""


def healthy(bid, station_id):

    request_params = {

        "BID": bid,
        "StationID": station_id,

    }

    response = requests.post(config['POS_ENDPOINT'] + '/api/healthy', params=request_params)

    response_object = response.json()

    return response_object


"""
Response:

                {
                    "Success": true
                }

Failed:

                {
                    "Success": false,
                    "ReturnString": "Thanks for asking",
                    "ErrorCode": 0
                }

"""
