# 🌍 AI Air Quality + BI Analyst Intelligence System

🔗 Live App: https://airqualityproject-ts4tpyltpkpsdhhemvuzuz.streamlit.app/

---

## 📌 Overview
An AI-powered data analytics and air quality intelligence system that performs **end-to-end data science workflow** — from data ingestion to insights, visualization, and basic prediction.

This project simulates how a **real data analyst + ML system** works on environmental datasets.

---

## 🚀 Features

### 🔢 AQI Checker
- Instant AQI classification
- Health advisory system
- Visual AQI scale indicator

### 📊 BI Data Analyst Mode
- Dataset upload (CSV)
- Automated data profiling
- KPI dashboard (Avg, Max, Risk Level)
- Outlier detection (IQR method)
- Anomaly detection (statistical deviation)
- Trend analysis (rolling average)
- Regional comparison (best vs worst locations)
- Correlation analysis
- Downloadable processed dataset

---

## 🧠 Data Science Workflow Implemented

### 1. Data Collection
- Input via CSV upload (real-world air quality datasets)

### 2. Data Cleaning
- Column standardization
- Handling missing values using median imputation

### 3. Data Preprocessing
- Filtering numeric features
- Feature extraction (if date columns exist)
- Data type handling

### 4. Exploratory Data Analysis (EDA)
- Statistical summaries
- Trend visualization
- Correlation matrix
- Distribution understanding

### 5. Feature Engineering
- Derived metrics (average index, risk levels)
- Regional aggregation
- Rolling averages for time trends

### 6. Anomaly Detection
- IQR-based outlier detection
- Standard deviation-based anomaly detection

### 7. Insight Generation
- AI-based rule engine for pollution interpretation
- Identification of high-risk zones
- Pattern-based reasoning

---

## 🤖 Machine Learning Logic (Basic)

- **Trend Forecasting**: Rolling mean used for next-value approximation
- **Risk Classification**: Rule-based AQI categorization
- **Pattern Detection**: Statistical anomaly detection

*(Lightweight ML logic designed for real-time interaction)*

---

## 🛠 Tech Stack
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
