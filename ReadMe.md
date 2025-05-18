# Sports Video Analysis System

![Sports Tracking Banner](https://img.shields.io/badge/Sports-Tracking-blue)
![Python Version](https://img.shields.io/badge/python-3.7%2B-brightgreen)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-yellow)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red)

A computer vision system for tracking players and balls in sports videos using YOLOv8.

## Features

- **Player Detection & Tracking**: Identifies individual players and maintains their identity across frames
- **Ball Tracking**: Locates and tracks the ball using a specialized detection model
- **Performance Optimization**: Caching system for saving detection results during development
- **Visualization**: Creates output videos with bounding boxes for players and ball

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLOv8
- Pickle

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/sports-tracking.git
   cd sports-tracking
   ```

2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python
   ```

3. Download YOLOv8 model:
   ```bash
   # YOLOv8x is downloaded automatically by Ultralytics
   # If using a custom model, place it in the models/ directory
   ```

## Project Structure

```
.
├── input_videos/           # Store input sports videos here
├── models/                 # YOLOv8 models
│   └── yolov8_best.pt      # Custom ball detection model
├── output_videos/          # Generated output videos
├── tracker_stubs/          # Cached detection results
├── trackers/               # Tracking modules
│   ├── __init__.py
│   ├── ball_tracker.py     # Ball detection and tracking
│   └── player_tracker.py   # Player detection and tracking
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── video_utils.py      # Video processing utilities
├── main.py                 # Main application
├── yolo_inference.py       # Example YOLO inference script
└── README.md
```

## Usage

1. Place your input video in the `input_videos/` folder (default: `input_video.mp4`)

2. Run the tracking system:
   ```bash
   python main.py
   ```

3. Find the output video in the `output_videos/` folder

## Configuration

You can modify the following parameters in `main.py`:

- Input and output video paths
- Model paths
- Stub settings for caching detections

Example:
```python
# Change input video
input_video_path = "input_videos/my_game.mp4"

# Use different model
player_tracker = PlayerTracker(model_path="yolov8m")

# Disable stub caching
player_detections = player_tracker.detect_frames(video_frames, read_from_stub=False)
```

## How It Works

1. **Video Processing**: The system reads the input video frame by frame
2. **Player Detection**: YOLOv8x identifies players and assigns tracking IDs
3. **Ball Detection**: A custom YOLOv8 model locates the ball in each frame
4. **Visualization**: Bounding boxes are drawn for players and the ball
5. **Output Generation**: Processed frames are combined into a output video

## Advanced Usage

### Using the Stub System

The stub system allows you to cache detection results to disk, saving computation time during development:

```python
# Enable stub system (load from cache if available)
player_detections = player_tracker.detect_frames(
    video_frames, 
    read_from_stub=True,
    stub_path="tracker_stubs/my_custom_detections.pkl"
)
```

### Using Different YOLOv8 Models

You can use different YOLOv8 models based on your needs:

```python
# For faster processing but less accuracy
player_tracker = PlayerTracker(model_path="yolov8n")

# For better accuracy but slower processing
player_tracker = PlayerTracker(model_path="yolov8x")
```

## Example Output

The output video will display:
- Red bounding boxes around detected players with player IDs
- Yellow bounding boxes around the detected ball

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)

## Future Plans

- Court/field detection
- Team classification
- Player movement analysis
- Real-time processing capabilities