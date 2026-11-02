from datetime import datetime

def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """
    for person in people:
        del person["name"]
        person["birth_year"] = int(person["birthdate"][0:4])
        del person["birthdate"]
        person["city_initial"] = person["city"][0]
        del person["city"]
        
    return people