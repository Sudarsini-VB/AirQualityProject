# =========================
# 🌍 AI AIR QUALITY + BI ANALYST SYSTEM (FINAL UPGRADED VERSION)
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AI AQI + BI System", layout="wide")

st.title("🌍 AI Air Quality + Data Analyst Intelligence System")
st.write("Choose mode: AQI Checker or Full Dataset Analytics")

st.markdown("---")

# =========================
# MODE SELECTION
# =========================
mode = st.radio("Select Mode", ["🔢 AQI Checker", "📊 BI Data Analyst"])

# =========================================================
# 🔢 AQI CHECKER MODE
# =========================================================
if mode == "🔢 AQI Checker":

    st.markdown("""
        <style>
        .aqi-box {
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            color: white;
            font-size: 26px;
            font-weight: bold;
            margin-top: 20px;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
        }
        .good { background: linear-gradient(90deg, #00c853, #64dd17); }
        .moderate { background: linear-gradient(90deg, #ffeb3b, #ffc107); color:black; }
        .poor { background: linear-gradient(90deg, #ff9800, #ff5722); }
        .verypoor { background: linear-gradient(90deg, #f44336, #b71c1c); }
        .severe { background: linear-gradient(90deg, #4a148c, #000000); }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("🔢 AQI Real-Time Checker")

    aqi = st.slider("Select AQI Value", 0, 500, 100)

    def get_style(aqi):
        if aqi <= 50:
            return "Good 🟢", "good", "Clean air 🌿 Safe for all"
        elif aqi <= 100:
            return "Moderate 🟡", "moderate", "Acceptable air 🙂"
        elif aqi <= 200:
            return "Poor 🟠", "poor", "Breathing discomfort 😷"
        elif aqi <= 300:
            return "Very Poor 🔴", "verypoor", "Health risk 🚨"
        else:
            return "Severe ☠️", "severe", "Dangerous air ⚠️"

    label, style, desc = get_style(aqi)

    st.markdown(f"""
        <div class="aqi-box {style}">
            AQI VALUE: {aqi} <br>
            STATUS: {label}
        </div>
    """, unsafe_allow_html=True)

    st.info(desc)

    st.subheader("💡 Health Advisory")

    if aqi <= 50:
        st.success("✔ Excellent air quality")
    elif aqi <= 100:
        st.warning("✔ Safe but monitor exposure")
    elif aqi <= 200:
        st.warning("⚠ Wear mask outdoors")
    elif aqi <= 300:
        st.error("🚨 Avoid outdoor activity")
    else:
        st.error("☠️ Stay indoors immediately")

    st.subheader("📊 AQI Scale")

    st.progress(aqi / 500)

    st.caption("0 = Clean 🟢 | 500 = Hazardous ☠️")

# =========================================================
# 📊 BI DATA ANALYST MODE (FULL FIXED UX VERSION)
# =========================================================
else:

    file = st.file_uploader("📁 Upload Dataset (CSV)", type=["csv"])

    if file:

        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()

        st.success("Dataset Loaded Successfully 🚀")

        numeric_df = df.select_dtypes(include=np.number)

        # =========================
        # DATA PROFILING
        # =========================
        st.subheader("📊 Data Profiling Report")

        profile = pd.DataFrame({
            "Data Type": df.dtypes,
            "Missing Values": df.isnull().sum(),
            "Missing %": (df.isnull().sum() / len(df)) * 100,
            "Unique Values": df.nunique()
        })

        st.dataframe(profile, use_container_width=True)

        st.markdown("---")

        # =========================
        # KPI DASHBOARD
        # =========================
        st.subheader("📌 KPI Dashboard")

        avg = numeric_df.mean().mean()
        max_val = numeric_df.max().max()

        col1, col2, col3 = st.columns(3)

        col1.metric("Average Value", round(avg, 2))
        col2.metric("Maximum Value", round(max_val, 2))
        col3.metric(
            "Risk Level",
            "Good 🟢" if avg <= 50 else
            "Moderate 🟡" if avg <= 100 else
            "Poor 🟠" if avg <= 200 else
            "Very Poor 🔴"
        )

        st.markdown("---")

        col = numeric_df.columns[0]

        # =========================
        # TREND ANALYSIS (SMALL + EXPAND)
        # =========================
        st.subheader("📈 Trend Analysis")

        fig, ax = plt.subplots(figsize=(6, 3))
        df[col].rolling(10).mean().plot(ax=ax)
        ax.set_title("Smoothed Trend")

        st.pyplot(fig, use_container_width=False)

        with st.expander("🔍 Expand Full Trend View"):
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            df[col].plot(ax=ax2)
            ax2.set_title("Full Trend")
            st.pyplot(fig2)

        st.markdown("---")

        # =========================
        # OUTLIERS
        # =========================
        st.subheader("⚠️ Outlier Detection")

        q1 = numeric_df[col].quantile(0.25)
        q3 = numeric_df[col].quantile(0.75)
        iqr = q3 - q1

        outliers = df[
            (numeric_df[col] < (q1 - 1.5 * iqr)) |
            (numeric_df[col] > (q3 + 1.5 * iqr))
        ]

        st.write("Outliers detected:", len(outliers))
        st.dataframe(outliers.head(), use_container_width=True)

        st.markdown("---")

        # =========================
        # ANOMALY DETECTION
        # =========================
        st.subheader("🧠 Anomaly Detection")

        mean = df[col].mean()
        std = df[col].std()

        anomalies = df[
            (df[col] > mean + 2 * std) |
            (df[col] < mean - 2 * std)
        ]

        st.write("Anomalies detected:", len(anomalies))
        st.dataframe(anomalies.head(), use_container_width=True)

        st.markdown("---")

        # =========================
        # REGION ANALYSIS
        # =========================
        st.subheader("🏙 Region Analysis")

        loc_cols = ["City", "State", "Location", "Station", "District"]
        loc = next((c for c in loc_cols if c in df.columns), None)

        if loc:
            ranking = df.groupby(loc)[col].mean().sort_values(ascending=False)

            st.write("🔥 Worst Regions")
            st.dataframe(ranking.head(), use_container_width=True)

            st.write("🟢 Best Regions")
            st.dataframe(ranking.tail(), use_container_width=True)

            st.bar_chart(ranking.head(10))

            with st.expander("📊 Expand Full Region Chart"):
                st.bar_chart(ranking)

        st.markdown("---")

        # =========================
        # CORRELATION MATRIX (FIXED SIZE)
        # =========================
        st.subheader("🔥 Correlation Matrix")

        fig3, ax3 = plt.subplots(figsize=(5, 4))
        ax3.imshow(numeric_df.corr(), cmap="coolwarm")
        ax3.set_title("Correlation Heatmap")

        st.pyplot(fig3, use_container_width=False)

        with st.expander("🔍 Expand Heatmap"):
            fig4, ax4 = plt.subplots(figsize=(10, 7))
            sns.heatmap(numeric_df.corr(), cmap="coolwarm", ax=ax4)
            st.pyplot(fig4)

        st.markdown("---")

        # =========================
        # INSIGHTS
        # =========================
        st.subheader("🧠 AI Insights")

        insights = []

        if avg > 150:
            insights.append("High pollution system detected (industrial + traffic)")
        else:
            insights.append("Air quality is within acceptable range")

        if loc:
            insights.append(f"Worst region: {ranking.index[0]}")

        for i in insights:
            st.write("•", i)

        st.markdown("---")

        # =========================
        # DOWNLOAD
        # =========================
        st.download_button(
            "📥 Download Report",
            df.to_csv(index=False).encode("utf-8"),
            "ai_bi_report.csv"
        )

    else:
        st.info("⬆ Upload dataset to start analysis")
