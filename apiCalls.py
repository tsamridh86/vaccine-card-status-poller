import requests
from plyer import notification

def checkOnline(regNo: str) -> bool:
  url = f"https://vaccine.mohp.gov.np/api/verify-public-search?reg_no={regNo}"
  response = requests.get(url)
  data = response.json()
  try:
    return data['is_verified'] == 1
  except:
    return False



def findVaccineInfo(name: str, regNo : str ) -> bool:
  foundVaccineInfo = checkOnline(regNo) 
  if foundVaccineInfo:
    notification.notify(
    title = f'Vaccine Card Data found for {name}',
    message = f"Vaccine Card Data found for {name}, check the website for more details",
    app_icon = None,
    timeout = 10,
    )
  return foundVaccineInfo