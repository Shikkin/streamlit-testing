import streamlit as st

st.set_page_config(layout="wide")

st.markdown('''### **ENCODING APP via streamlit (*testing*)**''')

with st.container(border=True):
    st.markdown("#### HOUSEHOLD ADDRESS")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Latitude", max_chars=12)
    with col2:
        st.text_input("Longitude", max_chars=12)

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Province")
    with col2:
        st.text_input("Municipality")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Barangay")
    with col2:
        st.text_input("Sitio")

    col1, col2 = st.columns([0.82,0.18])
    with col2:
        st.checkbox("Keep Data for Next Household")