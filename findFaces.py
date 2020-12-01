# Importing
import face_recognition

image = face_recognition.load_image_file('./images/groups/group2.jpg')  # numpy array
face_locations = face_recognition.face_locations(image)  # locations of the faces

# Array of Coordinates for Each Face
# print(face_locations)

# Printing the Number of People in the Photo
print(f'There are {len(face_locations)} people in this image')
