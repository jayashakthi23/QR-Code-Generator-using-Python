import qrcode
text=input("Enter the URL:")
qr=qrcode.make(text)
filename="qrcode.png"
qr.save(filename)
print("OR Code saved as", filename)