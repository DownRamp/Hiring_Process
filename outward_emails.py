import pysondb


def success():
    success = db.getDb("pass.json")
    success_list = success.getAll()

    for applicant in success_list:
        # First round Success
        if applicant.status == 0 and applicant.flag:
            message = "Hello, We had a look at your resume and we are excited to get to know more about you. In a few moments we will be sending you a take home test to see if you can get to the next round of interviews. Thank you and all the best."
            applicant.status+=1
            applicant.flag = False
        # Second round Success
        elif applicant.status == 1 and applicant.flag:
            message = "Hello, We have reviewed your take home test and we were interested in seeing more of you. Please select a time when you can meet with our engineering team for the next round of interviews."
            applicant.status+=1
            applicant.flag = False
        # Third round Success
        elif applicant.status == 2 and applicant.flag:
            message = "Hello, We had a great chat and would like to offer you a job here."
            applicant.status+=1
            applicant.flag = False

    #success.deleteAll()

def rejection():
    reject = db.getDb("reject.json")
    reject_list = reject.getAll()

    for applicant in reject_list:
        # First round rejects
        if applicant.status == 0:
            message = "Thank you for applying but we will not be moving forward with your application at this time."

        # Second round rejects
        elif applicant.status == 1:
            message = "Thank you for applying but the engineers did not feel that your skills where what we were looking for you."

        # Third round rejects
        elif applicant.status == 2:
            message = "Thank you for all your time and effort but we will not be moving forward with your application. We wish you all the best in your future."

        # Job has been filled
        elif applicant.status == 3:
            message = "Thank you for applying but the position has already been filled."

    reject.deleteAll()

def email(body,email):
    pass

def generate(firstname, company, salary, job_title, start_date, hr_name, hr_title, contact_info):
    offer = []
    offer.append("Hello "+firstname)
    offer.append("On behalf of "+company+", I am excited to present an offer of employment for the "+job_title+" position.\n")
    offer.append(" The team was very impressed with your experience and your enthusiasm.\n")
    offer.append(" Your starting salary is "+salary+" in Canadian dollars and your start date is "+ start_date+"\n")
    offer.append("For next steps, I'll be sending your employment agreement to you for review and signature via Docusign so it can all be done electronically. Please review the offer and let me know if you have any questions. ")
    offer.append("I look forward to hearing from you and hope to have you join the team!\n")
    offer.append("Thanks,\n")
    offer.append(hr_name)
    offer.append(hr_title)
    offer.append(contact_info)

def run():
    success()
    rejection()

