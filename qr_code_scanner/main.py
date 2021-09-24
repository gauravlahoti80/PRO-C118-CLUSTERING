import qrcode
import image 

my_qr = qrcode.QRCode(version=15, box_size=15,border=5)
data = "Gaurav"
my_qr.add_data(data)
my_qr.make(fit=True)
img = my_qr.make_image(fill = "black", back_color = "white")
img.save("qr.png")