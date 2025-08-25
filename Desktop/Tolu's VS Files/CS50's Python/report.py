# Dictionaries.
def main():
    spacecraft = {"name":"Voyager 1", "distance":"163"}
    print (create_report(spacecraft))
def create_report(spacecraft):
    return f""" 
    ========= REPORT =========
    name: {spacecraft["name"]}
    distance: {spacecraft["distance"]} AU
    ==========================
    """