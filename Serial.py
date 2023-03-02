from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PyPDF2 import PdfMerger
from os import path


pdf_merger = PdfMerger()
serialnumber = 1001
pagesrequired = 10
z= 0
print(serialnumber)
print(type(serialnumber))

def lable(i):
    # img = Image.open('Logbook_Template.png')
    # global serialnumber
    # textis = fr"AA-{serialnumber}"
    # I1 = ImageDraw.Draw(img)
    # fnt = ImageFont.truetype('consolas.ttf', 82)
    # I1.text((35, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I2 = ImageDraw.Draw(img)
    # I2.text((450, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I3 = ImageDraw.Draw(img)
    # I3.text((855, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I4 = ImageDraw.Draw(img)
    # I4.text((1270, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I5 = ImageDraw.Draw(img)
    # I5.text((1680, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I6 = ImageDraw.Draw(img)
    # I6.text((2095, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I7 = ImageDraw.Draw(img)
    # I7.text((2500, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # I8 = ImageDraw.Draw(img)
    # I8.text((2930, 25), textis,font= fnt, fill=(0, 0, 0))
    # serialnumber = serialnumber+1
    # img.show()
    img = Image.open('Logbook_Template.png')
    global serialnumber
    textis = fr"AA-{serialnumber}"
    I1 = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('consolas.ttf', 82)
    I1.text((2930, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}" #2930 2500 2095 1680 1270 855 450 35
    I1.text((2500, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"
    I1.text((2095, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"
    I1.text((1680, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"
    I1.text((1270, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"
    I1.text((855, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"
    I1.text((450, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"
    I1.text((35, 25), textis,font= fnt, fill=(0, 0, 0))
    serialnumber = serialnumber+1
    textis = fr"AA-{serialnumber}"

    img = img.transpose(Image.ROTATE_90)
    img = img.convert('RGB')
    saveas = fr"C:\Users\jyoth\Desktop\Log Book Serial\Output\{str(i)}.pdf"
    img.save(saveas)
    
    pdf_merger.append(saveas)
    


for z in range(pagesrequired):
    lable(z,)
    # outimage = Image.open(fr"C:\Users\jyoth\Desktop\Log Book Serial\Output\{str(z)}.png")
    # outimage = outimage.transpose(Image.ROTATE_90)
    # outimage.show()
    z=z+1
    
with open(path.abspath(rf'final.pdf'), 'wb') as finalpdf:
    pdf_merger.write(finalpdf)
