import os
import sys
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu

os.chdir(sys.path[0])

doc = DocxTemplate('template.docx')

placeholder_1 = InlineImage(doc, 'src/image_1.jpg', Cm(5))
placeholder_2 = InlineImage(doc, 'src/image_2.jpg', Cm(5))

context = {
    'name': 'Joel',
    'placeholder_1': placeholder_1,
    'placeholder_2': placeholder_2
}

doc.render(context)
doc.save('output_1.docx')
