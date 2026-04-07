import tkinter as tk
import time
from PIL import Image,ImageTk 

#Main Application window
root = tk.Tk()
root.title("Photo SLideshow Album")
root.geometry("900x900")

#List of Image Paths
image_paths=[
   r"C:\Users\Dell\OneDrive\Desktop\Album\img1.avif",
    r"C:\Users\Dell\OneDrive\Desktop\Album\img2.webp",
    r"C:\Users\Dell\OneDrive\Desktop\Album\img3.avif",
    r"C:\Users\Dell\OneDrive\Desktop\Album\img4.jpg",
    r"C:\Users\Dell\OneDrive\Desktop\Album\img5.avif",
    r"C:\Users\Dell\OneDrive\Desktop\Album\img6.jpg"
]
image_size = (700,700)
images=[]
for path in image_paths:
    img= Image.open(path)
    img=img.resize(image_size)
    images.append(img) #Adding each image in the list

#Convert PIL Images into Tkinter Compatible Image
final_images=[]
for img in images:
    photo = ImageTk.PhotoImage(img) 
    final_images.append(photo)

#Label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

#Slidesshow Function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

#Button
play_button = tk.Button(
    root,
    text = "Play the Slideshow",
    font=("Arial",17),
    command=start_slideshow
)
play_button.pack(pady=40)

root.mainloop()







