# importing required modules
import PyPDF2
import pysondb
from dotenv import load_dotenv

load_dotenv()

difficulty = os.environ.get("difficulty")

# fetch job posting and grab requirments and nice to haves
# add up the max total
# 2 points for reqs and 1 point for nice to have 7/10 is the total threshold

def walkthrough():
    # search through all files in Resumes
    # send to be filtered
    pass

def filter(id, path):
    score = 0
    # creating a pdf file object
    pdfFileObj = open(path, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    print(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()

    if score > difficulty:
        passed(id, email)
    else:
        reject(id, email)

# Flags (0-open but didn't pass, 1-Failed test, 2-Failed last interview, 3- Position filled)

def reject(id, email):
    # write name to reject list
    reject=db.getDb("reject.json")
    reject.add({"job_id": id, "email": email, "status": 0})

def passed(id, email):
    passed=db.getDb("pass.json")
    passed.add({"job_id": id, "email": email, "status":0, "flag": True})