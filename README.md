# 🖐️ Gesture-Controlled Presentation

A computer-vision application that lets users control presentation slides using **hand gestures** instead of a keyboard or mouse.

The project uses a webcam to detect hand landmarks and translates gestures into presentation actions such as navigation, annotation, erasing and pointer control.

## ✨ Features

- 👉 Navigate to the next or previous slide
- ✍️ Draw annotations directly on slides
- 🧹 Erase annotations
- 🤞 Pointer/highlight mode
- 🖐️ Hide/show the presentation window
- 🔄 Gesture-based automatic slide control
- 🎥 Real-time webcam-based interaction

## 🧠 How It Works

```text
Webcam
   ↓
Video Frame Capture
   ↓
Hand Detection & Landmark Tracking
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
| cvzone | Simplified hand-tracking utilities |
| MediaPipe | Hand landmark detection |
| NumPy | Array and coordinate operations |

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/bhallusiva/Gesture-Controlled-Presentation-python-opencv.git
cd Gesture-Controlled-Presentation-python-opencv
```

### 2. Install dependencies

```bash
pip install opencv-python cvzone mediapipe numpy
```

If a `requirements.txt` file is present, you can instead run:

```bash
pip install -r requirements.txt
```

### 3. Add presentation slides

Create a `Presentation/` directory and place the slide images used by the application inside it.

### 4. Run the application

Use the project's main Python entry point, for example:

```bash
python gesture_presentation.py
```

> The exact entry-point filename may vary depending on the current project files.

## 🖐️ Gesture Controls

| Gesture | Action |
|---|---|
| ☝️ Index finger | Draw / interact |
| ✌️ Index + middle fingers | Pointer mode |
| 🖐️ Five fingers | Hide / show presentation |
| Three-finger gesture | Erase annotation |
| Specific navigation gesture | Next / previous slide |
| Specific automation gesture | Auto-slide mode |

## 📁 Project Structure

```text
Gesture-Controlled-Presentation-python-opencv/
├── gesture_presentation.py
├── Presentation/
├── requirements.txt
└── README.md
```

## 🚀 Future Improvements

- PowerPoint / Google Slides integration
- Customizable gesture mappings
- Better gesture recognition accuracy
- Voice + gesture hybrid control
- Improved performance and cross-platform support

## 🎯 Learning Outcomes

This project helped me practice **computer vision, real-time video processing, hand landmark detection, coordinate-based interaction and event-driven application logic**.

---

**Author:** [Siva Bhallu](https://github.com/bhallusiva)
