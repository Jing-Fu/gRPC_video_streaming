import time
import cv2
import grpc
import camera_pb2
import camera_pb2_grpc


# 獲取相機畫面並傳送的生成器
def generate_frames():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 將影像轉換為JPEG格式
        ret, buffer = cv2.imencode(".jpg", frame)
        frame_data = buffer.tobytes()
        height, width = frame.shape[:2]

        # 生成 Frame message
        yield camera_pb2.Frame(image_data=frame_data, width=width, height=height)
        time.sleep(1 / 60)


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = camera_pb2_grpc.CameraServiceStub(channel)

    # 傳送畫面流
    response = stub.StreamFrames(generate_frames())
    print("Server response:", response.message)


if __name__ == "__main__":
    run()
