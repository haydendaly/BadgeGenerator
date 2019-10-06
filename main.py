import pyqrcode
from PIL import Image
import sys

def generate_qr(num):
    url = pyqrcode.create(num)
    url.png('qrcodes/'+str(num)+'.png', scale=20)

def create_badge(num):
    badge = Image.open('blank/front.png')
    qr_code = Image.open('qrcodes/'+str(num)+'.png')
    badge.paste(qr_code,(1230, 1820))
    badge.save('generated/badge'+str(num)+'.png')

def make_badges(num):
    for i in range(1, num+1):
        generate_qr(i)
        create_badge(i)

if __name__ == '__main__':
    num = int(sys.argv[1])
    make_badges(num)
