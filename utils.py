import yaml


def addExtraField(data: dict) -> dict:
    for entry in data:
        entry['found'] = False
    return data


def printStatus(found: bool, name: str) -> None:
    if found:
        print(f"Found Vaccine card for {name}")
    else:
        print(f"Could not find Vaccine card for {name}")


def getContentFromYamlFile() -> tuple[float, dict[str, str]]:
    with open("./config.yaml", 'r') as yamlFile:
        try:
            content = yaml.safe_load(yamlFile)
        except yaml.YAMLError as exc:
            print("Error in reading yaml file")
            print(exc)
    return content["duration"], addExtraField(content["people"])
