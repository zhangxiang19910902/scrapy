

import pdfplumber



with pdfplumber.open(r'C:\Users\Administrator\Desktop\OGP20230100799_Samedzade+.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()#提取文本
        print(text)
        print('\n')