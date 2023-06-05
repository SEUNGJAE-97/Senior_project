#### Keras 모델을 적용한 알약 판별 어플
### 데이터 전처리
## Get_img.py 
![11](https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/17500b43-624c-428d-a8cd-b8426c1fd7fb)
    
   - 이미지를 다운 받을 수 있는 URL로부터 데이터를 수집한다.
   - 각 이미지는 품목 일련번호를 파일 이름으로 갖는다.
   
## Data_set_processing.py 
   <p align="center"><img src="https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/79006101-1688-4541-ba29-1a6c235bb0bf" width="250" height="300"> 
   <img src="https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/398b3259-915c-4631-88a7-c4e161d21386" width="250" height="300"></p>
   
   - 가공되지 않은 데이터로부터 OpenCV 라이브러리를 활용하여 객체를 검출하고, Crob하여 저장한다.
   
## albumentations_data.ipynb
   ![output3](https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/37556ae6-e494-4dc3-bf07-b4e1e8b72cd1)

   - Data_set_processing.py에서 얻은 데이터에 Albumentations 라이브러리를 활용하여 데이터 증강을 한다. 
 
### 서버
## server.py
   - 멀티 프로세스를 활용하여 최대 10명의 동시접속을 지원한다.
   
   - 클라이언트(Android application)로부터 이미지를 전송받고, 해당 이미지를 학습 시킨 keras 모델로부터 
     예측 값을 클라이언트에게 재전송한다. 
## keras_example.ipynb
  # 첫번째 결과
  ![화면 캡처 2023-05-31 033955](https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/93f1d7b9-6e64-46c1-b037-c8a9a11b18f6)
  
  - 아무런 문양이 없는 이미지에 대해서도 학습을 진행하였다.
  
  - 이미지의 일부를 자르거나 가리는 등 데이터 증강 기법을 적용하였다. 
  # 문제점 
  - 너무 과하거나 의미없는 데이터가 늘어났고, 결과적으로 과적합(Overfitting)이라는 문제가 발생하였다.
 # 두번째 결과
 ![output](https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/fb15a3f6-9d7c-442b-8580-403a50bc597a)
 
  - 첫번째에 사용한 학습 데이터에서 앞이나 뒤에 아무런 문양이나 문자가 없는 경우를 제외하였다.
  
  - 데이터 증강 과정에서 과하게 데이터가 변형되는 상황을 막기 위하여 자르기, 가리기 등을 제외하여 학습 데이터셋을 
    다시 만들었다.  
  
  # 문제점 
  - 대략 98%의 정확도를 보였지만, 일정 epoch를 넘어서는 순간 급격하게 정확도가 떨어졌다. 
 # 세번째 결과 
 ![output2](https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/af84a319-8070-4121-ac8d-f2dce6cf45c5)
 
   - 급격하게 정확도가 떨어지기전에 조기멈춤 규제기법(Early Stopping)을 사용하였다. 
   - 
  
  
   
