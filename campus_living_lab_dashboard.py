import streamlit as st
import pandas as pd
import random
import time

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Campus Living Lab AI",
    page_icon="🏙️",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS (Frontend Design)
# -------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.metric-card {
    background: linear-gradient(135deg, #1f2933, #111827);
    padding: 20px;
    border-radius: 16px;
    color: white;
    text-align: center;
}
.metric-value {
    font-size: 32px;
    font-weight: bold;
}
.metric-label {
    color: #9ca3af;
}
.section {
    background-color: #111827;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
}
.title {
    font-size: 38px;
    font-weight: 700;
}
.subtitle {
    color: #9ca3af;
    margin-bottom: 20px;
}
.alert-high {
    background-color: #7f1d1d;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
}
.alert-medium {
    background-color: #78350f;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
}
.alert-low {
    background-color: #064e3b;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Title
# -------------------------------------------------
st.markdown("<div class='title'>🏙️ Campus Living Lab AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Turning campuses into living labs for traffic, utilities, safety & planning</div>",
    unsafe_allow_html=True
)

# -------------------------------------------------
# Simulated Arduino Data
# -------------------------------------------------
def generate_data():
    zones = ["Main Gate", "Hostel Area", "Academic Block", "Cafeteria"]
    rows = []

    for z in zones:
        footfall = random.randint(60, 280)
        occupancy = random.randint(30, 100)
        power = random.randint(20, 90)

        if footfall > 200:
            risk = "High"
        elif footfall > 120:
            risk = "Medium"
        else:
            risk = "Low"

        rows.append({
            "Zone": z,
            "Footfall": footfall,
            "Occupancy": occupancy,
            "Power": power,
            "Risk": risk
        })

    return pd.DataFrame(rows)

df = generate_data()

# -------------------------------------------------
# Metrics
# -------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{df['Footfall'].sum()}</div>
        <div class='metric-label'>Total Footfall</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{int(df['Occupancy'].mean())}%</div>
        <div class='metric-label'>Avg Occupancy</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{(df['Risk'] == 'High').sum()}</div>
        <div class='metric-label'>High Risk Zones</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-value'>{len(df)}</div>
        <div class='metric-label'>Active Zones</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# Traffic Section
# -------------------------------------------------
st.markdown("<div class='section'><h3>🚦 Traffic & Mobility</h3></div>", unsafe_allow_html=True)
st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# Safety Alerts
# -------------------------------------------------
st.markdown("<div class='section'><h3>🛡️ Safety Alerts</h3></div>", unsafe_allow_html=True)

for _, row in df.iterrows():
    if row["Risk"] == "High":
        st.markdown(
            f"<div class='alert-high'>🚨 High crowd risk at <b>{row['Zone']}</b></div>",
            unsafe_allow_html=True
        )
    elif row["Risk"] == "Medium":
        st.markdown(
            f"<div class='alert-medium'>⚠️ Moderate crowding at <b>{row['Zone']}</b></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='alert-low'>✅ {row['Zone']} is safe</div>",
            unsafe_allow_html=True
        )

# -------------------------------------------------
# Planning Insights
# -------------------------------------------------
st.markdown("<div class='section'><h3>🏗️ Planning Insights</h3></div>", unsafe_allow_html=True)

for _, row in df.iterrows():
    if row["Footfall"] > 220:
        st.info(f"📌 Consider infrastructure upgrade near {row['Zone']}")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption(
    "Campus as a Living Lab"
)

# -------------------------------------------------
# Auto Refresh
# -------------------------------------------------
time.sleep(20)
st.rerun()
