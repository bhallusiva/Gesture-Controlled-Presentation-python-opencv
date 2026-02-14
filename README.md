# 🖐️ Gesture Controlled Presentation

A **Python + OpenCV** project that allows users to control presentation slides using **hand gestures**.
You can move between slides, draw annotations, erase them, or even toggle the presentation webcam — all through gestures, no keyboard or mouse needed!

---

## 🎯 Overview

This project provides a **gesture-based control system** for presentations using your webcam.
It uses **Computer Vision** techniques to detect hand gestures and translate them into presentation commands such as next/previous slide, drawing, erasing, and toggling webcam visibility.

---

## ✨ Features

* 👆 **Navigate Slides:** Move to next or previous slides using hand gestures
* ✍️ **Annotate:** Draw on slides with your index finger
* ✋ **Erase:** Remove annotations using three fingers
* 🖐️ **Hide/Show:** Raise all five fingers to toggle presentation visibility
* 🤞 **Pointer Mode:** Highlight points on the slide without drawing
* 🎥 **Webcam Feed:** Display your webcam feed along with slides
* 🔁 **Auto Slide Mode:** Automatically switch slides using specific gestures

---

## 🧠 Tech Stack & Libraries Used

| Library          | Purpose                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| **Python**       | Main programming language for the project                                        |
| **OpenCV (cv2)** | Used for setting up the webcam, capturing frames, and displaying slides          |
| **NumPy**        | Handles mathematical and array manipulations for image and coordinate operations |
| **cvzone**       | Provides `HandTrackingModule` for easy hand gesture detection                    |
| **MediaPipe**    | Used internally by `cvzone` to detect and track hand landmarks efficiently       |

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/bhallusiva/gesture-controlled-presentation.git
cd gesture-controlled-presentation
```

### 2. Install dependencies

```bash
pip install opencv-python cvzone mediapipe numpy
```

### 3. Add your slides

* Create a folder named `Presentation` inside the project directory
* Add your slide images (e.g., `.jpg`, `.png`) inside that folder

### 4. Run the program

```bash
python gesture_presentation.py
```

---

## 🖐️ Gesture Controls

| Gesture                         | Action                        |
| ------------------------------- | ----------------------------- |
| 👉 Index Finger Up              | Draw annotations              |
| 🤞 Index + Middle Fingers       | Pointer Mode                  |
| 🖐️ All Five Fingers            | Hide / Show window            |
| 👆 Index Finger (Top of Screen) | Change slides (Next/Previous) |
| ✋ Three Fingers                 | Erase last annotation         |
| 🤙 Thumb + Index                | Auto slide                    |

---

## 🧩 Folder Structure

```
gesture-controlled-presentation/
│
├── gesture_presentation.py        # Main Python file
├── Presentation/                  # Folder containing presentation slide images
├── README.md                      # Project documentation
└── requirements.txt                # (Optional) Dependency list
```

---

## 🚀 Future Enhancements

* Add gesture customization for personalized controls
* Integrate with Microsoft PowerPoint / Google Slides directly
* Improve detection accuracy and performance
* Add voice command support for hybrid control

---

## 👨‍💻 Author

**Siva Bhallu**
📧 [bhallusivakumar@gmail.com](mailto:bhallusivakumar@gmail.com)
🌐 [LinkedIn Profile](https://www.linkedin.com/in/siva-bhallu-333836305/)

⭐ *Don’t forget to star this repo if you like it! *⭐
