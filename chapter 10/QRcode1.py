# Example 10.23 QR code generation
# https://pypi.org/project/qrcode/
# https://en.wikipedia.org/wiki/QR_code
# pip install qrcode

import qrcode

#Create a QRcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data("https://www.bioxsystems.com/")
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
