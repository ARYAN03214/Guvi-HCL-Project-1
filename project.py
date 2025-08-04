import streamlit as st
import pandas as pd
import seaborn as sns

st.title("📊 Correlation Analysis Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Filter numeric columns
    numeric_df = df.select_dtypes(include='number')

    # Show correlation heatmap
    st.subheader("🔹 Correlation Heatmap")
    corr_matrix = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Scatterplot section
    st.subheader("🔹 Scatterplot for Variable Pairs")
    cols = numeric_df.columns.tolist()

    x_axis = st.selectbox("Select X-axis variable", cols)
    y_axis = st.selectbox("Select Y-axis variable", cols)

    if x_axis and y_axis:
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=numeric_df, x=x_axis, y=y_axis, ax=ax2)
        ax2.set_title(f"{x_axis} vs {y_axis}")
        st.pyplot(fig2)
