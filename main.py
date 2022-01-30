import requests
import time
from datetime import datetime
import yaml
from plyer import notification
	

def checkOnline(regNo):
  url = f"https://vaccine.mohp.gov.np/api/verify-public-search?reg_no={regNo}"
  response = requests.get(url)
  data = response.json()
  try:
    return data['is_verified'] == 1
  except:
    return False
  

def getContentFromYamlFile():
  with open("./config.yaml", 'r') as yamlFile:
    try:
      content = yaml.safe_load(yamlFile)
    except yaml.YAMLError as exc:
      print("Error in reading yaml file")
      print(exc)
  return content["duration"], content["people"]


def findVaccineInfo(name, regNo):
  foundVaccineInfo = checkOnline(regNo)
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  if foundVaccineInfo:
    notification.notify(
    title = f'Vaccine Card Data found for {name}',
    message = f"Vaccine Data found on {dt_string} for {name}",
    app_icon = None,
    timeout = 10,
    )
    return (f"Vaccine Data found on {dt_string} for {name}")   
  else:
    return (f"Vaccine Data not found on {dt_string} for {name}")

while(True):
  duration, registrationNumbers = getContentFromYamlFile()
  print(f"Total of {len(registrationNumbers)} registration numbers loaded")
  for regNo in registrationNumbers:
    print(findVaccineInfo(regNo['name'], regNo['number']))
  time.sleep(60*duration)