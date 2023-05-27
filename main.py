import qrcode
link = "https://www.instagram.com"
img = qrcode.make(link)
print(img)
img.save("instagram.jpg", format="JPEG", scale=5)



