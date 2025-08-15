import requests
from datetime import datetime
from zoneinfo import ZoneInfo

logFilePath="Logs/Logs.txt"
url="""https://eci.ec.europa.eu/045/public/api/report/progression"""
#Time Logs- Asia/Kolkata (India Standard Time)
currentLocalTime=datetime.now(ZoneInfo("Asia/Kolkata"))
currentLocalTime=currentLocalTime.strftime("%Y-%m-%d %H:%M:%S %Z")

def writeLogs(message,logFilePath=logFilePath):
    with open(logFilePath,"a") as file:
        file.write(message) 

try:
    response=requests.get(url)
    if(response.status_code!=200):
        message=f"""Time={currentLocalTime} Message=Failed API Call, Status-{response.status_code}\n"""
        writeLogs(message,logFilePath)
    else:
        try:
            data=response.json()
            signatureCount=data["signatureCount"]
            goal=data["goal"]
            message=f"""Time={currentLocalTime} Message=Signature Count-{signatureCount}, Goal-{goal}\n"""
            writeLogs(message,logFilePath)
            #print(f"Signatures- {signatureCount} Goal- {goal}")
        except Exception as e:
            message=f"""Time={currentLocalTime} Message=Unexpected Response Structure, Response Text-{response.text}\n"""
            writeLogs(message,logFilePath)
except Exception as e:
    message=f"""Time={currentLocalTime} Message=Program Failed, Error message={e}\n"""
    writeLogs(message,logFilePath)
