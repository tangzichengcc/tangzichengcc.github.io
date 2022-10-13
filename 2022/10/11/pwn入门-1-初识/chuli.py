from PIL import Image


img_file = './image-20221011173542682.png'
im = Image.open(img_file)

im.save('test.png',quality=50)
