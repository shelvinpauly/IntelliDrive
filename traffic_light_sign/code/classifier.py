import torch

light_weights = '/home/qamar/yolov5/runs/train/exp5/weights/best.pt'
sign_weights = '/home/qamar/yolov5/runs/train/exp6/weights/best.pt'

# run model on image if it is sign or traffic
def classify(img, sign_bool):
    if sign_bool:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=sign_weights)
    else:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=light_weights)

    results = model(img)
    return results
