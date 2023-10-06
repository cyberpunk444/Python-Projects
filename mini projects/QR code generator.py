from qrcode import make

data = input("Enter text or link to embed : ")
img = make(data) #generate
name_of_file = input("Enter name of qrcode file to save : ")
img.save(f"{name_of_file}.png")  #save the image in current directory

print("QR successfully generated 👍")