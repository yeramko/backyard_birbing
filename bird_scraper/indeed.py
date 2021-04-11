import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://ca.indeed.com/jobs?q=Junior+Developer+-senior%2C+-sr&l=Vancouver%2C+BC&limit={LIMIT}&radius=25"

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

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"======== Scrapping from Indeed: PG: {page} ========")

        r = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

        for result in results:
            job = extract_data(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
