import time
import apiCalls
import utils


duration, registrationNumbers = utils.getContentFromYamlFile()
while(True):
    print(f"Total of {len(registrationNumbers)} registration numbers loaded")
    for regNo in registrationNumbers:
        if regNo['found'] == False:
            regNo['found'] = apiCalls.findVaccineInfo(
                regNo['name'], regNo['number'])
            utils.printStatus(regNo['found'], regNo['name'])
    time.sleep(60*duration)
