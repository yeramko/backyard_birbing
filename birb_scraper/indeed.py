import requests
from bs4 import BeautifulSoup

URL = f"https://www.birdscanada.org/apps/checklist/checklist.jsp?lang=EN&region=CAbcgv&regionName=Metro+Vancouver%2C+British+Columbia&month=&week=&dt_day=10&dt_month=4&dt_year=2021"

def get_last_page():
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

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

def extract_jobs():
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")

    photodivs = soup.find_all("div", {"class": "photodiv"})

    birbs = []

    for photodiv in photodivs:
        birbs.append(photodiv.find("p").get_text())
        #birbs.append(photodiv.find("img"))

    return birbs


def get_jobs(anything):
    #last_page = get_last_page()
    jobs = extract_jobs()
    return jobs
