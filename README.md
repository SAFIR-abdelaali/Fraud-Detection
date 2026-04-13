# Fraud Detection System

A machine learning solution designed to detect fraudulent transaction with high precision. This project moves beyond simple classification to address the "Class Imbalance" problem common in financial datasets.

## Overview
Financial fraud detection is a "needle in a haystack" problem. In this dataset, fraudulent transactions represent less than 0.1% of the total volume. This project implements a high-performance **XGBoost** model that achieves a **92% Precision** rate, successfully reducing false alarms (False Positives) by over 97% compared to baseline models.

## Dataset Link
[Fraud Detection Dataset on Kaggle](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)

## Key Innovations
* **Feature Engineering (`is_emptied`):** Identified a critical "smoking gun" pattern where accounts are perfectly drained to $0.00. Adding this binary feature improved model clarity significantly.
* **XGBoost Implementation:** Leveraged gradient boosting to capture complex, non-linear relationships between transaction amounts and account history.
* **Threshold Optimization:** Implemented a strict **0.99 classification threshold**. This ensures the system only flags transactions when it is extremely certain, protecting customer experience by minimizing wrongly blocked cards.

## Performance Metrics
After optimization and feature engineering, the model achieved:

| Metric | Score | Significance |
| :--- | :--- | :--- |
| **Precision** | **0.92** | 9 out of 10 flags are actual fraud. |
| **Recall** | **0.77** | Successfully catches the majority of fraud cases. |
| **F1-Score** | **0.84** | Strong balance between detection and accuracy. |
| **False Positives** | **109** | Out of 1.27M transactions, only 109 innocent users were flagged. |

## Technology Stack
* **Language:** Python 3.14.2
* **Core Libraries:** Pandas, NumPy, Scikit-Learn
* **ML Algorithm:** Logitic Regression(first), XGBoost (Extreme Gradient Boosting)
* **Visualization:** Matplotlib, Seaborn
* **Deployment:** Streamlit (Interactive Web Interface)
* **Model Persistence:** Joblib

## Project Structure
* `fraud_detection.ipynb`: Data exploration, feature engineering, and model training.
* `app.py`: Streamlit web application code.
* `fraud_model.pkl`: The serialized trained pipeline (Scaler + Encoder + XGBoost).
* `README.md`: Project documentation.

## How to Run
1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install pandas scikit-learn xgboost streamlit joblib numpy matplotlib
    ```
3.  **Train the model** (or use the provided `.pkl` file).
4.  **Launch the Dashboard:**
    ```bash
    streamlit run app.py
    ```

---
*Developed as a high-precision solution for modern digital banking safety.*