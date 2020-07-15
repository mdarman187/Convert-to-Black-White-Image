from PIL import Image


# provide the image name or location. here you can even use a variable to store and assign name
img = Image.open("imagename.jpg") 

# here the image is converted to black & white
img_bw = img.convert("L)

#image is saved to the current directory. here we can even assign you own name and location.
img_bw.save("imagename-bw.jpg")

# show the converted image as output
img_bw.show()
