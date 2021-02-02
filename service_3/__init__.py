import logging
from random import randint
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
        
    numbers = ""
    for _ in range(5):
        numbers += str(randint(0,9))

    return func.HttpResponse(
        numbers,
        status_code=200
    )