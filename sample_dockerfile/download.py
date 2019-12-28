# https://raw.githubusercontent.com/vehicle-history/developers-portal/gh-pages-vh/Dockerfile

import csv
import requests
import os 
import time

def download(csvfile):
    i = 0
    url = "https://raw.githubusercontent.com/"
    with open(csvfile) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            new_url = url + row[0] + "/" + row[1].split("/")[len(row[1].split("/"))-1] + "/" + row[2]
            print("Downloading: " + new_url)
            os.makedirs("files/" + str(i))
            #urllib.request.urlretrieve(new_url, "files/" + str(i) + "/Dockerfile")
            #try:
            #    urllib.request.urlretrieve(new_url, "files/" + str(i) + "/Dockerfile")
            #except Exception as e:
            #    print(e)
            try:
                r = requests.get(new_url, verify=False)
                
                with open("files/" + str(i) + "/Dockerfile", "wb") as df:
                    df.write(r.content)
            except Exception as e:
                print(e)
            i += 1
            if i == 2000:
                return

requests.adapters.DEFAULT_RETRIES=5
download('github_dockerfile_info.csv')
