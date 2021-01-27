'''


'''

'''
# opencv 동영상 불러오기
import cv2
video_file = "image/dog.mp4" #동영상 파일 경로
cap = cv2.VideoCapture(video_file) #동영상 캡처 객체 생성

if cap.isOpened(): #캡처 객체 초기화 확인
    while True:
        ret, img = cap.read() #다음 프레임 읽기
        if ret: #프레임 읽기 정상
            cv2.imshow(video_file, img) # 화면에 표시
            cv2.waitKey(25) # 25ms 지연(40fps로 가정)
        else: # 다음 프레임을 읽을 수 없음
            break # 재생 완료
else:
    print("can't open video.") # 캡처 객체 초기화 실패
cap.release() # 캡처 자원 반납
cv2.destroyAllWindows()
'''

#opencv 본인 캠 키기
import cv2
cap = cv2.VideoCapture(0) # ① 0번 카메라 장치 연결
if cap.isOpened():
    while True:
        ret, img = cap.read() # 카메라 프레임 읽기
        if ret:
            cv2.imshow('camera', img) # 프레임 이미지 표시
            if cv2.waitKey(1) != -1: # ② 1ms동안 키 입력 대기
                break # 아무 키나 눌렸으면 중지
        else:
            print("no frame")
            break
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()

