# 🖐️ Gesture-Controlled Presentation

A real-time computer-vision application that allows users to interact with presentation slides using **hand gestures instead of a keyboard or mouse**.

The project captures webcam frames, detects hand landmarks, recognizes gestures and translates them into presentation commands.

## ✨ Features

- 👉 Next / previous slide navigation
- ✍️ Slide annotation
- 🧹 Erase annotations
- 🤞 Pointer / highlight interaction
- 🖐️ Presentation visibility control
- 🔄 Gesture-based presentation control
- 🎥 Real-time webcam processing

## 🧠 System Flow

```text
Webcam
  ↓
Frame Capture
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
| OpenCV | Webcam and image processing |
| MediaPipe | Hand landmark detection |
| cvzone | Hand-tracking utilities |
| NumPy | Coordinate and array operations |

## 🖐️ Gesture Interaction

The application maps different hand configurations to presentation actions such as navigation, pointer interaction, annotation and erasing.

Gesture mappings are configurable as the project evolves.

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

If needed:

```bash
pip install opencv-python cvzone mediapipe numpy
```

### 3. Prepare presentation assets

Create the required presentation/assets directory and place the slide images used by the application inside it.

### 4. Run

Run the project's Python entry point from the repository root.

## 🎓 Engineering Concepts

- Real-time video processing
- Hand landmark detection
- Gesture recognition
- Coordinate-based interaction
- Event-driven application logic
- Integrating multiple computer-vision libraries

## 🚀 Future Improvements

- PowerPoint / Google Slides integration
- Customizable gesture profiles
- More robust gesture recognition
- Voice + gesture interaction
- Better cross-platform support
- Modular gesture-processing architecture

## 👨‍💻 Author

**Siva Bhallu** — [GitHub](https://github.com/bhallusiva)
