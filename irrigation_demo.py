import streamlit as st

st.set_page_config(page_title="Smart Irrigation Controller", layout="centered")

st.title("Smart Irrigation Controller - Demo Mode")

# Soil Moisture Slider
moisture = st.slider("Soil Moisture (%)", 0, 100, 55)

# Rain forecast input
rain = st.radio("Rain Expected?", ["Yes", "No"])

# Crop type input
crop = st.selectbox("Crop Type", ["tomato", "rice", "Wheat"])

# Crop moisture thresholds
thresholds = {"tomato": 60, "rice": 80, "Wheat": 50}

# Irrigation decision
irrigate = moisture < thresholds[crop] and rain == "No"

# Display irrigation status
if irrigate:
    st.success("Irrigation ON (Relay + LED ON)")
    st.markdown("![LED ON](https://i.imgur.com/N0Q7m6n.gif)")
else:
    st.info("Irrigation OFF (Relay + LED OFF)")
    st.markdown("![LED OFF](https://i.imgur.com/qeTP0U7.png)")

# Explain decision
st.write(f"Moisture: {moisture}%, Threshold for {crop}: {thresholds[crop]}%, Rain expected: {rain}")
