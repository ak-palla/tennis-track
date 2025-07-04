from ultralytics import YOLO
import cv2
import pickle

class BallTracker:
    def __init__(self,model_path):
        self.model = YOLO(model_path)
    
    def detect_frames(self, frames, read_from_stub=False, stub_path=None):
        if read_from_stub and stub_path is not None:
            try:
                with open(stub_path, 'rb') as f:
                    ball_detections = pickle.load(f)
                print(f"[INFO] Loaded detections from {stub_path}")
                return ball_detections
            except FileNotFoundError:
                print(f"[WARN] Stub not found at {stub_path}, running fresh detection...")

        ball_detections = []
        for frame in frames:
            player_dict = self.detect_frame(frame)
            ball_detections.append(player_dict)

        if stub_path is not None:
            with open(stub_path, 'wb') as f:
                pickle.dump(ball_detections, f)
            print(f"[INFO] Saved new detections to {stub_path}")

        return ball_detections

    
        
    def detect_frame(self, frame):
        results = self.model.predict(frame, conf = 0.15)[0] 
        ## Persist tell the machine that there are more frames to come and you must persist the tracker

        
        ball_dict = {}
        
        # Next we must ensure that we exclude everthing other than player for tracking
        for box in results.boxes:
  
            result = box.xyxy.tolist()[0]

           
            ball_dict[1] = result
                
        return ball_dict
    
    def draw_bboxes(self, video_frames, player_detections):
        output_video_frames = []
        for frame, ball_dict in zip(video_frames, player_detections):
            if not ball_dict:  # Skip frames with no detections
                output_video_frames.append(frame)
                continue
            for track_id, bbox in ball_dict.items():
                x1, y1, x2, y2 = bbox
                cv2.putText(frame, f"Ball ID: {track_id}", (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)
            output_video_frames.append(frame)
        return output_video_frames


            