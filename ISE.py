
from config import isedetail,url
import json
import requests
from requests.auth import HTTPBasicAuth
import logging

logger = logging.getLogger(__name__)
FORMAT = "[ Filename: %(filename)s -> Functioname: %(funcName)s(): LineNum: %(lineno)s ] %(levelname)s: %(message)s"
logging.basicConfig(format= FORMAT, filename="ISEAPI.log", filemode='a', level=logging.INFO)

class ISEAPI:

    # A class to manage various fucntions in ISE

    def __init__(self):
        self.iseip = isedetail['iseip']
        self.username = isedetail['ers_user']
        self.password = isedetail['ers_pass']
        self.verify = isedetail['verify']
        self.disablewarn = isedetail['disable_warnings']

    def getendpointurl(self,bulk):

        if bulk:
            return url['bulkendpoint']
        else:
            return url['endpoint']
    def getdeleteurl(self):
        return url["deleteendpoint"]

    def getiseip(self):
        return self.iseip

    def getusername(self):
        return self.username

    def getpassword(self):
        return self.password

    def apicall(self, method, url, payload):
        logger.info("Connection attempted for {} with {} performing {} operation.".format(url,payload,method))
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        resp = requests.request(method, url = url, data = payload, verify=self.verify, headers=headers, auth=HTTPBasicAuth(self.username,self.password))
        return resp
    def postendpoint(self):
        uri = self.getendpointurl(False)
        url = "https://" + str(self.getiseip()) + ":9060" + str(uri)
        rawdata = open("endpoint.json",'r')
        payload = json.loads(rawdata.read())
        resp = self.apicall("POST", url, json.dumps(payload))
        if resp.status_code == 201:
            logger.info("Endpoint is Added Successfully.")
        else:
            logger.error("Issue with Adding Endpoint. For more Details, Response from ISE was --->\n {}".format(resp.text))
    def postbulkendpoint(self):
        uri = self.getendpointurl(True)
        url = "https://" + str(self.getiseip()) + ":9060" + str(uri)
        rawdata = open("bulkendpoint.xml", 'r')
        resp = self.apicall("PUT", url, rawdata)
        if resp.status_code == 202:
            logger.info("All Endpoints are  Added Successfully.")
        else:
            logger.error("Issue with Adding Endpoint. For more Details, Response from ISE was --->\n {}".format(resp.text))
    def delendpoint(self,endpointid):
        uri = self.getdeleteurl()
        url = "https://" + str(self.getiseip()) + ":9060" + str(uri) + str(endpointid)
        resp = self.apicall("DELETE", url,{})
        if resp.status_code == 204:
            logger.info("{}  is  Deleted Successfully.")
        else:
            logger.error("Issue with Deleting Endpoint with UUID {}. For more Details, Response from ISE was --->\n {}".format(endpointid,resp.text))
    def getendpoint(self):
        uri = self.getendpointurl(False)
        url = "https://" + str(self.getiseip()) + ":9060" + str(uri)
        payload = {}
        resp = self.apicall("GET", url, json.dumps(payload))
        if resp.status_code == 201:
            logger.info("All Endpoints are  Fetched Successfully. For more Details -----> \n {}".format(resp.text))
        else:
            logger.error("Issue with Deleting Endpoint. For more Details, Response from ISE was --->\n {}".format(resp.text))


myise =  ISEAPI()
#myise.getendpoint()
myise.postendpoint()
#myise.postbulkendpoint()
#myise.delendpoint("f63def30-70f3-11eb-a6f1-7a52f728b7f3")




