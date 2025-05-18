# Sports Tracking System - Technical Documentation

## Overview
This documentation covers the Sports Tracking System, a computer vision application designed to track players and the ball in sports videos. The system utilizes YOLOv8 object detection models to identify and track multiple players and the ball across video frames.

## System Architecture

### Core Components
The system consists of the following primary components:

1. **Video Processing Utilities**
   - Located in `utils/video_utils.py`
   - Handles reading video files frame by frame and saving processed output videos

2. **Player Tracking Module**
   - Located in `trackers/player_tracker.py`
   - Uses YOLOv8 to detect and track players across video frames
   - Maintains player identity across frames using tracking IDs

3. **Ball Tracking Module**
   - Located in `trackers/ball_tracker.py`
   - Uses a custom-trained YOLOv8 model to detect the ball in each frame

4. **Main Application**
   - Located in `main.py`
   - Orchestrates the entire tracking pipeline

### Dependency Tree
```
main.py
├── utils/
│   ├── __init__.py
│   └── video_utils.py
└── trackers/
    ├── __init__.py
    ├── player_tracker.py
    └── ball_tracker.py
```

## Component Details

### Video Utilities (`utils/video_utils.py`)

#### Functions:
- `read_video(video_path)`: Reads a video file and returns a list of frames
- `save_video(output_video_frames, output_video_path)`: Saves processed frames as a video file

### Player Tracker (`trackers/player_tracker.py`)

#### Class: `PlayerTracker`

##### Methods:
- `__init__(model_path)`: Initializes the tracker with a YOLOv8 model
- `detect_frames(frames, read_from_stub=False, stub_path=None)`: Processes multiple frames to detect players
- `detect_frame(frame)`: Processes a single frame to detect players
- `draw_bboxes(video_frames, player_detections)`: Draws bounding boxes for detected players

##### Detection Format:
Player detections are stored as a dictionary with the format:
```python
{
    track_id: [x1, y1, x2, y2],
    ...
}
```
Where `track_id` is a unique identifier for each player and `[x1, y1, x2, y2]` are the bounding box coordinates.

### Ball Tracker (`trackers/ball_tracker.py`)

#### Class: `BallTracker`

##### Methods:
- `__init__(model_path)`: Initializes the tracker with a custom YOLOv8 model
- `detect_frames(frames, read_from_stub=False, stub_path=None)`: Processes multiple frames to detect the ball
- `detect_frame(frame)`: Processes a single frame to detect the ball
- `draw_bboxes(video_frames, ball_detections)`: Draws bounding boxes for the detected ball

##### Detection Format:
Ball detections are stored as a dictionary with the format:
```python
{
    1: [x1, y1, x2, y2]
}
```
Where `1` is the identifier for the ball and `[x1, y1, x2, y2]` are the bounding box coordinates.

## Optimization Features

### Stub System
Both trackers implement a "stub" system that allows caching detection results to disk. This saves computation time during development:

1. When `read_from_stub=True` and a valid stub file exists:
   - The system loads pre-computed detections from the stub file
   - This avoids re-running expensive detection operations

2. When `read_from_stub=False` or no valid stub file exists:
   - The system performs detection on all frames
   - Results are saved to the stub file for future use

## Models

### Player Detection Model
- Uses the YOLOv8x model from Ultralytics
- Configured to detect the "person" class with tracking enabled
- The `persist=True` parameter maintains tracking identity across frames

### Ball Detection Model
- Uses a custom YOLOv8 model trained specifically for ball detection
- Located at `models/yolov8_best.pt`
- Configured with a lower confidence threshold (0.15) to capture small, fast-moving balls

## Error Handling
- The system includes robust error handling for missing stub files
- Debug logging provides visibility into the detection process
- Frame count validation ensures consistency between input and output

## Data Flow

1. **Video Input**
   - Video is read frame by frame using `read_video()`

2. **Object Detection**
   - Player Tracker:
     - Each frame is processed to detect people
     - Each person is assigned a tracking ID
     - Results are saved as a list of dictionaries

   - Ball Tracker:
     - Each frame is processed to detect the ball
     - Results are saved as a list of dictionaries

3. **Visualization**
   - Bounding boxes are drawn for players (red) and ball (yellow)
   - Player IDs are displayed above each bounding box

4. **Video Output**
   - Processed frames are saved as a video file using `save_video()`

## Technical Limitations

1. **Ball Detection Accuracy**
   - Small, fast-moving balls can be challenging to detect consistently
   - The system uses a lower confidence threshold (0.15) for ball detection

2. **Player Identity Preservation**
   - In crowded scenes with occlusions, player IDs may occasionally switch

3. **Processing Speed**
   - Processing is performed offline (not real-time)
   - Stub system helps optimize development workflow

## Future Improvements

1. **Court Detection**
   - Add functionality to detect and track court/field lines and keypoints

2. **Team Classification**
   - Extend player tracking to classify players by team

3. **Player Pose Estimation**
   - Integrate pose estimation to track player movements and actions

4. **Real-time Processing**
   - Optimize for real-time processing capabilities

5. **Player Statistics**
   - Generate player movement and positioning statistics