from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.environ.get("DATABASE_URI"))
mydb = client["hire_api"]
mycol1 = mydb["applicants"]
mycol2 = mydb["jobs"]

def close(job_id):    
    # get rid of job pdf or store?
    os.rmdir("Jobs/"+job_id)
    myquery = { "job_id": job_id }
    mycol2.delete_one(myquery)

    # go through resumes and reject
    # Turn to reject in db
    myquery = { "job_id": job_id }
    newvalues = { "$set": { "status": 3, "flag": False} }

    mycol1.delete_one(myquery, newvalues)

    # delete resumes on file 
    os.rmdir("Resumes/"+job_id)
