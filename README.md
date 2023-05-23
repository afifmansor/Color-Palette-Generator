The Color-Palette-Generator is a tool designed to generate color palettes from uploaded images. It allows users to upload multiple images and extracts the dominant colors from each image to create a color scheme. The tool utilizes the K-means clustering algorithm from the scikit-learn library to cluster the pixels of the uploaded images based on their color values.

Here's how the Color-Palette-Generator works:

1. User Interface: The tool provides a user-friendly interface using the Streamlit framework. It allows users to upload multiple images of their choice.

2. Image Processing: Once the images are uploaded, the tool uses the Python Imaging Library (PIL) to open and convert the images to the RGB color mode if they are not already in RGB format. The images are then resized to a smaller size for faster processing.

3. Color Extraction: The resized images are converted into numpy arrays, and the pixel values are reshaped into a 2D array. The K-means clustering algorithm is applied to these pixel arrays to identify the dominant colors. The number of dominant colors to be extracted can be specified by the user.

4. Color Scheme Generation: The RGB values of the dominant colors are converted to hexadecimal format to represent the color scheme. The file names of the uploaded images and their corresponding color schemes are stored in a pandas DataFrame.

5. Display and Download: The color schemes are displayed as a table using Streamlit, allowing users to visualize the generated palettes. Additionally, the tool provides a download button that allows users to download the color schemes as a CSV file, enabling further analysis or usage in other applications.

6. Temporary File Handling: The uploaded images are temporarily saved on the server and later removed to ensure clean-up and privacy.

Overall, the Color-Palette-Generator provides a convenient way for users to extract and explore dominant color schemes from their images. It can be useful for various applications such as graphic design, web development, or any project requiring color inspiration.


# Reference
### Color Identification in Images
https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71
