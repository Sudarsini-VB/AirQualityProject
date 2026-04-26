# =========================
# 🌍 AI AIR QUALITY + BI ANALYST SYSTEM (FINAL UI FIXED)
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AI AQI + BI System", layout="wide")

st.title("🌍 AI Air Quality + Data Analyst Intelligence System")
st.write("Interactive analytics + AI insights + dynamic dashboard")

st.markdown("---")

mode = st.radio("Select Mode", ["🔢 AQI Checker", "📊 BI Data Analyst"])

# =========================================================
# 🔢 AQI CHECKER
# =========================================================
if mode == "🔢 AQI Checker":

    st.subheader("🔢 AQI Real-Time Checker")

    aqi = st.slider("Select AQI Value", 0, 500, 100)

    def classify(aqi):
        if aqi <= 50:
            return "Good 🟢", "#00c853"
        elif aqi <= 100:
            return "Moderate 🟡", "#ffc107"
        elif aqi <= 200:
            return "Poor 🟠", "#ff9800"
        elif aqi <= 300:
            return "Very Poor 🔴", "#f44336"
        else:
            return "Severe ☠️", "#4a148c"

    label, color = classify(aqi)

    st.markdown(f"""
        <div style="
            background:{color};
            padding:25px;
            border-radius:15px;
            text-align:center;
            color:white;
            font-size:26px;
            font-weight:bold;">
            AQI: {aqi} <br> {label}
        </div>
    """, unsafe_allow_html=True)

    st.progress(aqi / 500)

# =========================================================
# 📊 BI DATA ANALYST MODE
# =========================================================
else:

    file = st.file_uploader("📁 Upload Dataset (CSV)", type=["csv"])

    if file:

        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()

        st.success("Dataset Loaded Successfully 🚀")

        if "From Date" in df.columns:
            df["From Date"] = pd.to_datetime(df["From Date"], errors="coerce")
            df["Year"] = df["From Date"].dt.year
            df["Month"] = df["From Date"].dt.month

        numeric_df = df.select_dtypes(include=np.number)

        # =========================
        # SUMMARY
        # =========================
        st.subheader("📌 Analyst Summary Report")

        loc_cols = ["City", "State", "Location", "Station", "District"]
        loc = next((c for c in loc_cols if c in df.columns), None)

        location_info = df[loc].mode()[0] if loc else "Not Available"

        if "From Date" in df.columns:
            start_date = df["From Date"].min()
            end_date = df["From Date"].max()
        else:
            start_date, end_date = "N/A", "N/A"

        st.info(f"""
        📍 Location: {location_info}  
        📅 Date Range: {start_date} → {end_date}  
        📊 Records: {df.shape[0]}  
        """)

        st.markdown("---")

        # =========================
        # FILTER
        # =========================
        col1, col2 = st.columns(2)

        if "Year" in df.columns:
            year = col1.selectbox("Select Year", ["All"] + sorted(df["Year"].dropna().unique()))
            if year != "All":
                df = df[df["Year"] == year]

        selected_col = col2.selectbox("Select Metric", numeric_df.columns)

        st.markdown("---")

        # =========================
        # KPI
        # =========================
        st.subheader("📊 KPI Dashboard")

        avg = df[selected_col].mean()
        max_val = df[selected_col].max()
        min_val = df[selected_col].min()

        c1, c2, c3 = st.columns(3)

        c1.metric("Average", round(avg, 2))
        c2.metric("Max", round(max_val, 2))
        c3.metric("Min", round(min_val, 2))

        st.markdown("---")

        # =========================
        # 📈 TREND (FIXED SIZE)
        # =========================
        st.subheader("📈 Trend Analysis")

        fig, ax = plt.subplots(figsize=(3, 2))  # 👈 MEDIUM SIZE
        df[selected_col].rolling(10).mean().plot(ax=ax)
        ax.set_title("Smoothed Trend")

        st.pyplot(fig, use_container_width=False)

        # 🔍 Zoom view
        with st.expander("🔍 Click to View Full Chart"):
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            df[selected_col].plot(ax=ax2)
            st.pyplot(fig2)

        st.markdown("---")

        # =========================
        # 🏙 REGION (SMALL CHART)
        # =========================
        if loc:

            st.subheader("🏙 Region Analysis")

            ranking = df.groupby(loc)[selected_col].mean().sort_values(ascending=False)

            st.dataframe(ranking.head())

            fig_bar, ax_bar = plt.subplots(figsize=(6, 3))
            ranking.head(10).plot(kind="bar", ax=ax_bar)
            ax_bar.set_title("Top Regions")

            st.pyplot(fig_bar, use_container_width=False)

            with st.expander("🔍 Expand Region Chart"):
                fig_big, ax_big = plt.subplots(figsize=(10, 5))
                ranking.plot(kind="bar", ax=ax_big)
                st.pyplot(fig_big)

        st.markdown("---")

        # =========================
        # 🔥 HEATMAP (FIXED)
        # =========================
        st.subheader("🔥 Correlation Heatmap")

        fig3, ax3 = plt.subplots(figsize=(3, 2))  # 👈 MEDIUM
        sns.heatmap(numeric_df.corr(), cmap="coolwarm", ax=ax3)

        st.pyplot(fig3, use_container_width=False)

        with st.expander("🔍 Expand Heatmap"):
            fig4, ax4 = plt.subplots(figsize=(10, 7))
            sns.heatmap(numeric_df.corr(), cmap="coolwarm", ax=ax4)
            st.pyplot(fig4)

        st.markdown("---")

        # =========================
        # AI INSIGHTS
        # =========================
        st.subheader("🧠 AI Insights")

        insights = []

        if avg > 150:
            insights.append("🔴 High pollution detected")
        elif avg > 80:
            insights.append("🟠 Moderate pollution")
        else:
            insights.append("🟢 Air quality safe")

        for i in insights:
            st.write("•", i)

        st.markdown("---")

        # =========================
        # DOWNLOAD
        # =========================
        st.download_button(
            "📥 Download Data",
            df.to_csv(index=False).encode("utf-8"),
            "report.csv"
        )

    else:
        st.info("⬆ Upload dataset to start analysis")
