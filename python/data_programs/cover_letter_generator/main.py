import os
import pandas as pd
from datetime import date
from docxtpl import DocxTemplate
#TODO: create functions

#setup directory and variable info
PATH = '/Users/emir/gitrepo/public/python/data_programs/cover_letter_generator/'
company_name = input("Enter name of the Company : ").title()
position_name = input("Enter name of the Position: ").title()

#setup variables to be replaced
context = { 
           'company_name' : company_name, 
           'position_name' : position_name
           }

#setup which name & file
first_name = input('legal or short name?\n l for legal, s for short\n:').lower()
if first_name == 'l':
   name = 'Emirhan_Gonul'
else:
   name = "Emir_Gonul"

#open cover letter
doc = DocxTemplate(f"{PATH}{name}-CoverLetter.docx")
#Load up data
doc.render(context)

#check if a folder for company exists
new_path = f'{PATH}letters/{company_name}'
isExist = os.path.exists(new_path)
#if folder doesnt exist create it 
if not isExist:
   # Create a new directory for the company
   os.makedirs(new_path)
   print(f"{company_name} directory is created!")

# Save the file with personalized filename
doc.save(f'{PATH}letters/{company_name}/{name}_'+company_name+'_'+position_name+'.docx')

#verify file and print results
success = os.path.exists(f'{PATH}letters/{company_name}/{name}_'+company_name+'_'+position_name+'.docx')
if success:
   print(f'{company_name}/{name}_'+company_name+'_'+position_name+'.docx created!')

#create dict for csv file
today = str(date.today())
data = {
   'Date': [today],
   'Name': [company_name],
   'Position': [position_name],
   'Email': [name]   
}
#create data frame, #record entry to csv
df = pd.DataFrame(data)
df.to_excel('/Users/emir/Desktop/app_list.csv', mode='a', index=False, header=False) 
# print message
print("Data appended successfully.")