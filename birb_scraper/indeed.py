import requests
from bs4 import BeautifulSoup



def extract_data(html):

    title = html.find("h2", {"class":"title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            target_text = company_anchor
        else:
            target_text = company

        company = str(target_text.string).strip()
    else:
        company = None

    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {
        'title': title, 
        'company': company, 
        'location': location,
        'link': f"https://ca.indeed.com/viewjob?jk={job_id}"
        }

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
        "picture": picture,
        "location": location}
        birbs.append(birb)
        print(birb)

    return birbs


def get_jobs(regionName):

    if regionName:
        regionName = regionName.lower()
        if regionName == "british columbia":
            regionName = "bc"
        if regionName == "alberta":
            regionName = "ab"
        if regionName == "ontario":
            regionName = "on"
        if regionName == "quebec":
            regionName = "qc"
        if regionName == "manitoba":
            regionName = "mb"
        if regionName == "saskatchewan":
            regionName = "sk"
        if regionName == "yukon":
            regionName = "yk"
        if regionName == "northwest territories" or "northwest" or "nwt":
            regionName = "nt"
        if regionName == "nunavut":
            regionName = "nu"
        if regionName == "nova scotia":
            regionName = "ns"
        if regionName == "new brunswick":
            regionName = "nb"
        if regionName == "prince edward island" or "prince edward" or "pei":
            regionName = "pe"
        if regionName == "newfoundland" or "labrador" or "newfoundland labrador":
            regionName = "nlnf"
        else:
            regionName = regionName


    URL = f"https://www.birdscanada.org/apps/checklist/checklist.jsp?lang=EN&region=CA{regionName}&month=&week=&dt_day=11&dt_month=4&dt_year=2021"

    jobs = extract_jobs(URL)
    return jobs
