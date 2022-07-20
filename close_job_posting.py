from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ.get("mongo_url"))
db = client.hire
# Delete job posting id folder
# Move all current resumes to reject

def search(dirName):
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return listOfFiles

def close(job_id):
    os.rmdir("Jobs/"+job_id)
    # go through resumes and reject
    db.hire.deleteOne( { id: job_id } )
    list_files = search("Resumes/"+job_id)
    for file in list_files:
        continue
        # Turn to reject
    os.rmdir("Resumes/"+job_id)
