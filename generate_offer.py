def generate(firstname, company, salary, job_title, start_date, hr_name, hr_title, contact_info):
    offer = []
    offer.append("Hello "+firstname)
    offer.append("On behalf of "+company+", I am excited to present an offer of employment for the "+job_title+" position.\n")
    offer.append(" The team was very impressed with your experience and your enthusiasm.\n")
    offer.append(" Your starting salary is "+salary+" Canadian dollars and your start date is "+ start_date+"\n")
    offer.append("For next steps, I'll be sending your employment agreement to you for review and signature via Docusign so it can all be done electronically. Please review the offer and let me know if you have any questions. ")
    offer.append("I look forward to hearing from you and hope to have you join the team!\n")
    offer.append("Thanks,\n")
    offer.append(hr_name)
    offer.append(hr_title)
    offer.append(contact_info)