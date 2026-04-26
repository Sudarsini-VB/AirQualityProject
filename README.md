# 🌍 AI Air Quality + BI Analyst Intelligence System

🔗 Live App: https://airqualityproject-faqvocetvzeh3sw4xeutpu.streamlit.app/

---

## 📌 Overview
An AI-powered interactive system that performs **end-to-end data analysis, visualization, and intelligent insights** for air quality datasets.

The application combines **AQI evaluation + BI dashboard + data science workflow** into a single platform, enabling users to explore pollution data like a professional data analyst.

---

## 🚀 Features

### 🔢 AQI Checker (Interactive UI)
- Real-time AQI input using slider
- Instant classification (Good → Severe)
- Health advisory based on AQI level
- Visual AQI scale (progress indicator)
- Clean UI with dynamic feedback

---

### 📊 BI Data Analyst Mode (Full Automation)

#### 📌 Dataset Understanding
- Auto-detects dataset structure (rows, columns)
- Identifies location columns (City/State/Station)
- Displays meaning of pollution parameters:
  - PM2.5, PM10 → Particulate matter
  - NO2 → Vehicle emissions
  - SO2 → Industrial pollution
  - CO → Carbon monoxide
  - O3 → Ozone
  - WS → Wind speed

---

#### 🎛 Dynamic Filters (Interactive)
- Year filter (auto-generated from dataset)
- Date range filter (if date column exists)
- Metric selector (user selects any column)
- Fully interactive dashboard (updates instantly)

---

#### 📊 KPI Dashboard
- Average value
- Maximum value
- Minimum value
- Dynamic based on selected metric

---

#### 📈 Interactive Data Visualization
- Rolling mean trend (smoothed analysis)
- Expandable full dataset view
- Column-based visualization (user-controlled)
- Auto-updates when filters change

---

#### ⚠️ Outlier Detection
- IQR-based statistical method
- Detects extreme values/spikes
- Displays abnormal data points

---

#### 🧠 Anomaly Detection
- Standard deviation-based detection
- Identifies unusual patterns in data

---

#### 🏙 Region Analysis
- Auto-detects location column
- Shows:
  - Worst regions (high pollution)
  - Best regions (low pollution)
- Bar chart visualization for comparison

---

#### 🔥 Correlation Analysis
- Heatmap showing relationships between variables
- Helps identify pollution dependencies

---

#### 🧠 AI Insights Engine
- Automatically interprets dataset
- Detects:
  - High pollution patterns
  - Urban/industrial impact
  - Risk levels
- Highlights worst affected region

---

#### 📊 Overall Dataset Insight
- Displays full dataset trend (without filters)
- Helps compare filtered vs overall data

---

#### 📥 Export Feature
- Download filtered dataset as CSV
- Useful for reporting and further analysis

---

## 🧠 Data Science Workflow Implemented

### 1. Data Collection
- User uploads real-world dataset (CSV)

### 2. Data Cleaning
- Column normalization
- Missing value handling (median imputation)

### 3. Data Preprocessing
- Numeric feature extraction
- Date feature engineering (Year, Month)
- Data filtering

### 4. Exploratory Data Analysis (EDA)
- Statistical summaries
- Trend visualization
- Correlation matrix

### 5. Feature Engineering
- Rolling averages for smoothing
- Aggregation by region
- Derived KPIs

### 6. Outlier & Anomaly Detection
- IQR method
- Standard deviation method

### 7. Insight Generation
- Rule-based AI interpretation
- Pollution reasoning
- Risk classification

---

## 🤖 Machine Learning Logic (Lightweight)

- Trend smoothing using rolling mean
- Statistical anomaly detection
- Rule-based classification (AQI levels)

Designed for **real-time performance and interactivity**

---

## 🛠 Tech Stack
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
