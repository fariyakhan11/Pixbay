
import PIL
from PIL import Image, ImageFilter,ImageEnhance, ImageOps
import io
import numpy as np
from colorizer import Colorizer
import cv2

# IMAGE TRANSFIGURATION

#-------------blur----------
def blur_image(image):
    im = Image.open(image)
    im = im.filter(ImageFilter.GaussianBlur(radius=6))
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

#------------Grayscale----------
def convert_to_grayscale(image):
    im = Image.open(image).convert('L')
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

#-----------colorize----------------
def convert_to_colour(image):
    colored_img = Colorizer(image,base64_res=False)
    return colored_img
# --------sketch-----------------
def sketch_image(image):
    img = Image.open(image)
    img = np.asarray(img)  
    # convert an image from one color space to another
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       
    invert = cv2.bitwise_not(grey_img) # helps in masking of the image
    # sharp edges in images are smoothed while minimizing too much blurring
    blur = cv2.GaussianBlur(invert, (23, 23), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    sketch = cv2.cvtColor(sketch, cv2.COLOR_BGR2RGB)
    out = Image.fromarray(sketch)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)


#IMAGE ENHANCEMENT FUNCTIONS

#------------sharpness---------------------------
def sharpen_image(image,value):
    im = Image.open(image)
    enhancer =  ImageEnhance.Sharpness(im)
    im= enhancer.enhance(int(value)/10)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

#--------------contrast----------------------------
def contrast_image(image,value):
    im = Image.open(image)
    enhancer = ImageEnhance.Contrast(im)
    im= enhancer.enhance(int(value)/10)
    print(int(value)/10)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

# --------------------Saturate----------------------------
def saturation_image(image,value):
    im = Image.open(image)
    enhancer = ImageEnhance.Color(im)
    im = enhancer.enhance(int(value)/10)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)


# --------------------Bright----------------------------
def bright_image(image,value):
    im = Image.open(image)
    enhancer = ImageEnhance.Brightness(im)
    im = enhancer.enhance(int(value)/10)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

#Edit Tools

#--------dodge------------
def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8') 

#-------------Transpose-----------------
def transpose_image(image):
    im = Image.open(image)
    out = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)


# --------------------mirror----------------------------
def mirror_image(image):
    im = Image.open(image)
    out = ImageOps.mirror(im)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)



# -----------------------Rotate----------------------------
def rot_image(image):
    im = Image.open(image)
    im = im.rotate(90)
    file_object = io.BytesIO()
    im.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

# ----------------------scale-------------------------------
def rescale_image(image):
    img = Image.open(image)
    img = np.asarray(img)    
    rows, cols, dim = img.shape         # get the image shape
    M = np.float32([[1.5, 0  , 0],      # transformation matrix for Scaling  
                    [0,   1.8, 0],
                    [0,   0,   1]])
    out = cv2.warpPerspective(img,M,(cols*2,rows*2))
    out = Image.fromarray(out)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

# --------------------shear X------------
def shear_imageX(image):
    img = Image.open(image)
    img = np.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # convert from BGR to RGB so we can plot using matplotlib
    rows, cols, dim = img.shape                  # get the image shape
    M = np.float32([[1, 0.5, 0],
                    [0, 1  , 0],
                    [0, 0  , 0.85]])
               
    sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))
    out = cv2.cvtColor(sheared_img, cv2.COLOR_BGR2RGB)
    out = Image.fromarray(out)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

#-------------------shear Y-----------------

def shear_imageY(image):
    img = Image.open(image)
    img = np.asarray(img)   
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # convert from BGR to RGB so we can plot using matplotlib
    rows, cols, dim = img.shape                  # get the image shape
    M = np.float32([[1.18,  0, 0],
            	  [0.25, 1, 0],
            	  [0,   0, 1]])                 
    sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))   # apply a perspective transformation to the image 
    out = cv2.cvtColor(sheared_img, cv2.COLOR_BGR2RGB)
    out = Image.fromarray(out)
    file_object = io.BytesIO()
    out.save(file_object, "PNG")
    file_object.seek(0)
    return (file_object)

