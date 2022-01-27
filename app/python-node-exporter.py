import requests
import http.server
import socketserver
import time
from threading import Thread



def GetDataFunc():
    while True :

        #----------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------
        #               in this part, i'll get some data from an API
        #
        #               and put it into "metricsDictionary"
        #
        #              you can remove this part and add your own script
        #
        #             (put your key/value items into "metricsDictionary")
        #----------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------
       
        service = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json",timeout=3)
        service_json  = service.json()

        metricsDictionary = {}
        metricsDictionary["Bitcoin_USD: "] = service_json["bpi"]["USD"]["rate"].replace(",", "")
        metricsDictionary["Bitcoin_EUR: "] = service_json["bpi"]["EUR"]["rate"].replace(",", "")

        #----------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------
        #
        #	Now, I'll put all key/value items of metricsDictionary into metrics.txt file
        #
        #----------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------

        # This function will get data every 5 seconds
        time.sleep(5)

        # open file to write new data
        file_object = open('metrics.txt', 'w')
        
        for item in metricsDictionary :
            file_object.write("\n")
            file_object.write(item)
            file_object.write(metricsDictionary[item])


# run GetDataFunc func in the background
background_thread = Thread(target = GetDataFunc)
background_thread.start()





#----------------run http server on port 9999-----------------

def WebServer():
    PORT = 9999

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


# run WebServer func in the background
background_thread = Thread(target = WebServer)
background_thread.start()
