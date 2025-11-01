# Gesture-Controlled-Presentation-python-opencv
# 🖐️ Gesture Controlled Presentation

A **Python + OpenCV** project that allows users to control presentation slides using **hand gestures**.  
You can move between slides, draw annotations, erase them, or even toggle the presentation webcam etc.. — all through gestures, no keyboard or mouse needed!

---

## 🎯 Overview

This project provides a **gesture-based control system** for presentations using your webcam.  
It uses **Computer Vision** techniques to detect hand gestures and translate them into presentation commands such as next/previous slide, drawing, erasing, and toggling webcam visibility.

---

## ✨ Features

- 👆 **Navigate Slides:** Move to next or previous slides using hand gestures  
- ✍️ **Annotate:** Draw on slides with your index finger  
- ✋ **Erase:** Remove annotations using three fingers  
- 🖐️ **Hide/Show:** Raise all five fingers to toggle presentation visibility  
- 🤞 **Pointer Mode:** Highlight points on the slide without drawing        
- 🎥 **Webcam Feed:** Display your webcam feed along with slides  
- 🔁 **Auto Slide Mode:** Automatically switch slides using specific gestures  

---

## 🧠 Tech Stack & Libraries Used

| Library | Purpose |
|----------|----------|
| **Python** | Main programming language for the project |
| **OpenCV (cv2)** | Used for setting up the webcam, capturing frames, and displaying slides |
| **NumPy** | Handles mathematical and array manipulations for image and coordinate operations |
| **cvzone** | Provides `HandTrackingModule` for easy hand gesture detection |
| **MediaPipe** | Used internally by `cvzone` to detect and track hand landmarks efficiently |

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/bhallusiva/gesture-controlled-presentation.git
   cd gesture-controlled-presentation

