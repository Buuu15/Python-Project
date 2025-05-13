import qrcode

data = input("Enter the URL to be converted to QR code: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename + ".png")

print("QR code generated and saved as " + filename + ".png")
