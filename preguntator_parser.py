import pdfplumber

pdf_path = './'+ input('Insert the source input name, without the .pdf:\n')+'.pdf'
txt_path = './'+ input('Insert the target output name, without .txt:\n')+'.txt'

questionDelimiter='.- ' # anything that represents uniquely the question but not the options, in my case it was '1.- '.
optionStartToRemove=[' ','X ']# This represents the start of each option, in my case X marked the correct answer
optionDelimiters = list('abcdefghijklmnopqrstuvwxyz')
optionCounter=0
introductionFinished=False

with pdfplumber.open(pdf_path) as pdf:
    all_text = ''
    for page in pdf.pages:
        for line in page.extract_text().splitlines():
            if questionDelimiter in line:
                all_text+='\n'
                introductionFinished=True
                all_text += '?: '+ line+'\n'
                optionCounter=0
            else:
                if introductionFinished:
                    cleanString=line
                    for start in optionStartToRemove:
                        cleanString=cleanString.replace(start,'')
                    all_text+= optionDelimiters[optionCounter]+ '. ' + cleanString + '\n'
                    optionCounter+=1

with open(txt_path, 'w', encoding='utf-8') as f:
    f.write(all_text)

print(f"Text extracted and saved to {txt_path}")
