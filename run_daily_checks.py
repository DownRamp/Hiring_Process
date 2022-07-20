import filter_resume
import fetch_resumes_email
import outward_emails

# add script to move people the next phase
# user will create a list of approved applicants to move forward
# change flag to true for those applicants

# fetch resumes if exists
fetch_resumes_email.read_email_from_gmail()

# filter resumes if exists
filter_resume.walkthrough()

# send out emails
outward_emails.run()
