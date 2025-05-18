import pickle


from utils import (read_video,
                   save_video)

from trackers import PlayerTracker, BallTracker



def main():
    # Read Video
    input_video_path = "input_videos/input_video.mp4"
    video_frames = read_video(input_video_path)

    # Detect Players and Ball
    player_tracker = PlayerTracker(model_path="yolov8x")
    ball_tracker = BallTracker(model_path = 'models /yolov8_best.pt')
    
    # Detect ball Frames:
    ball_detections = ball_tracker.detect_frames(video_frames,
                                                 read_from_stub=True,
                                                 stub_path="tracker_stubs/ball_detections.pkl")
    
    # Try reading from stub
    read_from_stub = True
    stub_path = "tracker_stubs/player_detections.pkl"

    if read_from_stub:
        try:
            with open(stub_path, "rb") as f:
                player_detections = pickle.load(f)
            print(f"[INFO] Loaded detections from {stub_path}")
        except FileNotFoundError:
            print(f"[WARN] Stub not found. Running fresh detection.")
            player_detections = player_tracker.detect_frames(video_frames, read_from_stub=False, stub_path=stub_path)
    else:
        player_detections = player_tracker.detect_frames(video_frames, read_from_stub=False, stub_path=stub_path)

    # Debug stub contents
    print(f"[DEBUG] Total detection frames: {len(player_detections)}")
    for i, det in enumerate(player_detections[:5]):
        print(f"[DEBUG] Frame {i}: {det}")

    # Draw Output 
    output_video_frames = player_tracker.draw_bboxes(video_frames, player_detections)
    output_video_frames = ball_tracker.draw_bboxes(output_video_frames, ball_detections)
    
    ## Draw court Keypoints
   
    print(f"[DEBUG] Output video frames: {len(output_video_frames)}")

    save_video(output_video_frames, "output_videos/output_video.avi")

    
    
if __name__ == "__main__":
    main()
    