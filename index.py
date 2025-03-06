import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        ('meter', 'centimeter'): 100,
        ('centimeter', 'meter'): 0.01
    }
    
    if (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]
    else:
        return "Invalid conversion units"

# Streamlit UI
st.title("Length Converter")

value = st.number_input("Enter the length value:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Select the 'from' unit:", ["meter", "centimeter"])
to_unit = st.selectbox("Select the 'to' unit:", ["meter", "centimeter"])

if st.button("Convert"):
    result = length_converter(value, from_unit, to_unit)
    st.success(f"Converted value: {result} {to_unit}")

