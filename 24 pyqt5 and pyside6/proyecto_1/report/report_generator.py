from pathlib import Path
import datetime
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "template.docx"
doc = DocxTemplate(document_path)

name = "Joel"
last_name = "Barrantes"
email = "joelbarrantes@gmail.com"
password = "yolopan13"
date_time = datetime.datetime.today()
today = date_time.strftime("%Y_%m_%d")

context = {
    "NAME": name,
    "LAST_NAME": last_name,
    "EMAIL": email,
    "PASSWORD": password,
    "DATE_TIME": date_time.strftime("%Y-%m-%d")
}


doc.render(context)
doc.save(Path(__file__).parent / f"contract_{today}.docx")
