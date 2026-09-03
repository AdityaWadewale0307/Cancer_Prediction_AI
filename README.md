# Cancer_Prediction_AI
A machine-learning powered web application that predicts cancer classification using a trained **Random Forest Classifier**. The project provides an interactive **Streamlit** interface where users can enter patient and tumor-related information and receive a model prediction with probability information.

## 🚀 Live Demo

[👉 Try the Live Application](https://cancerpredictionai-jfobeen7fo7ddvxk8rwjg9.streamlit.app/)


## 📌 Project Overview

**Cancer Prediction AI** is an end-to-end machine learning project that demonstrates how a trained classification model can be integrated into an interactive web application.

The application allows a user to:

- Enter patient information such as age and gender.
- Enter tumor-related input features.
- Submit the information through an interactive Streamlit interface.
- Generate a prediction using a trained Random Forest model.
- View prediction/probability information in an easy-to-understand dashboard.

The project combines **Machine Learning, Python, Model Deployment, and Streamlit UI development** into one complete application.

## ✨ Features

### 🤖 Machine Learning
- Random Forest Classifier for classification.
- Pre-trained model saved using `joblib`.
- Model loaded directly by the Streamlit application.
- Supports prediction from user-provided feature values.

### 🖥️ Interactive Web Application
- Built with Streamlit.
- Clean and responsive dashboard-style interface.
- Patient Information section.
- Tumor Information section.
- Prediction section.
- Probability visualization.
- Sidebar containing model information and input-feature details.

### 📊 Model Information
- **Algorithm:** Random Forest Classifier
- **Number of input features:** 17
- **Model format:** Joblib (`.joblib`)
- **Application framework:** Streamlit

- ## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas / NumPy | Data processing and numerical operations |
| Scikit-learn | Machine learning model |
| Random Forest | Classification algorithm |
| Joblib | Model serialization and loading |
| Streamlit | Interactive web application |
| Jupyter Notebook | Data analysis and model development |
| Git & GitHub | Version control and project hosting |

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning & Preprocessing
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Random Forest Classifier
   ↓
Model Evaluation
   ↓
Save Trained Model (.joblib)
   ↓
Streamlit Application
   ↓
User Input
   ↓
Model Prediction
   ↓
Prediction & Probability Display
```

## 🧠 Machine Learning Model

The application uses a **Random Forest Classifier**.

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce a more robust classification result.

### Why Random Forest?

Random Forest was selected because it:

- Handles classification problems effectively.
- Can work with multiple input features.
- Captures nonlinear relationships between features.
- Is generally less prone to overfitting than a single decision tree.
- Provides probability estimates for classification.
- Works well as a baseline model for many tabular datasets.

### Model Pipeline

The general machine-learning workflow used in this project is:

1. Load the dataset.
2. Inspect and understand the data.
3. Perform data preprocessing.
4. Select the required features.
5. Split the dataset into training and testing sets.
6. Train the Random Forest Classifier.
7. Evaluate the model.
8. Save the trained model using Joblib.
9. Load the saved model inside the Streamlit application.
10. Generate predictions from user input.

---

## 🎨 Streamlit Application

The application has been designed as an interactive dashboard.

### Sidebar

The sidebar provides information about:

- About the Model
- Machine Learning Algorithm
- Number of input features
- General project information

### Main Dashboard

The main page contains:

#### 👤 Patient Information
Users can enter basic patient-related information such as:

- Age
- Gender

#### 🔬 Tumor Information
Users can enter the tumor-related features required by the trained model.

#### 📈 Prediction Output
After submitting the information, the application generates the model prediction and probability information.

## 📋 Requirements

The project requires Python and the packages listed in `requirements.txt`.

Example:

```text
scikit-learn==1.3.0
joblib
numpy
streamlit
```
For reproducibility, it is recommended to pin package versions when deploying the application.

## 🎯 Learning Objectives

This project demonstrates practical knowledge of:

- Python programming
- Data preprocessing
- Exploratory data analysis
- Feature selection
- Supervised machine learning
- Random Forest classification
- Model training and evaluation
- Model serialization using Joblib
- Streamlit application development
- Interactive UI design
- Git and GitHub
- Machine learning model deployment

---

## 🔮 Future Improvements

Possible improvements for future versions include:

- Add more machine-learning algorithms such as Logistic Regression, SVM, XGBoost, and Gradient Boosting.
- Compare model performance using multiple evaluation metrics.
- Add confusion matrix and ROC-AUC visualizations.
- Add feature importance visualization.
- Improve input validation and error handling.
- Add a dedicated model-performance page.
- Add an interactive data-analysis page.
- Add prediction history.
- Improve mobile responsiveness.
- Add automated model retraining.
- Add explainable-AI features such as SHAP.
- Add a more comprehensive deployment pipeline.

---

## 👨‍💻 Author

**Aditya Wadewale**

GitHub: **AdityaWadewale0307**

---

## ⭐ Project Purpose

The main purpose of this project is to demonstrate how a machine-learning classification model can be converted into a practical, interactive web application.

It combines the complete workflow:

**Data → Machine Learning → Model Saving → Streamlit UI → Prediction → Deployment**
