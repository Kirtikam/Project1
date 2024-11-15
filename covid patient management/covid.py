# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:28:49 2024

@author: Dell
"""

# Covid Patient Information Management System
from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import Calendar, DateEntry
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3


class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS patient_t (id PRIMARYKEY int, firstname text, lastname text, dateOfBirth date,  "
            "gender text, address text, contactNumber text, emailAddress text, covidStatus text, history text, doctor text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, firstname, lastname, dateOfBirth,gender, address, contactNumber, emailAddress, covidStatus, history, doctor):
        self.dbCursor.execute("INSERT INTO patient_t VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        id, firstname, lastname, dateOfBirth,  gender, address, contactNumber, emailAddress, covidStatus, history, doctor))
        self.dbConnection.commit()

    def Update(self, firstname, lastname, dateOfBirth, gender, address, contactNumber, emailAddress, covidStatus, history, doctor, id):
        self.dbCursor.execute(
            "UPDATE patient_t SET firstname = ?, lastname = ?, dateOfBirth = ?, gender = ?, address = ?, contactNumber = ?, emailAddress = ?, covidStatus = ?, history = ?, doctor = ? WHERE id = ?",
            (firstname, lastname, dateOfBirth, gender, address, contactNumber, emailAddress, covidStatus, history, doctor, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM patient_t WHERE id = ?", (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM patient_t WHERE id = ?", (id,))
        tkinter.messagebox.showinfo("Deleted data", "Successfully Deleted the Patient data in the database")
        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute("SELECT * FROM patient_t")
        records = self.dbCursor.fetchall()
        return records

class Database2:
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS vaccine (id PRIMARYKEY int, firstname text, lastname text,age text,bloodgrp text,gender text,dose1 date,dose2 date)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, firstname, lastname,age,bloodgrp,gender,dose1,dose2):
        self.dbCursor.execute("INSERT INTO vaccine VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
        id, firstname, lastname, age, bloodgrp, gender, dose1,dose2))
        self.dbConnection.commit()
    def Display2(self):
        self.dbCursor.execute("SELECT * FROM vaccine")
        records = self.dbCursor.fetchall()
        return records

class Values:
    def Validate(self, id, firstname, lastname, contactNumber, emailAdress):
        if not (id.isdigit() and (len(id) <=3 )):
            return "id"
        elif not (firstname.isalpha()):
            return "firstname"
        elif not (lastname.isalpha()):
            return "lastname"
        elif not (contactNumber.isdigit() and (len(contactNumber) == 10)):
            return "contactNumber"
        elif not (emailAdress.count("@") == 1 and emailAdress.count(".") > 0):
            return "emailAddress"
        else:
            return "SUCCESS"
class Values2:
    def Validate(self, id, firstname, lastname):
        if not (id.isdigit() and (len(id) <=3 )):
            return "id"
        elif not (firstname.isalpha()):
            return "firstname"
        elif not (lastname.isalpha()):
            return "lastname"
        else:
            return "SUCCESS"

class InsertWindow:
    def __init__(self):
        self.window = tkinter.Toplevel()
        self.window.geometry("1200x700")
        self.window.resizable(0,0)
        self.window.wm_title("Insert Patient Data ")
        self.id = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.contactNumber = tkinter.StringVar()
        self.emailAddress = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.doctor = tkinter.StringVar()
        self.genderType = ["Male", "Female", "Transgender", "Other"]
        self.covidStatusList = ["Positive", "Negative"]

        tkinter.Label(self.window, text = "Insert Patient Information",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 220,y = 50)
        tkinter.Label(self.window,  text="Patient Id", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 100)
        tkinter.Label(self.window,   text="Patient First Name", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 150)
        tkinter.Label(self.window,    text="Patient Last Name",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 200)
        tkinter.Label(self.window,  text="Date of Birth", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 250)
      
        tkinter.Label(self.window,  text="Patient Gender",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 300)
        tkinter.Label(self.window, text="Patient Address", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 350)
        tkinter.Label(self.window,  text="Patient Contact Number", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 400)
        tkinter.Label(self.window,  text="Patient Email Address", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 450)
        tkinter.Label(self.window,  text="Covid Status", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 500)
        tkinter.Label(self.window, text="History of Patient",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 550)
        tkinter.Label(self.window,  text="Name of Doctor", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 600)


        self.idEntry = tkinter.Entry(self.window,  textvariable=self.id)
        self.idEntry.place(x = 370,y = 100,width=250,height=30)
        
        self.firstnameEntry = tkinter.Entry(self.window, textvariable=self.firstname)
        self.firstnameEntry.place(x = 370,y = 150,width=250,height=30)
        
        self.lastnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lastname)
        self.lastnameEntry.place(x = 370,y = 200,width=250,height=30)

        self.cal = DateEntry(self.window, width=12,  borderwidth=2)
        self.cal.place(x = 370,y = 250,width=250,height=30)
        
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderType, width=25)
        self.genderBox.place(x = 370,y = 300,width=250,height=30)
        
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.addressEntry.place(x = 370,y = 350,width=250,height=30)
        
        self.contactNumberEntry = tkinter.Entry(self.window, width=25, textvariable=self.contactNumber)
        self.contactNumberEntry .place(x = 370,y = 400,width=250,height=30)
        
        self.emailAddressEntry = tkinter.Entry(self.window, width=25, textvariable=self.emailAddress)
        self.emailAddressEntry.place(x = 370,y = 450,width=250,height=30)

        self.covidStatusBox = tkinter.ttk.Combobox(self.window, values=self.covidStatusList, width=25)
        self.covidStatusBox.place(x = 370,y = 500,width=250,height=30)
        
        self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
        self.historyEntry .place(x = 370,y = 550,width=250,height=30)
        
        self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)
        self.doctorEntry.place(x = 370,y = 600,width=250,height=30)
        tkinter.Button(self.window, fg='black',font='verdana',justify='center',width='20',relief='ridge', text="Insert", command=self.Insert).place(x = 50,y = 650,width=160,height=30)
        tkinter.Button(self.window, fg='black',font='verdana',justify='center',width='20',relief='ridge', text="Reset", command=self.Reset).place(x = 220,y = 650,width=160,height=30)
        tkinter.Button(self.window,fg='black',font='verdana',justify='center',width='20',relief='ridge',text="Close", command=self.window.destroy).place(x = 390,y = 650,width=160,height=30)
        self.window.mainloop()

    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                         self.contactNumberEntry.get(), self.emailAddressEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(), self.cal.get(),
                                 self.genderBox.get(), self.addressEntry.get(),
                                 self.contactNumberEntry.get(), self.emailAddressEntry.get(), self.covidStatusBox.get(),
                                 self.historyEntry.get(), self.doctorEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.firstnameEntry.delete(0, tkinter.END)
        self.lastnameEntry.delete(0, tkinter.END)
        self.dateOfBirthBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.contactNumberEntry.delete(0, tkinter.END)
        self.emailAddressEntry.delete(0, tkinter.END)
        self.covidStatusBox.set("")
        self.historyEntry.delete(0, tkinter.END)
        self.doctorEntry.delete(0, tkinter.END)


class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Toplevel()
        self.window.geometry("1200x700")
        self.window.wm_title("Update data")
        self.window.resizable(0,0)
        self.id = id
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.contactNumber = tkinter.StringVar()
        self.emailAddress = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.doctor = tkinter.StringVar()

        self.genderType = ["Male", "Female", "Transgender", "Other"]
        self.covidStatusList = ["Positive", "Negative"]
        tkinter.Label(self.window, text = "Update Patient Information",justify="center", font="verdana",relief="flat",highlightthickness="0",width="30").place(x = 140,y = 50)
        tkinter.Label(self.window,  text="Patient Id", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 100)
        tkinter.Label(self.window,   text="Patient First Name", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 150)
        tkinter.Label(self.window,    text="Patient Last Name",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 200)
        tkinter.Label(self.window,  text="Date of Birth", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 250)

        tkinter.Label(self.window,  text="Patient Gender",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 300)
        tkinter.Label(self.window, text="Patient Address", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 350)
        tkinter.Label(self.window,  text="Patient Contact Number", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 400)
        tkinter.Label(self.window,  text="Patient Email Address", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 450)
        tkinter.Label(self.window,  text="Covid Status", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 500)
        tkinter.Label(self.window, text="History of Patient",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 550)
        tkinter.Label(self.window,  text="Name of Doctor", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 50,y = 600)

        self.database = Database()
        self.searchResults = self.database.Search(id)

        tkinter.Label(self.window, text=self.searchResults[0][0], width=25).place(x = 370,y = 100,width=250,height=30)
        
        self.firstnameEntry = tkinter.Entry(self.window, textvariable=self.firstname)
        self.firstnameEntry.place(x = 370,y = 150,width=250,height=30)

        self.lastnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lastname)
        self.lastnameEntry.place(x = 370,y = 200,width=250,height=30)

        self.dateOfBirthBox = DateEntry(self.window, width=12,  borderwidth=2)
        self.dateOfBirthBox.place(x = 370,y = 250,width=250,height=30)

        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderType, width=25)
        self.genderBox.place(x = 370,y = 300,width=250,height=30)

        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.addressEntry.place(x = 370,y = 350,width=250,height=30)

        self.contactNumberEntry = tkinter.Entry(self.window, width=25, textvariable=self.contactNumber)
        self.contactNumberEntry .place(x = 370,y = 400,width=250,height=30)

        self.emailAddressEntry = tkinter.Entry(self.window, width=25, textvariable=self.emailAddress)
        self.emailAddressEntry.place(x = 370,y = 450,width=250,height=30)

        self.covidStatusBox = tkinter.ttk.Combobox(self.window, values=self.covidStatusList, width=25)
        self.covidStatusBox.place(x = 370,y = 500,width=250,height=30)

        self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
        self.historyEntry .place(x = 370,y = 550,width=250,height=30)

        self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)
        self.doctorEntry.place(x = 370,y = 600,width=250,height=30)

        tkinter.Button(self.window, fg='black',font='verdana',justify='center',width='20',relief='ridge', text="Update",command=self.Update).place(x = 50,y = 650,width=160,height=30)
        tkinter.Button(self.window, fg='black',font='verdana',justify='center',width='20',relief='ridge', text="Reset",command=self.Reset).place(x = 220,y = 650,width=160,height=30)

        tkinter.Button(self.window, fg='black',font='verdana',justify='center',width='20',relief='ridge', text="Exit",command=self.window.destroy).place(x = 390,y = 650,width=160,height=30)
        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.firstnameEntry.get(), self.lastnameEntry.get(), self.dateOfBirthBox.get(),self.genderBox.get(), self.addressEntry.get(), self.contactNumberEntry.get(),
                             self.emailAddressEntry.get(), self.covidStatusBox.get(), self.historyEntry.get(),
                             self.doctorEntry.get(), self.id)
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.firstnameEntry.delete(0, tkinter.END)
        self.lastnameEntry.delete(0, tkinter.END)
        self.dateOfBirthBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.contactNumberEntry.delete(0, tkinter.END)
        self.emailAddressEntry.delete(0, tkinter.END)
        self.covidStatusBox.set("")
        self.historyEntry.delete(0, tkinter.END)
        self.doctorEntry.delete(0, tkinter.END)


class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")
        self.databaseViewWindow.resizable(0,0)
     
        tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "id", "firstname", "lastname", "dateOfBirth",  "gender", "address", "contactNumber", "emailAddress", "covidStatus", "history",
        "doctor")
        self.databaseView.heading("id", text="Patient ID")
        self.databaseView.heading("firstname", text="First Name")
        self.databaseView.heading("lastname", text="Last Name")
        self.databaseView.heading("dateOfBirth", text="Date of Birth")
        
        self.databaseView.heading("gender", text="Gender")
        self.databaseView.heading("address", text="Home Address")
        self.databaseView.heading("contactNumber", text="Contact Number")
        self.databaseView.heading("emailAddress", text="Email Address")
        self.databaseView.heading("covidStatus", text="Covid Status")
        self.databaseView.heading("history", text="History")
        self.databaseView.heading("doctor", text="Doctor")

        self.databaseView.column("id", width=100)
        self.databaseView.column("firstname", width=100)
        self.databaseView.column("lastname", width=100)
        self.databaseView.column("dateOfBirth", width=100)
        
        self.databaseView.column("gender", width=100)
        self.databaseView.column("address", width=200)
        self.databaseView.column("contactNumber", width=100)
        self.databaseView.column("emailAddress", width=200)
        self.databaseView.column("covidStatus", width=100)
        self.databaseView.column("history", width=100)
        self.databaseView.column("doctor", width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class SearchDeleteWindow:
    def __init__(self, task):
        self.window = tkinter.Toplevel()
        self.window.wm_title(task + " data")
        self.window.geometry("500x300")
        self.window.resizable(0,0)
        self.id = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.heading = "Please enter Patient ID to " + task

        tkinter.Label(self.window, text=self.heading, justify="center", font="verdana",relief="flat",highlightthickness="0",width="30").place(x=50, y=50)
        tkinter.Label(self.window, text="Patient ID", justify="center", font="verdana",relief="flat",highlightthickness="0",width="10").place(x=120, y=100)

        self.idEntry = tkinter.Entry(self.window, textvariable=self.id)
        self.idEntry.place(x=270,y=100,width=100,height=30)


        if (task == "Search"):
            tkinter.Button(self.window, text=task, fg='black',font='verdana',justify='center',width='15',relief='ridge',command=self.Search).place(x=145, y=160)
        elif (task == "Delete"):
            tkinter.Button(self.window, text=task, fg='black',font='verdana',justify='center',width='15',relief='ridge',command=self.Delete).place(x=145, y=160)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())


class VaccineWindow:
    def __init__(self):
        self.window = tkinter.Toplevel()
        self.window.geometry("1200x600")
        self.window.resizable(0, 0)
        self.window.wm_title("Vaccination Details ")
        self.id = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.age = tkinter.StringVar()
        self.genderType = ["Male", "Female", "Transgender", "Other"]
        self.bloodListType = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        tkinter.Label(self.window, text="Vaccination Details", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=220, y=50)
        tkinter.Label(self.window, text="Patient Id", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=100)
        tkinter.Label(self.window, text="Patient First Name", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=150)
        tkinter.Label(self.window, text="Patient Last Name", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=200)
        tkinter.Label(self.window, text="Patient Age", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=250)
        tkinter.Label(self.window, text="Patient Blood Group", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=300)
        tkinter.Label(self.window, text="Patient Gender", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=350)
        tkinter.Label(self.window, text="1st Dose", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=400)
        tkinter.Label(self.window, text="2nd Dose", justify="center", font="verdana", relief="flat",
                      highlightthickness="0", width="20").place(x=50, y=450)

        self.idEntry = tkinter.Entry(self.window, textvariable=self.id)
        self.idEntry.place(x=370, y=100, width=250, height=30)

        self.firstnameEntry = tkinter.Entry(self.window, textvariable=self.firstname)
        self.firstnameEntry.place(x=370, y=150, width=250, height=30)

        self.lastnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lastname)
        self.lastnameEntry.place(x=370, y=200, width=250, height=30)

        self.ageEntry = tkinter.Entry(self.window, width=25, textvariable=self.age)
        self.ageEntry.place(x=370, y=250, width=250, height=30)

        self.bloodgrpBox = tkinter.ttk.Combobox(self.window, values=self.bloodListType, width=25)
        self.bloodgrpBox.place(x=370, y=300, width=250, height=30)

        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderType, width=25)
        self.genderBox.place(x=370, y=350, width=250, height=30)

        self.dose1 = DateEntry(self.window, width=12, borderwidth=2)
        self.dose1.place(x=370, y=400, width=250, height=30)

        self.dose2 = DateEntry(self.window, width=12, borderwidth=2)
        self.dose2.place(x=370, y=450, width=250, height=30)

        tkinter.Button(self.window, fg='black', font='verdana', justify='center', width='20', relief='ridge',
                       text="Insert", command=self.Insert).place(x=50, y=520, width=160, height=30)
        tkinter.Button(self.window, fg='black', font='verdana', justify='center', width='20', relief='ridge',
                       text="Reset", command=self.Reset).place(x=220, y=520, width=160, height=30)
        tkinter.Button(self.window, fg='black', font='verdana', justify='center', width='20', relief='ridge',
                       text="Close", command=self.window.destroy).place(x=390, y=520, width=160, height=30)
        self.window.mainloop()

    def Insert(self):
        self.values = Values2()
        self.database = Database2()
        self.test = self.values.Validate(self.idEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.firstnameEntry.get(), self.lastnameEntry.get(),
                                 self.ageEntry.get(), self.bloodgrpBox.get(),
                                 self.genderBox.get(), self.dose1.get(), self.dose2.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.firstnameEntry.delete(0, tkinter.END)
        self.lastnameEntry.delete(0, tkinter.END)
        self.ageEntry.delete(0, tkinter.END)
        self.bloodgrpBox.set("")
        self.genderBox.set("")
        self.dose1.set("")
        self.dose2.set("")
        
        
class Database2View:
    def __init__(self, data):
        self.database2ViewWindow = tkinter.Tk()
        self.database2ViewWindow.wm_title("Database View")
        self.database2ViewWindow.resizable(0,0)
       
        tkinter.Label(self.database2ViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

        self.database2View = tkinter.ttk.Treeview(self.database2ViewWindow)
        self.database2View.grid(pady=5, column=1, row=2)
        self.database2View["show"] = "headings"
        self.database2View["columns"] = (
        "id", "firstname", "lastname", "age", "bloodgrp" ,"gender", "dose1", "dose2")

        self.database2View.heading("id", text="Patient ID")
        self.database2View.heading("firstname", text="First Name")
        self.database2View.heading("lastname", text="Last Name")
        self.database2View.heading("age", text="Age")
        self.database2View.heading("bloodgrp",text="Blood Group")
        self.database2View.heading("gender", text="Gender")
        self.database2View.heading("dose1", text="1st Dose")
        self.database2View.heading("dose2", text="2nd Dose")
        
        self.database2View.column("id", width=100)
        self.database2View.column("firstname", width=100)
        self.database2View.column("lastname", width=100)
        self.database2View.column("age", width=100)
        self.database2View.column("bloodgrp", width=100)
        self.database2View.column("gender", width=100)
        self.database2View.column("dose1", width=100)
        self.database2View.column("dose2", width=100)

        for record in data:
            self.database2View.insert('', 'end', values=(record))

        self.database2ViewWindow.mainloop()

class HomePage:
    def __init__(self):
        self.homePageWindow=tkinter.Toplevel()
        self.homePageWindow.geometry("1000x600")
        self.homePageWindow.resizable(0,0)
        self.homePageWindow.title('Patient Information Management System')
        t1 = Label(self.homePageWindow, text = "Select Operation",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 170,y = 100)
        tkinter.Button(self.homePageWindow,    text="Insert",fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.Insert).place(x = 170,y = 150)
        tkinter.Button(self.homePageWindow,   text="Update", fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.Update).place(x = 170,y = 200)
        tkinter.Button(self.homePageWindow,  text="Search", fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.Search).place(x = 170,y = 250)
        tkinter.Button(self.homePageWindow,   text="Delete", fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.Delete).place(x = 170,y = 300)
        tkinter.Button(self.homePageWindow,   text="Display", fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.Display).place(x = 170,y = 350)
        tkinter.Button(self.homePageWindow,   text="Vaccination", fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.Vaccine).place(x = 170,y = 400)                                                                                           
        tkinter.Button(self.homePageWindow,   text="Exit", fg='black',font='verdana',justify='center',width='20',relief='ridge', command=self.homePageWindow.destroy).place(x = 170,y = 450)
        self.homePageWindow.mainloop()

    def Insert(self):
        self.insertWindow = InsertWindow()
    def Update(self):
        self.updateIDWindow = tkinter.Toplevel()
        self.updateIDWindow.wm_title("Update data")
        self.updateIDWindow.geometry("500x300")
        self.updateIDWindow.resizable(0,0)
        self.id = tkinter.StringVar()
        tkinter.Label(self.updateIDWindow, text="UPDATE DATA", justify="center", font="verdana",relief="flat",highlightthickness="0",width="30").place(x=50, y=50)
        tkinter.Label(self.updateIDWindow, text="Enter the ID to update: ", justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x=50, y=100)
        self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id,)
        self.idEntry.place(x=340,y=100,width=100,height=30)
        tkinter.Button(self.updateIDWindow, text="Update", fg='black',font='verdana',justify='center',width='15',relief='ridge',command=self.updateID).place(x=145,y=160)
        self.updateIDWindow.mainloop()
      

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):

        self.deleteWindow = SearchDeleteWindow("Delete")


    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)
    def Vaccine(self):
        self.vaccinewindow=VaccineWindow()


class Mainpage:
    def __init__(self):
        self.mainwindow=tkinter.Tk()
      
        self.mainwindow.title('Covid Patient Information Management System')
        self.mainwindow.geometry("600x600")
        self.mainwindow.resizable(0,0)
        photo = Image.open("hospital.png")
        image= ImageTk.PhotoImage(image=photo)
        w = Label(self.mainwindow, image=image)
        w.pack()
        pat_info=Button(self.mainwindow, text="Covid Patients Information Management System", fg='black',font='verdana',justify='center',width='40',relief='ridge')
        pat_info.place(x=40, y=100)
        pat_info = Button(self.mainwindow, text="View Covid Patients", fg='black',font='verdana', justify='center', width='20', relief='ridge', command=self.Display)
        pat_info.place(x=150, y=250)
        vacc_info=Button(self.mainwindow, text="View Vaccinated Patients", fg='black',font='verdana',justify='center',width='20',relief='ridge',command=self.Display2)
        vacc_info.place(x=150, y=300)
        doc=Button(self.mainwindow, text="Add Patients Data", fg='black',font='verdana',justify='center',width='20',relief='ridge',command=self.Passwin)
        doc.place(x=150, y=350)
        self.mainwindow.mainloop()
    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)

    def Display2(self):
        self.database = Database2()
        self.data = self.database.Display2()
        self.display2Window = Database2View(self.data)
        
    def Passwin(self):
        self.passwindow=tkinter.Toplevel()
        self.passwindow.title('Password')
        self.passwindow.geometry("300x300")
        self.p="1234"
        l=Label(self.passwindow, text = "Enter Password",justify="center", font="verdana",relief="flat",highlightthickness="0",width="20").place(x = 20,y = 50)
        self.passEntry = tkinter.Entry(self.passwindow, width=5)
        self.passEntry.place(x=100,y=100,width=100,height=30)
        sub=Button(self.passwindow, text="Submit", fg='black',font='verdana',justify='center',width='10',relief='ridge',command=self.HomePage).place(x=75,y=150)
    def HomePage(self):
        if self.passEntry.get()=="1234" :
            self.homepage=HomePage()
        else:
            tkinter.messagebox.showinfo(" ","Incorrect Password")
        
    
mp = Mainpage()




