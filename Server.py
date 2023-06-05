# date : 23.04.16 ~ 06. 01
# func : 어플리케이션으로부터 이미지를 전송 받는다.
#        해당 이미지를 모델에 넣고 나온 데이터(알약의 고유 ID 값)
#        를 다시 어플리케이션으로 전송한다. 어플리케이션에서는 해당 고유ID를 
#        다시 데이터베이스에서 찾아 화면에 띄워준다. 
import socket
import os
import multiprocessing
import tensorflow as tf
import numpy as np
import cv2

# 1. 멀티프로세싱으로 한번에 많은 클라이언트와 소켓통신을 진행한다.
#     서버 설정
class_names = [
    '197400246', '198300605', '198701126', '198801248', '198801534',
    '198801657', '198901340', '199001505', '199101702', '199301551',
    '199401319', '199501306', '199601642', '199601724', '199701845',
    '199701895', '199801389', '199801580', '199801651', '199801826',
    '199801864', '199801880', '199801882', '199901577', '199901764',
    '199901886', '199901915', '199906848', '200108428', '200201717',
    '200301465', '200401859', '200500248', '200907782', '200907817',
    '200908266', '200908444', '200908499', '200908500', '200908862',
    '200908953', '201000163', '201000674', '201101253', '201101451',
    '201101491', '201101508', '201101576', '201101585', '201101857',
    '201101885', '201102120', '201102470', '201102473', '201102545',
    '201102546', '201102618', '201103116', '201103161', '201103214',
    '201103297', '201103308', '201103309', '201103366', '201103449',
    '201105511', '201105613', '201105697', '201105818', '201105914',
    '201105915', '201106062', '201106063', '201106314', '201106322',
    '201106367', '201106371', '201106770', '201109259', '201109329',
    '201109333', '201109335', '201109431', '201109442', '201109826',
    '201109827', '201109900', '201110104', '201110105', '201110123',
    '201110192', '201110262', '201110452', '201110467', '201110513',
    '201110661', '201110739', '201110747', '201110830', '201111087',
    '201112195', '201200120', '201206445', '201206484', '201206525',
    '201206552', '201206553', '201206575', '201206592', '201206776',
    '201206781', '201206828', '201206871', '201206916', '201206997',
    '201206998', '201207011', '201207054', '201207068', '201207104',
    '201207105', '201207237', '201207343', '201207344', '201207415',
    '201207487', '201207490', '201207507', '201210185', '201210189',
    '201210739', '201211056', '201211098', '201300020', '201300035',
    '201300036', '201300049', '201300109', '201300127', '201301235',
    '201301370', '201301376', '201301655', '202200407']
# 서버 주소와 포트번호
IP = ''  # 모든 인터페이스에서 접속 허용
PORT = 8000
PATH = "E:/image/image.jpg"  # 파일을 수신할 경로 및 이름


# 크롭된 이미지를 입력 받는다.
def find_contr(img):
    target = img
    target = cv2.resize(target, dsize=(500, 500), interpolation=cv2.INTER_LANCZOS4)
    # 이미지 처리
    targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    targetBlur = cv2.GaussianBlur(targetGray, (5, 5), 3)
    targetTh = cv2.Canny(targetBlur, 150, 250)

    # 모든 컨투어 찾기
    cntrs_target, hierarchy = cv2.findContours(targetTh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cntrs_target = sorted(cntrs_target, key=cv2.contourArea, reverse=True)
    x, y, w, h = cv2.boundingRect(cntrs_target[0])

    # croppted_image = targetTh[y:y+h, x:x+w]
    saved_image = target[y:y + h, x:x + w]

    cv2.imshow("Cropped_image", saved_image)
    cv2.waitKey(0)

    return saved_image


def perform_grabcut(img, rect):
    # Load the image
    image = img
    image = cv2.resize(image, dsize=(500, 500), interpolation=cv2.INTER_LANCZOS4)

    # Create a mask with zeros initially
    mask = np.zeros(image.shape[:2], np.uint8)

    # Set the background and foreground model
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Apply GrabCut on the specified ROI
    cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where the probable foreground is set to 1 and the others to 0
    mask_probable_foreground = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Apply the mask to the original image
    image_with_background_removed = image * mask_probable_foreground[:, :, np.newaxis]

    # Display the result
    #cv2.imshow("Original Image", image)
    #cv2.imshow("Image with Background Removed", image_with_background_removed)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return image_with_background_removed


def get_key():
    # load model
    roi_rect = (100, 100, 200, 250)

    model = tf.keras.models.load_model("E:/rps3.h5")
    img = cv2.imread(PATH, cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img, (500, 500))

    removed_image = perform_grabcut(img, roi_rect)
    #saved_image = find_contr(removed_image)

    #saved_image = cv2.resize(saved_image, (500,500))

    img_array = tf.keras.preprocessing.image.img_to_array(removed_image)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)



    # print(type(class_names[np.argmax(predictions)]))
    return class_names[np.argmax(predictions)]


def handle_client(conn, addr, path):
    # 파일 데이터 수신
    data_size = conn.recv(4)
    data_size = int.from_bytes(data_size, byteorder='big')
    received_data = bytearray()

    while len(received_data) < data_size:
        packet = conn.recv(data_size - len(received_data))
        if not packet:
            break
        received_data += packet
    print("received data length : ", len(received_data))

    with open(path, 'wb') as f:
        f.write(received_data)

    key = get_key()
    send_string(conn, key)
    # 소켓 종료
    conn.close()
    print('클라이언트 {}의 파일 전송이 완료되었습니다.'.format(addr))
    print('접속을 종료합니다.')


def send_string(client_socket, string):
    # 문자열 인코딩
    string = string.encode('UTF-8')
    print(string)
    # 문자열 전송
    client_socket.sendall(string)


if __name__ == '__main__':
    # 소켓 생성 및 바인딩
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen(10)  # 최대 10개의 클라이언트까지 대기 가능
    print('server start')

    # 멀티프로세싱으로 클라이언트 처리
    while True:
        conn, addr = server_socket.accept()
        print('새로운 클라이언트 {}가 연결되었습니다.'.format(addr))
        p = multiprocessing.Process(target=handle_client, args=(conn, addr, PATH))
        p.start()
