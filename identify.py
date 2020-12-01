# Importing
import face_recognition
import random
from PIL import Image, ImageDraw

# Getting the Encodings for Both Gal Gadot, Henry Cavill Faces, and Joaquin Phoenix
image_of_gal = face_recognition.load_image_file('./images/known/gal-gadot.jpg')
gal_face_encoding = face_recognition.face_encodings(image_of_gal)[0]

image_of_henry = face_recognition.load_image_file('./images/known/henry-cavill.jpg')
henry_face_encoding = face_recognition.face_encodings(image_of_henry)[0]

image_of_joaquin = face_recognition.load_image_file('./images/known/joaquin-phoenix.jpg')
joaquin_face_encoding = face_recognition.face_encodings(image_of_joaquin)[0]

# Create Array of Encodings and Names
known_face_encodings = [gal_face_encoding, henry_face_encoding, joaquin_face_encoding]
known_face_names = ['Gal Gadot', 'Henry Cavill', 'Joaquin Phoenix']

# Loading Test Image to Find Faces in
test_image = face_recognition.load_image_file('./images/groups/group1.jpg')

# Finding Faces in Test Image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)
# print(face_encodings)

# Converting to PIL Format
pil_image = Image.fromarray(test_image)

# Create an ImageDraw Instance in order to Draw on top of the Image
draw = ImageDraw.Draw(pil_image)

# Looping for all the Faces in the Test Image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = 'Unknown Person'

    # Testing if Match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Drawing the Main Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 255))
    # Drawing the Label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(255, 255, 255, 255))
    # Drawing the Text
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

# It is Recommended to Delete the Draw Instance
del draw

# Display Image
pil_image.show()

# Saving the Image
pil_image.save(f'./images/others/known{random.randint(1, 100)}.jpg')  # Saving the Images
