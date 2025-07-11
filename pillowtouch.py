from PIL import Image
#Open image using Image module
im = Image.open(r"C:\temp\99-WebSites\website-reiki\reikisession.jpg")
#Show actual Image 
#im.show()
#Show rotated Image
#im = im.rotate(45) 
#im.show()

print(f"Filename: {im.filename}\n Format: {im.format}\n Width: {im.width}\n Height: {im.height}\n Mode: {im.mode}\n Size: {im.size}")


im.save('reikisession.gif','GIF')