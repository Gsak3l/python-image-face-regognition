# Importing
from PIL import Image
import face_recognition
import random

image = face_recognition.load_image_file('./images/groups/group2.jpg')  # numpy array
face_locations = face_recognition.face_locations(image)  # locations of the faces

for face_location in face_locations:  # Looping for Each Face Location
    top, right, bottom, left = face_location  # Getting all the Coordinates
    face_image = image[top:bottom, left: right]  # Giving the Coordinates to an Image Array
    pil_image = Image.fromarray(face_image)  # Loading these Images
    pil_image.show()  # Showing the Images
    pil_image.save(f'./images/others/{random.randint(1, 10000)}.jpg')  # Saving the Images
