from deepface import DeepFace
backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe'
]
recognition = DeepFace.find(img_path = "MV5BNzA5NGI2ZGMtYzM0Yi00YTFlLWEyNWItYjBlZDZmZWM2OGM3XkEyXkFqcGdeQXVyNjUxMjc1OTM@._V1_.jpg", db_path = "faces", detector_backend=backends[5])
print(recognition)
