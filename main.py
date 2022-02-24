import time
import apiCalls
import utils
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] %(message)s')


duration, registrationNumbers = utils.getContentFromYamlFile()
while(True):
    logging.info(f"Total of {len(registrationNumbers)} registration numbers loaded")
    for regNo in registrationNumbers:
        logging.debug(f"Checking registration number {regNo}")
        if regNo['found'] == False:
            regNo['found'] = apiCalls.findVaccineInfo(regNo['name'], regNo['number'])
            utils.printStatus(regNo['found'], regNo['name'])
        else:
            logging.info(f"Already found Vaccine card for {regNo['name']}")
    time.sleep(60*duration)
