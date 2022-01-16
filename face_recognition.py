from deepface import DeepFace

obj = DeepFace.verify(img1_path="images/2_6.jpg", img2_path="images/3.jpg", model_name='ArcFace', detector_backend='retinaface')
print(obj)
