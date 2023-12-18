import json
import requests

def send_data(data,dataname,ip_addr,port):
    json_data = {}
    json_data.update(zip(data,dataname))

    # create request with header
    url = "http://" + ip_addr + ":" + port + "/"

    response = requests.post(
        url,
        data = json.dumps(json_data)
    )

    print("[DEBUG] response:" + response.json())
    