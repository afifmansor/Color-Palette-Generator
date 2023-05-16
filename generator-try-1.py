import streamlit as st
import pandas as pd
import altair as alt

# Function to generate bar chart from DataFrame
def generate_bar_chart(df):
    chart = alt.Chart(df).mark_bar().encode(
        x='Category',
        y='Value'
    ).properties(
        width=600,
        height=400
    )
    return chart

# Main Streamlit app code
def main():
    # Set app title and header
    st.set_page_config(page_title="Bar Chart Generator", page_icon=":bar_chart:")
    st.title("Bar Chart Generator")

    # Upload CSV file
    st.sidebar.title("Upload CSV file")
    file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    # If file is uploaded, read data and generate bar chart
    if file is not None:
        df = pd.read_csv(file)
        st.write("Original Data:")
        st.write(df)
        chart = generate_bar_chart(df)
        st.write("Bar Chart:")
        st.altair_chart(chart, use_container_width=True)
        
        # Add download link for bar chart data as CSV
        csv = df.to_csv(index=False)
        href = f'<a href="data:file/csv;base64,{b64encode(csv.encode()).decode()}" download="bar_chart_data.csv">Download Bar Chart Data</a>'
        st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()

