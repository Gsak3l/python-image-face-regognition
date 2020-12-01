# Importing
import face_recognition

# -- GAL GADOT -- #
# Loading the Image of Gal Gadot
image_of_gal = face_recognition.load_image_file('./images/known/gal-gadot.jpg')
# Face Encoding Returns the Facial Features that can be Compared to Other Images
gal_face_encoding = face_recognition.face_encodings(image_of_gal)[0]  # Just the First Element is Needed

# -- OTHER UNKNOWN HUMAN -- #
# Loading the Image of Gal Gadot
unknown_image = face_recognition.load_image_file('./images/unknown/unknown14.jpg')
# Face Encoding Returns the Facial Features that can be Compared to Other Images
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]  # Just the First Element is Needed

# Comparing the Two Faces
results = face_recognition.compare_faces([gal_face_encoding], unknown_face_encoding)  # Returns Either True or False

if results[0]:
    print('This is Gal')
else:
    print('This is NOT Gal')
