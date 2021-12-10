import win32com.client as win32
import os


def convert_to_pdf(doc):
    """Convert given word document to pdf"""
    word = win32.DispatchEx("Word.Application")
    new_name = doc.replace(".docx", r".pdf")
    worddoc = word.Documents.Open(doc)
    worddoc.SaveAs(new_name, FileFormat=17)
    worddoc.Close()
    return None


# path_to_word_document = os.path.join(os.getcwd(),
#                                      'report_1.docx')
convert_to_pdf(
    r'C:\Users\joel_\OneDrive\Documentos\GitHub\1.__Dustin__\15. python-docx and docxtpl\report_1.docx')
