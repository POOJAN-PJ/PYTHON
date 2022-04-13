from PIL import Image

# Path for your image where it is
image_1 = Image.open(
    r'C:\Users\Mayan Prajapati\OneDrive\Pictures\3rd_sem_marksheet.jpg')

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(r'C:\Users\Mayan Prajapati\OneDrive\Desktop\Study\CE259 Programming in Python\Practical\3rd_sem_marksheet.pdf')
