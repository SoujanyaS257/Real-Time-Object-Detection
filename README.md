# Talking Object Detector 🎯🔊

A real-time object detection system using **OpenCV** and **cvlib**, with spoken feedback via **pyttsx3**.  
This project detects objects from a webcam feed and announces them aloud.

---

## 🚀 Features
- Real-time object detection using webcam
- Bounding boxes drawn around detected objects
- Speaks detected object names (only once to avoid repetition)
- Lightweight implementation with `cvlib` and `pyttsx3`

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/talking-object-detector.git
cd talking-object-detector
```

### 2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the script with:
```bash
python obj_det.py
```

- A window will open showing your webcam feed  
- Detected objects will have bounding boxes  
- The program will **speak** the detected objects once  

Press "q" to quit.

---

## 📂 Project Structure
```
talking-object-detector/
│
├── obj_det.py           # Main script
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements
- [OpenCV](https://opencv.org/) – Computer vision library  
- [cvlib](https://www.cvlib.net/) – Simple object detection  
- [pyttsx3](https://pyttsx3.readthedocs.io/) – Text-to-speech in Python  
