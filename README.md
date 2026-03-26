# IntiCheck - AI-Powered Skin Condition Triage Tool

**Authors**:[Jan Domański](https://github.com/jaaneeczek), [Damian Cybula](https://github.com/DdamianC), [Katarzyna Kuczyńska](https://github.com/kasiakk1) 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.0+-blue.svg)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/tensorflow-2.0+-orange.svg)](https://www.tensorflow.org/)

<img width="2516" height="1318" alt="image" src="https://github.com/user-attachments/assets/4961bcd7-4c43-4db3-96b1-927aeabd3d8d" />

## 🌟 Project Description

IntiCheck is a discreet AI-powered medical assistant that analyzes skin condition images in seconds. Stop guessing with search engines—let AI provide preliminary classification to guide your next steps toward professional care.

This progressive web app (PWA) combines cutting-edge machine learning with privacy-by-design principles, ensuring your health data stays secure and anonymous.

## ✨ Key Features

- **Privacy-by-Design**: Images are processed entirely in-memory and immediately destroyed after analysis—no data storage or persistence
- **In-Memory Processing**: Utilizes byte stream processing in RAM to maintain complete data anonymity and security
- **PWA Support**: Installable web app with offline capabilities and native app-like experience
- **Real-time AI Classification**: Instant analysis of skin conditions using MobileNetV2-based convolutional neural network
- **Medical Triage Guidance**: Provides immediate action recommendations and specialist referrals
- **Responsive Design**: Optimized for both desktop and mobile devices

## 🛠 Tech Stack

- **Backend**: Flask (Python web framework)
- **AI/ML**: TensorFlow with Keras, MobileNetV2 architecture
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **PWA**: Service Worker API, Web App Manifest
- **Deployment**: Docker containerization
- **Image Processing**: Pillow (PIL)
- **Numerical Computing**: NumPy

## 🏗 Architecture

### Data Flow Overview

1. **Image Upload**: User captures or uploads a skin condition photo via the web interface
2. **Client-side Validation**: Image is previewed and validated on the frontend
3. **Secure Transmission**: Image is sent as FormData to the Flask backend via HTTPS POST
4. **In-Memory Processing**: 
   - Image is loaded into RAM as a byte stream using `io.BytesIO`
   - PIL processes the image (resize to 224x224, convert to RGB if needed)
   - NumPy converts to tensor format for model input
5. **AI Inference**: TensorFlow model performs classification across 6 medical categories
6. **Response Generation**: Backend maps model output to medical knowledge base
7. **Immediate Cleanup**: All image data is destroyed from memory after response
8. **Client Display**: Results shown with confidence score, description, and recommendations

### Security Architecture

- **Zero Data Persistence**: Images never touch disk storage
- **Memory-Only Processing**: All operations occur in volatile RAM
- **Stateless Design**: No session data or user tracking
- **CORS Protection**: Configured for secure cross-origin requests

## 🚀 Setup Instructions

### Local Development

1. **Prerequisites**
   ```bash
   # Python 3.11+
   python --version

   # Git (optional, for cloning)
   git --version
   ```

2. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd inticheck
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Locally**
   ```bash
   python server.py
   ```

5. **Access the App**
   - Open your browser to `http://localhost:7860`
   - The app will be available at the root path

### Docker Deployment

1. **Build the Container**
   ```bash
   docker build -t inticheck .
   ```

2. **Run the Container**
   ```bash
   docker run -p 7860:7860 inticheck
   ```

3. **Access the App**
   - Navigate to `http://localhost:7860` in your browser

### Production Deployment

The app is configured for Hugging Face Spaces deployment:
- Port 7860 is exposed
- Static files are served from the root directory
- CORS is enabled for cross-origin requests

## ⚕️ Medical Disclaimer

**IMPORTANT: This application is a TRIAGE TOOL, NOT a final diagnosis.**

IntiCheck uses artificial intelligence to provide preliminary classification of skin conditions. While our AI model has been trained on medical datasets, it:

- Is not a substitute for professional medical advice
- May produce incorrect classifications
- Should never be used as the sole basis for medical decisions
- Requires validation by qualified healthcare professionals

**Always consult a physician or dermatologist for proper diagnosis and treatment.** Early detection and professional care are crucial for skin health.

## 📁 Project Structure

```
inticheck/
├── server.py              # Flask backend with AI inference
├── index.html             # Main application interface
├── about.html             # About page with project details
├── manifest.json          # PWA manifest
├── sw.js                  # Service worker for PWA functionality
├── inti_check_v5_pro.h5   # Trained TensorFlow model
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker container configuration
└── stack.txt             # Technical documentation
```

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with privacy and user safety as top priorities
- Medical knowledge base curated with healthcare professional input
- AI model trained on anonymized medical datasets
- Open-source community for the amazing tools and frameworks

---

**Remember: Your health matters. When in doubt, consult a professional.**</content>
<parameter name="filePath">c:\Users\user\Desktop\IntiCheckEng\README.md
