import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def main():
    st.title('CSV File Plotter')

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display basic dataframe info
        st.subheader('Uploaded Data Overview')
        st.write(df.head())

        # Column selection
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

        # Plotting options
        st.subheader('Plotting Options')

        # Scatter Plot
        scatter_plot = st.checkbox('Scatter Plot')
        if scatter_plot and len(numeric_columns) >= 2:
            x_col = st.selectbox('X-axis', numeric_columns)
            y_col = st.selectbox('Y-axis', [col for col in numeric_columns if col != x_col])

            fig, ax = plt.subplots()
            ax.scatter(df[x_col], df[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f'Scatter Plot: {x_col} vs {y_col}')
            st.pyplot(fig)

        # Histogram
        histogram_plot = st.checkbox('Histogram')
        if histogram_plot and numeric_columns:
            hist_col = st.selectbox('Column for Histogram', numeric_columns)

            fig, ax = plt.subplots()
            ax.hist(df[hist_col], bins='auto')
            ax.set_xlabel(hist_col)
            ax.set_ylabel('Frequency')
            ax.set_title(f'Histogram of {hist_col}')
            st.pyplot(fig)

        # Box Plot
        box_plot = st.checkbox('Box Plot')
        if box_plot and categorical_columns and numeric_columns:
            cat_col = st.selectbox('Categorical Column', categorical_columns)
            num_col = st.selectbox('Numeric Column', numeric_columns)

            fig, ax = plt.subplots()
            df.boxplot(column=num_col, by=cat_col, ax=ax)
            ax.set_title(f'Box Plot: {num_col} by {cat_col}')
            st.pyplot(fig)

        # Pie Chart
        pie_chart = st.checkbox('Pie Chart')
        if pie_chart and categorical_columns:
            pie_col = st.selectbox('Column for Pie Chart', categorical_columns)

            fig, ax = plt.subplots()
            df[pie_col].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
            ax.set_title(f'Pie Chart of {pie_col}')
            st.pyplot(fig)

        # Heatmap (Correlation)
        heatmap_plot = st.checkbox('Correlation Heatmap')
        if heatmap_plot and len(numeric_columns) > 1:
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
            ax.set_title('Correlation Heatmap')
            st.pyplot(fig)


if __name__ == '__main__':
    main()