import requests
from bs4 import BeautifulSoup



def extract_jobs(URL):
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")

    photodivs = soup.find_all("div", {"class": "photodiv"})

    birbs = []

    for photodiv in photodivs:
        name = photodiv.find("p").get_text()

        image = photodiv.find("img")
        img = image.attrs['src']
        picture = "https://www.birdscanada.org/bscapps/checklist/"+img
        location = "Metro Vancouver, BC"
        birb = {"name": name,
        "picture": picture}
        birbs.append(birb)
        print(birb)

    return birbs


def get_jobs(regionName):
    print(regionName)
    regionName = regionName.lower()
    if regionName == "british columbia":
        regionName = "bc"
    elif regionName == "alberta":
        regionName = "ab"
    elif regionName == "ontario":
        regionName = "on"
    elif regionName == "quebec":
        regionName = "qc"
    elif regionName == "manitoba":
        regionName = "mb"
    elif regionName == "saskatchewan":
        regionName = "sk"
    elif regionName == "yukon":
        regionName = "yk"
    elif regionName == "northwest territories" or "northwest" or "nwt":
        regionName = "nt"
    elif regionName == "nunavut":
        regionName = "nu"
    elif regionName == "nova scotia":
        regionName = "ns"
    elif regionName == "new brunswick":
        regionName = "nb"
    elif regionName == "prince edward island" or "prince edward" or "pei":
        regionName = "pe"
    elif regionName == "newfoundland" or "labrador" or "newfoundland labrador":
        regionName = "nlnf"
    else:
        regionName = regionName

    URL = f"https://www.birdscanada.org/apps/checklist/checklist.jsp?lang=EN&region=CA{regionName}&month=&week=&dt_day=11&dt_month=4&dt_year=2021"

    jobs = extract_jobs(URL)
    return jobs
