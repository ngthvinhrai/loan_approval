from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler

def decision():

    if home_ownership_entry.get() in ['OWN', 'OTHER']:
        result_label.config(text="NOT APPROVED!")
    else:
        ndf = new_df.copy()
        
        ndf.loc[0, 'person_age'] = int(age_entry.get())
        ndf.loc[0, 'person_income'] = int(income_entry.get())
        ndf.loc[0, 'person_emp_length'] = float(experience_entry.get())
        ndf.loc[0, 'loan_amnt'] = int(loan_amount_entry.get())
        ndf.loc[0, 'loan_int_rate'] = float(interest_rate_entry.get())
        ndf.loc[0, 'loan_percent_income'] = int(loan_amount_entry.get())/int(income_entry.get())
        ndf.loc[0, 'cb_person_cred_hist_length'] = int(credit_history_entry.get())
        ndf.loc[0, f'person_home_ownership_{home_ownership_entry.get()}'] = 1 
        ndf.loc[0, f'loan_intent_{purpose_entry.get()}'] = 1
        ndf.loc[0, f'loan_grade_{grade_entry.get()}'] = 1
        ndf.loc[0, f'cb_person_default_on_file_{loan_defaults_entry.get()}'] = 1
        ndf = ndf.replace(np.nan, 0)

        ndf[['person_income', 'loan_amnt']] = scaler.transform(ndf[['person_income', 'loan_amnt']])
        
        if model.predict(ndf) == 1: result_label.config(text="APPROVED!")
        else: result_label.config(text="NOT APPROVED!")




    # result_label.config(text=f"Monthly Payment: ${age_entry.get()}")

df = pd.read_csv('Loan_Approval.csv')
df = df.drop(columns=['id', 'loan_status', 'person_home_ownership', 'loan_intent', 'loan_grade', 'cb_person_default_on_file'])

new_df = pd.DataFrame(columns=df.columns)
new_df['person_home_ownership_MORTGAGE'] = 0
new_df['person_home_ownership_RENT'] = 0
new_df['loan_intent_DEBTCONSOLIDATION'] = 0
new_df['loan_intent_EDUCATION'] = 0
new_df['loan_intent_HOMEIMPROVEMENT'] = 0
new_df['loan_intent_MEDICAL'] = 0
new_df['loan_intent_PERSONAL'] = 0
new_df['loan_intent_VENTURE'] = 0
new_df['loan_grade_A'] = 0
new_df['loan_grade_B'] = 0
new_df['loan_grade_C'] = 0
new_df['loan_grade_D'] = 0
new_df['loan_grade_E'] = 0
new_df['loan_grade_F'] = 0
new_df['loan_grade_G'] = 0
new_df['cb_person_default_on_file_N'] = 0
new_df['cb_person_default_on_file_Y'] = 0

scaler = joblib.load('scaler.save')
model = joblib.load('model_rbf_100.pkl')



window = Tk()
window.title("Loan Application")


age_label = Label(window, text="Age:")
age_entry = Entry(window)

income_label = Label(window, text="Annual Income:")
income_entry = Entry(window)

home_ownership_label = Label(window, text="Home Ownership")
home_ownership_entry = ttk.Combobox(window, values=["RENT", "OWN", "MORTGAGE", "OTHER"])

experience_label = Label(window, text="Years of Employment:")
experience_entry = Entry(window)

purpose_label = Label(window, text="Purpose")
purpose_entry = ttk.Combobox(window, values=["EDUCATION", "MEDICAL", "PERSONAL", "VENTURE", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"])

grade_label = Label(window, text="Grade")
grade_entry = ttk.Combobox(window, values=["A", "B", "C", "D", "E", "F", "G"])

loan_amount_label = Label(window, text="Loan Amount:")
loan_amount_entry = Entry(window)

interest_rate_label = Label(window, text="Interest Rate (%):")
interest_rate_entry = Entry(window)

loan_defaults_label = Label(window, text="Loan Defaults")
loan_defaults_entry = ttk.Combobox(window, values=["N", "Y"])

credit_history_label = Label(window, text="Credit History:")
credit_history_entry = Entry(window)


calculate_button = Button(window, text="Submit", command=decision)

result_label = Label(window, text="")

age_label.grid(row=0, column=0)
age_entry.grid(row=0, column=1)

income_label.grid(row=1, column=0)
income_entry.grid(row=1, column=1)

home_ownership_label.grid(row=2, column=0)
home_ownership_entry.grid(row=2, column=1)

experience_label.grid(row=3, column=0)
experience_entry.grid(row=3, column=1)

purpose_label.grid(row=4, column=0)
purpose_entry.grid(row=4, column=1)

grade_label.grid(row=5, column=0)
grade_entry.grid(row=5, column=1)

loan_amount_label.grid(row=6, column=0)
loan_amount_entry.grid(row=6, column=1)

interest_rate_label.grid(row=7, column=0)
interest_rate_entry.grid(row=7, column=1)

loan_defaults_label.grid(row=8, column=0)
loan_defaults_entry.grid(row=8, column=1)

credit_history_label.grid(row=9, column=0)
credit_history_entry.grid(row=9, column=1)

calculate_button.grid(row=10, column=1)

result_label.grid(row=11, column=1)

window.mainloop()