import yaml
import logging

def addExtraField(data: dict) -> dict:
    for entry in data:
        entry['found'] = False
    return data


def printStatus(found: bool, name: str) -> None:
    if found:
        logging.info(f"Found Vaccine card for {name}")
    else:
        logging.info(f"Could not find Vaccine card for {name}")


def getContentFromYamlFile() -> tuple[float, dict[str, str]]:
    with open("./config.yaml", 'r') as yamlFile:
        try:
            content = yaml.safe_load(yamlFile)
            logging.info("Yaml file loaded successfully")
            logging.debug("Yaml file loaded successfully, the content is: " + str(content))
        except yaml.YAMLError as exc:
            logging.error("Error in reading yaml file")
            logging.error(exc)
    return content["duration"], addExtraField(content["people"])
