from paz.models import SSD300
from paz.pipelines import DetectSingleShot
from paz.backend.camera import VideoPlayer, Camera


# weights_path = 'experiments/SSD300_RUN_00_07-06-2022_13-17-39/model_weights.hdf5'
weights_path = 'experiments/SSD300_RUN_00_08-06-2022_10-52-57/model_weights.hdf5'
class_names = ['background', 'hand']
model = SSD300(len(class_names), None, None)
model.load_weights(weights_path)
score_thresh = 0.2

nms_thresh = 0.45
detect = DetectSingleShot(model, class_names, score_thresh, nms_thresh)

camera = Camera(device_id=4)
player = VideoPlayer((1280, 960), detect, camera)
player.run()