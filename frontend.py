import streamlit as st
import pandas as pd
import os

st.title("Cold Email Generator for B2C Startups")

uploaded_file = st.file_uploader("Upload your leads CSV file", type=["csv"])

if uploaded_file is not None:
    temp_path = os.path.join("temp_upload.csv")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Leads uploaded! Generating emails...")
    os.system(f"python main.py {temp_path}")

    if os.path.exists(temp_path):
        output_df = pd.read_csv(temp_path)
        st.dataframe(output_df)
        st.download_button("Download Emails", output_df.to_csv(index=False), "emails.csv", "text/csv")
