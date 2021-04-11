from indeed import get_jobs as get_birbs
from sof import get_jobs as get_sof_jobs
from save import save_to_file

sof_jobs = get_sof_jobs()
indeed_jobs = get_birbs()

jobs = sof_jobs + indeed_jobs

save_to_file(jobs)

tot_jobs = len(indeed_jobs)
print(f"Scraper Done! Scraped {tot_jobs} jobs. Great job, Jason!")