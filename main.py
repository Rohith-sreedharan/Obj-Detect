import cv2
from ultralytics import YOLO

# Intial Declartion
model = YOLO("yolov8n.pt")  
cap = cv2.VideoCapture("sam.mp4")
ball_count = 0
total_confidence = 0.0

# Logging For Accuracy
with open("ball_detections.txt", "w") as log_file:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, verbose=False)
        for result in results[0].boxes.data:
            x1, y1, x2, y2, confidence, class_id = result
            if confidence > 0.25 and class_id == 0:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                ball_count += 1
                total_confidence += confidence
                # Frame time (Mac Min Split time is  25 FPS)
                frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
                minutes = int(frame_time // 60)
                seconds = int(frame_time % 60)
                milliseconds = int((frame_time - int(frame_time)) * 1000)
                log_file.write(f"Element name: Green Ball\n"
                               f"Element frame: {minutes:02d}:{seconds:02d}:{milliseconds:03d}\n"
                               f"Confidence: {confidence:.2f}\n\n")
        cv2.putText(frame, f"Ball Count: {ball_count}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Frame', frame)
        # handling explict cases
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
# Generate report
print("Total Ball Count:", ball_count)
print("Average Confidence:", total_confidence / ball_count)