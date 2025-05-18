import cv2

# Running it Frame by Frame
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

# Saving the video

def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        print("[ERROR] No frames provided to save_video(). Skipping video write.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    height, width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

    for frame in output_video_frames:
        out.write(frame)
    out.release()
    print(f"[INFO] Video saved successfully to {output_video_path}")
