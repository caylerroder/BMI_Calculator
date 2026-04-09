import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator")
st.markdown("### Body Mass Index Calculator")
st.markdown("---")

weight = st.number_input("**Weight (kg)**", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("**Height (meters)**", min_value=0.5, max_value=3.0, value=1.75, step=0.01)

if st.button("Calculate BMI", use_container_width=True):
    bmi = weight / (height * height)

    st.markdown("---")
    st.markdown(f"## Your BMI: **{bmi:.2f}**")

    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
        advice = "Consider consulting a nutritionist to gain healthy weight."
    elif 18.5 <= bmi < 25.0:
        category = "Normal weight"
        color = "green"
        advice = "Great job! Maintain your healthy lifestyle."
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
        color = "orange"
        advice = "Consider a balanced diet and regular exercise."
    else:
        category = "Obese"
        color = "red"
        advice = "Please consult a healthcare professional for guidance."

    st.markdown(f"### Category: :{color}[**{category}**]")
    st.info(f"💡 {advice}")

    st.markdown("---")
    st.markdown("#### BMI Reference Table")
    st.table({
        "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
        "BMI Range": ["< 18.5", "18.5 – 24.9", "25.0 – 29.9", "≥ 30.0"]
    })

st.markdown("---")
st.caption("Formula: BMI = Weight (kg) / Height² (m²)")
