import qrcode

data = "https://www.linkedin.com/in/matthew-bourgeois-81a987204/"

img = qrcode.make(data)

img.save('/Users/matt/Desktop/images/linkedqr.png')