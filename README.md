**Keras 모델을 적용한 알약 판별 어플**

# Data_set_processing.py 
   - 가공되지 않은 데이터로부터 OpenCV 라이브러리를 활용하여 객체를 검출하고, Crob하여 저장한다.
# Get_img.py 
   - 이미지를 다운 받을 수 있는 URL로부터 데이터를 수집한다.
# albumentations_data.ipynb
   - Data_set_processing.py에서 얻은 데이터에 Albumentations 라이브러리를 활용하여 데이터 증강을 한다. 
