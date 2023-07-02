import os
from docxtpl import DocxTemplate

#setup directory and variable info
PATH = '/Users/emir/gitrepo/public/python/data_programs/cover_letter_generator/'
company_name = input("Enter name of the Company : ").title()
position_name = input("Enter name of the Position: ").title()

#setup variables to be replaced
context = { 
           'company_name' : company_name, 
           'position_name' : position_name
           }

#open cover letter
doc = DocxTemplate(f"{PATH}Emir_Gonul-CoverLetter.docx")
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
doc.save(f'{PATH}letters/{company_name}/Emir_Gonul_'+company_name+'_'+position_name+'.docx')

#verify file and print results
success = os.path.exists(f'{PATH}letters/{company_name}/Emir_Gonul_'+company_name+'_'+position_name+'.docx')
if success:
   print(f'{company_name}/Emir_Gonul_'+company_name+'_'+position_name+'.docx created!')