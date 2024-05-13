# Dr DiagnoSense
<div align='center'>
  <img src="https://img.shields.io/github/contributors/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=blue" alt="GitHub contributors">
  <img src="https://img.shields.io/github/issues-closed-raw/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=brightgreen" alt="GitHub Closed issues">
  <img src="https://img.shields.io/github/issues-pr/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=aqua" alt="GitHub PR Open">
  <img src="https://img.shields.io/github/issues-pr-closed-raw/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=blue" alt="GitHub PR closed">
  <img src="https://img.shields.io/github/languages/count/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=brightgreen" alt="GitHub language count">
  <img src="https://img.shields.io/github/last-commit/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=blue" alt="GitHub last commit">
  <img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?style=for-the-badge" alt="GitHub Maintained">
  <img src="https://img.shields.io/github/repo-size/TheNaiveSamosa/Dr-DiagnoSense?style=for-the-badge&color=aqua" alt="Github Repo Size">
</div>
Welcome to Dr DiagnoSense, your personal health assistant powered by machine learning!

## About
Dr DiagnoSense is a derivative project inspired by Aditya Khamitkar's original creation, DoctorBot. While DoctorBot was directly developed in collaboration with Intel and the Government of India, Dr DiagnoSense inherits the spirit of leveraging machine learning techniques to provide health insights. The aim remains consistent: to offer a language-based health assistant that analyzes symptoms, provides probable causes of conditions, and suggests medications, all free of cost.

Dr DiagnoSense aims to leverage machine learning (ML) techniques to detect and provide insights on various health conditions including Alzheimer's disease, brain tumors, breast cancer, diabetes, epilepsy, and heart attacks. Our ultimate goal is to create a Language Learning Model (LLM) that users can interact with to discuss their health concerns. Dr DiagnoSense will analyze symptoms, provide probable causes of the condition, and even suggest medications, all free of cost.

## Disease Prediction
- **Alzheimer's Disease**: Utilizes cognitive assessment data and neuroimaging techniques to detect early signs of Alzheimer's.
- **Brain Tumor**: Analyzes MRI images to detect brain tumors.
- **Breast Cancer**: Utilizes mammogram images to detect signs of breast cancer.
- **Heart Attack Detection**: Analyzes various health parameters such as blood pressure, cholesterol levels, and heart rate to assess the risk of heart attacks.

## How to Use
1. **Install Dependencies**: Make sure you have all the necessary dependencies installed. See the `requirements.txt` file for details.
2. **Run Dr DiagnoSense**: Execute the main script to start interacting with Dr DiagnoSense.
3. **Discuss Your Health**: Type in your symptoms or health concerns to start a conversation with Dr DiagnoSense.
4. **Receive Insights**: Dr DiagnoSense will analyze your inputs and provide insights on potential health conditions and medications.

## Project Structure
    ├── Alzheimer's Disease
    │   ├── alzheimers_model.ipynb
    │   ├── alzheimers_predictor.py
    │   └── alzheimers_model.pkl
    ├── Brain Tumor
    │   ├── brain_tumor_model.ipynb
    │   ├── brain_tumor_predictor.py
    │   └── brain_tumor_model.pkl
    ├── Breast Cancer
    │   ├── breast_cancer_model.ipynb
    │   ├── breast_cancer_predictor.py
    │   └── breast_cancer_model.pkl
    |   ├── Heart Attack Detection
    │   ├── heart_attack_model.ipynb
    │   ├── heart_attack_predictor.py
    │   └── heart_attack_model.pkl
    ├── Dr. DiagnoSense (Streamlit Web App)
    │   └── dr_diagnosense.py
    ├── LICENSE
    ├── README.md
    └── requirements.txt

    ---
```
   +---------------------------------------------------------------+
   |                       Dr. DiagnoSense                         |
   +---------------------------------------------------------------+
                     |                           |
                     v                           |
   +-----------------+--------------------------+------------------+
   |                    Data Collection and Preprocessing           |
   |                                                                |
   |         +-----------------+------------------+-----------------+
   |         |                 |                  |                 |
   |         v                 v                  v                 |
   |  Alzheimer's Disease  Brain Tumor     Breast Cancer     Heart Attack |
   |      (alzheimers)     (brain_tumor)    (breast_cancer) (heart_attack)|
   |         |                 |                  |                 |
   |         |                 |                  |                 |
   |         v                 v                  v                 |
   |   +------------------+ +------------------+ +------------------+
   |   |   ML Algorithms  | |   ML Algorithms  | |   ML Algorithms  |
   |   |   (if accuracy   | |   (if accuracy   | |   (if accuracy   |
   |   |   is good)       | |   is good)       | |   is good)       |
   |   |                  | |                  | |                  |
   |   +------------------+ +------------------+ +------------------+
   |         |                 |                  |                 |
   |         v                 v                  v                 |
   |   +------------------+ +------------------+ +------------------+
   |   | Pickle File (.pkl)| | Pickle File (.pkl)| | Pickle File (.pkl)|
   |   |     (Model)       | |     (Model)       | |     (Model)       |
   |   +------------------+ +------------------+ +------------------+
   |         |                 |                  |                 |
   |         |                 |                  |                 |
   |         v                 v                  v                 |
   |     App.py               App.py             App.py            App.py
   |         |                 |                  |                 |
   |         v                 v                  v                 |
   |     Streamlit.py       Streamlit.py        Streamlit.py       Streamlit.py
   |         |                 |                  |                 |
   +---------+-----------------+------------------+-----------------+
                                     |
                                     v
                              Web Application

```

## Contributing
We welcome contributions from the community to improve Dr DiagnoSense's accuracy and features. Feel free to fork this repository, make improvements, and submit a pull request.

## Disclaimer
Dr DiagnoSense is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## License
This project is licensed under the [Apache License 2.0](LICENSE).
