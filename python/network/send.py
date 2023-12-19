import json
import requests

def send_data(data,dataname,ip_addr,port,uri):
    print("data:"+str(data)+" "+"dataname:"+str(dataname))
    json_data = dict(zip(dataname,data))
    
    # create request with header
    url = "http://" + ip_addr + ":" + port + uri 

    response = requests.post(
        url,
        json = json.dumps(json_data)
    )
