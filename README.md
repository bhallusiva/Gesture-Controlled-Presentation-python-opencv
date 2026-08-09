# 🖐️ Gesture-Controlled Presentation

A real-time **computer-vision presentation controller** that lets users navigate and interact with presentation slides using hand gestures instead of a keyboard or mouse.

The project combines webcam video processing, hand-landmark detection and gesture recognition to translate physical hand movements into presentation commands.

## ✨ Features

- 👉 Next / previous slide navigation
- ✍️ Draw annotations on slides
- 🧹 Erase annotations
- 🤞 Pointer / highlight mode
- 🖐️ Hide / show presentation window
- 🔄 Gesture-based automatic slide control
- 🎥 Real-time webcam interaction

## 🧠 System Flow

```text
Webcam
   ↓
Video Frame Capture
   ↓
Hand Landmark Detection
   ↓
Gesture Recognition
   ↓
Presentation Command
   ↓
Slide / Annotation Update
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| OpenCV | Webcam capture and image processing |
| cvzone | Hand-tracking utilities |
| MediaPipe | Hand landmark detection |
| NumPy | Coordinate and array operations |

## 🖐️ Gesture Controls

| Gesture | Action |
|---|---|
| ☝️ Index finger | Draw / interact |
| ✌️ Index + middle fingers | Pointer mode |
| 🖐️ Five fingers | Hide / show presentation |
| Three-finger gesture | Erase annotation |
| Navigation gesture | Next / previous slide |
| Automation gesture | Auto-slide mode |

> Gesture mappings can be adjusted as the project evolves.

## ⚙️ Setup

### 1. Clone

```bash
git clone https://github.com/bhallusiva/Gesture-Controlled-Presentation-python-opencv.git
cd Gesture-Controlled-Presentation-python-opencv
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable in your local checkout:

```bash
pip install opencv-python cvzone mediapipe numpy
```

### 3. Prepare presentation assets

Create a `Presentation/` directory and place the slide images required by the application inside it.

### 4. Run

Run the project's Python entry point from the repository root.

## 🎓 Engineering Concepts Practiced

- Real-time video processing
- Computer vision
- Hand landmark detection
- Gesture recognition
- Coordinate-based interaction
- Event-driven application logic
- Integrating multiple Python libraries into one application

## 🚀 Future Improvements

- PowerPoint / Google Slides integration
- Customizable gesture mappings
- Improved gesture recognition accuracy
- Voice + gesture hybrid control
- Better performance and cross-platform support
- Modular gesture-processing architecture

## 👨‍💻 Author

**Siva Bhallu** — [GitHub](https://github.com/bhallusiva)
