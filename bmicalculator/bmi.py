import streamlit as st

st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (m):", min_value=0.1)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)  # yahan pe bmi define kiya gaya
    st.write(f"Your BMI is: {bmi:.2f}")

    # Conditions
    if bmi <= 18.5:
        st.warning("You are underweight.")
    elif 18.5 < bmi <= 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi <= 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
