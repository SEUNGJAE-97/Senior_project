### Keras 모델을 적용한 알약 판별 어플

## Get_img.py 
    <img src="https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/17500b43-624c-428d-a8cd-b8426c1fd7fb">
    
   - 이미지를 다운 받을 수 있는 URL로부터 데이터를 수집한다.
   
## Data_set_processing.py 
   <p align="center"><img src="https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/79006101-1688-4541-ba29-1a6c235bb0bf" width="250" height="300"> 
   <img src="https://github.com/SEUNGJAE-97/Senior_project/assets/117517535/398b3259-915c-4631-88a7-c4e161d21386" width="250" height="300"></p>
   
   - 가공되지 않은 데이터로부터 OpenCV 라이브러리를 활용하여 객체를 검출하고, Crob하여 저장한다.
   

   
## albumentations_data.ipynb
   - Data_set_processing.py에서 얻은 데이터에 Albumentations 라이브러리를 활용하여 데이터 증강을 한다. 
