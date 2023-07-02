#pip install docxtpl
from docxtpl import DocxTemplate

company_name = input("Enter name of the Company : ")
position_name = input("Enter name of the Position: ")

context = { 
           'company_name' : company_name, 
           'position_name' : position_name
           }

# Open our master template
doc = DocxTemplate("/Users/emir/gitrepo/public/python/data_programs/cover_letter_generator/Emir_Gonul-CoverLetter.docx")
print(doc)
# Load them up
doc.render(context)
# Save the file with personalized filename
doc.save('/Users/emir/gitrepo/public/python/data_programs/cover_letter_generator/test.docx')