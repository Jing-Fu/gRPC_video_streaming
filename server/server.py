import cv2
import grpc
import numpy as np
from concurrent import futures
import camera_pb2
import camera_pb2_grpc
import threading
import queue

# 定義 Queue 用於在線程之間傳遞影像數據
image_queue = queue.Queue()


def display_image():
    running = True
    while running:
        if not image_queue.empty():
            current_image = image_queue.get()
            cv2.imshow("Received Frame", current_image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            running = False  # 設置標誌為 False，退出顯示循環
            break
    cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗


class CameraService(camera_pb2_grpc.CameraServiceServicer):
    def StreamFrames(self, request_iterator, context):
        for frame in request_iterator:
            # 獲取影像數據
            image_data = frame.image_data
            # 將 bytes 轉換為 numpy array
            nparr = np.frombuffer(image_data, np.uint8)
            current_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # 將影像放入 Queue
            image_queue.put(current_image)

        return camera_pb2.Response(message="Stream Ended")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    camera_pb2_grpc.add_CameraServiceServicer_to_server(CameraService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server is running on port 50051...")

    # 啟動影像顯示線程
    threading.Thread(target=display_image, daemon=True).start()

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
