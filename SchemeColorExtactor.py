import streamlit as st
import base64
import os
from PIL import Image
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def extract_color_scheme(image_path, num_colors):
    # Load the image using PIL
    image = Image.open(image_path)

    # Convert the image to RGB mode if it's not already in RGB
    image = image.convert("RGB")

    # Resize the image to a smaller size for faster processing
    resized_image = image.resize((100, 100))

    # Convert the resized image to a numpy array
    image_array = np.array(resized_image)

    # Reshape the image array to a 2D array of pixels
    pixel_array = image_array.reshape(-1, 3)

    # Perform K-means clustering to find the dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixel_array)
    colors = kmeans.cluster_centers_

    # Convert the colors to integer values
    colors = colors.astype(int)

    return colors


def generate_color_scheme_df(file_paths, num_colors):
    color_schemes = []

    for file_path in file_paths:
        try:
            # Extract color scheme from each image
            colors = extract_color_scheme(file_path, num_colors)

            # Convert the colors to hexadecimal format
            hex_colors = ['#%02x%02x%02x' % (color[0], color[1], color[2]) for color in colors]

            # Store the file name and color scheme in a dictionary
            color_scheme = {'File Name': file_path, 'Color Scheme': hex_colors}
            color_schemes.append(color_scheme)
        except Exception as e:
            print(f"Error processing image {file_path}: {str(e)}")

    # Create a pandas DataFrame from the color schemes
    df = pd.DataFrame(color_schemes)

    return df


def save_color_schemes_to_csv(df, output_path):
    # Save the DataFrame to an Excel file
    df.to_csv(output_path, index=False)


def main():
    image = Image.open('path/to/your/invoke_logo.jpg')  
    st.image(image, caption="Invoke Logo", use_column_width=True)
    st.title("Image Color Scheme Generator")
    st.write("Upload images to generate color schemes.")

    # Allow the user to upload multiple images
    uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True)

    if uploaded_files:
        st.write("Generating color schemes...")

        # Process the uploaded images and generate the color schemes DataFrame
        file_paths = []
        for uploaded_file in uploaded_files:
            # Save the uploaded file temporarily
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
                file_paths.append(uploaded_file.name)

        df = generate_color_scheme_df(file_paths, num_colors=5)

        # Display the color schemes as a table
        st.write(df)

        # Allow the user to download the color schemes as a CSV file
        csv_data = df.to_csv(index=False)
        b64 = base64.b64encode(csv_data.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="color_schemes.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

        # Remove the temporary uploaded files
        for file_path in file_paths:
            os.remove(file_path)


if __name__ == "__main__":
    main()
