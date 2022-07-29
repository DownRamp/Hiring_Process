#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import customtkinter
from dotenv import load_dotenv
import os
import uuid
from fpdf import FPDF
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ.get("DATABASE_URI"))
mydb = client["hire_api"]
mycol1 = mydb["applicants"]
mycol2 = mydb["jobs"]

id = uuid.uuid4()
company = os.environ.get("company")
email = os.environ.get("email")
company_description = os.environ.get("company_description")
benefits = os.environ.get("benefits")

class Window():
    def __init__(self, main):
        width_val = 200
        self.main = main
        self.win = customtkinter.CTkFrame(master=self.main, corner_radius=15)
        self.win.pack(fill=BOTH, expand =1)
        self.canvas = Canvas(self.win)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # for scrolling
        self.scroll = ttk.Scrollbar(self.win, orient=VERTICAL, command = self.canvas.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand = self.scroll.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        self.frm = customtkinter.CTkFrame(master=self.canvas, corner_radius=15)
        self.canvas.create_window((0,0), window = self.frm, anchor="nw")
        self.label = customtkinter.CTkLabel(master=self.frm, justify=LEFT, text="Enter chapter information")
        self.label.pack(padx=20, pady=20)

        # start of form
        self.entry_title = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Job Title")
        self.entry_title.pack(pady=20, padx=20)

        self.entry_des = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Job Description")
        self.entry_des.pack(pady=20, padx=20)

        self.entry_pay = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter pay")
        self.entry_pay.pack(pady=20, padx=20)

        self.entry_set = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Position travel requirements (Remote, Hybrid, office)")
        self.entry_set.pack(pady=20, padx=20)

        self.entry_tech_req = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Technical skills required (seperate with commas)")
        self.entry_tech_req.pack(pady=20, padx=20)

        self.entry_tech_nice = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Technical skills nice to have (seperate with commas)")
        self.entry_tech_nice.pack(pady=20, padx=20)

        self.entry_years = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Number of years experience")
        self.entry_years.pack(pady=20, padx=20)

        self.entry_personality = customtkinter.CTkEntry(master=self.frm,
                                    width=width_val,
                                    placeholder_text="Enter Personality description")
        self.entry_personality.pack(pady=20, padx=20)

        self.button =customtkinter.CTkButton(master=self.frm, text="Submit", command=lambda: self.enter_values())
        self.button.pack(padx=20, pady=20)

    def enter_values(self):
            self.job = []
            self.job.append(self.entry_title.get())
            self.job.append(company)
            self.job.append(company_description)
            self.job.append(self.entry_des.get())
            self.job.append(self.entry_pay.get())
            self.job.append(self.entry_set.get())
            self.job.append(self.entry_tech_req.get())
            self.job.append(self.entry_tech_nice.get())
            self.job.append(self.entry_years.get())
            self.job.append(self.entry_personality.get())
            self.job.append(benefits)
            self.generate_pdf()
            self.save_id()

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        # create a cells
        for index, i in enumerate(self.job):
            if index%2 == 0:
                pdf.cell(200, 10, txt = i, ln = 1, align = 'L')

            else:
                pdf.cell(200, 10, txt = i,
                         ln = 1, align = 'L')

        # save the pdf with name .pdf
        pdf.output(f"Jobs/{id}.pdf")

    def save_id(self):
        # save id to db somewhere
        jobs ={"id": id, "title": self.entry_title.get(),
        "description":self.entry_des.get(),"pay":self.entry_pay.get(), "setting":self.entry_set.get(), "requirements": self.entry_tech_req.get(),
        "nice":self.entry_tech_nice.get(), "experience":self.entry_years.get(), "personality":self.entry_personality.get()}
        result=mycol2.insert_one(jobs)
        print(result)
        # create folder
        os.mkdir('Resumes/'+id) 

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    root = customtkinter.CTk()
    root.title("Chapter maker")
    root.geometry("300x800")
    Window(root)
    root.mainloop()