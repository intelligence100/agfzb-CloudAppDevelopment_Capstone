# IBM Action, method=GET, Python 3.9
# API https://eca74085.eu-gb.apigw.appdomain.cloud/postreviews
# Params
# {
# "review": 
#     {
#         "id": 1114,
#         "name": "Upkar Lidder",
#         "dealership": 15,
#         "review": "Great service!",
#         "purchase": false,
#         "another": "field",
#         "purchase_date": "02/16/2021",
#         "car_make": "Audi",
#         "car_model": "Car",
#         "car_year": 2021
#     }
# }
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    # my IAM_API_KEY
    authenticator = IAMAuthenticator("CWo8t7mAGKyhAJN2AxMmBOj6DqJTYg1ndXhYPaZfZiXM")
    service = CloudantV1(authenticator=authenticator)
    # my COUCH_URL
    service.set_service_url("https://1708aa9a-50ab-4ff8-9c91-61c949d17ed2-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }
