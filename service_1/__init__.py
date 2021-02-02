import logging
import azure.functions as func
import requests
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "FROM PORTAL"
key = "FROM PORTAL"

client = CosmosClient(endpoint, key)

database = client.create_database_if_not_exists(id="RandomUsernames")
container = database.create_container_if_not_exists(
    id="RandomUsernamesContainer",
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = requests.get("URL FOR SERVICE 2 FROM THE PORTAL")
    numbers = requests.get("URL FOR SERVICE 3 FROM THE PORTAL")

    username = letters.text + numbers.text

    container.create_item(body={
        "id": str(1),
        "username": username
        })

    return func.HttpResponse(
        letters.text + numbers.text,
        status_code=200
    )