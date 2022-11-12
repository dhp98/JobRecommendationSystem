# Saved file for each job url
JOBS_LINKS_JSON_FILE = r'./data/linkedin_jobs_links.json'
# Saved file for each job info
JOBS_INFO_JSON_FILE = r'./data/linkedin_jobs_info.json'
# Saved file for recommended jobs
RECOMMENDED_JOBS_FILE = r'./data/recommended_jobs'
# Path to webdriver exe
WEBDRIVER_PATH = r'/Users/dhyeypandya/TIS/JobRecommendationSystem/chromedriver'
# Cities to search: 6 largest Canadian cities
JOB_LOCATIONS = ['California,CA', 'Toronto,ON', 'Montréal,QC', 'Ottawa,ON', 'Calgary,AB', 'Edmonton,AB']
# Seach "data scientist" OR "data+engineer" OR "data+analyst" with quotation marks
JOB_SEARCH_WORDS = '"software engineer"+OR+"data scientist"+OR+"software developer"'
# To avoid same job posted multiple times, we only look back for 30 days
DAY_RANGE = 30
# Path to sample resume
SAMPLE_RESUME_PDF = r'./data/PWang_resume.pdf'