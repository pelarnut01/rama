from line_protocol_parser import parse_line
import requests
from pathlib import Path
import os


url = 'http://192.168.1.81:8086/api/v2/write'

myobj = {'org': 'Daikin','bucket':'rama'}



data_path = Path.joinpath(Path.home(), "Documents", "rama")
data_filenames = [file.name for file in list(data_path.iterdir())]
print(data_filenames) # ได้ /home/phyblas/umi/ebi.py

for filename in data_filenames:
    filepath = Path.joinpath(data_path, filename)
    print(filepath)
    json_data = open(filepath, 'rb').read()
    with open(filepath, "r") as file:
        x = requests.post(url, data=json_data,params = myobj ,headers = {"Content-Type":"text/plain","Authorization":"Token P3q5pptgiZ2f07or9OQMJ6Vf6Tr-bWbXA14sWNKfnDNijXcMcw1VvoCXW_KKsDK8usNfZgYp-izG0xT6fr9jwA=="})
        print(x.text)






