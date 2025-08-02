from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="crop_insect_dataset/crop_insect.yaml",
    epochs=50,
    imgsz=640,
    name="crop_insect_detect_model"
)
