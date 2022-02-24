import requests
from plyer import notification
import logging

def checkOnline(regNo: str) -> bool:
    logging.debug("Checking online for registration number: " + regNo)
    url = f"https://vaccine.mohp.gov.np/api/verify-public-search?reg_no={regNo}"
    response = requests.get(url)
    data = response.json()
    logging.debug("Response from server: " + str(data))
    try:
        logging.debug("Data found for registration number: " + regNo)
        return data['is_verified'] == 1
    except:
        logging.debug("No data found for registration number: " + regNo)
        return False


def findVaccineInfo(name: str, regNo: str) -> bool:
    foundVaccineInfo = checkOnline(regNo)
    if foundVaccineInfo:
        logging.debug("Notifying user about Vaccine card found")
        notification.notify(
            title=f'Vaccine Card Data found for {name}',
            message=f"Vaccine Card Data found for {name}, check the website for more details",
            app_icon=None,
            timeout=10,
        )
    return foundVaccineInfo
