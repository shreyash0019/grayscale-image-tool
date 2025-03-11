# Colored Image to Black & White Image Converter

A simple Python script that takes a colored image filename as an argument, converts it into a grayscale image, and saves the output image file. This script demonstrates the basic usage of the Pillow library.

## Libraries Required

To run this script, you need to have the Pillow library installed. You can install it using pip:

```bash
pip install Pillow
```

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/<your-username>/image-to-bw-converter.git
    cd image-to-bw-converter
    ```

2. **Navigate to the Script's Folder**:
    Open the command prompt or terminal and navigate to the folder where the script is located.

3. **Run the Script**:
    Use the following command to run the script. Replace `<image_file_name>` with the name of the image file you want to convert.

    ```bash
    python bw_convert.py <image_file_name>
    ```

### Example

Here are some examples of how to run the script:

```bash
python bw_convert.py sample_image.jpg
python bw_convert.py sample_image.png
```

## Detailed Steps

1. **Importing Libraries**:
    - The script uses the Pillow library for image processing.

2. **Opening the Image**:
    - The script opens the image file provided as an argument.

3. **Converting to Grayscale**:
    - The script converts the opened image to grayscale using the `convert('L')` method.

4. **Saving the Grayscale Image**:
    - The script saves the converted grayscale image with a filename indicating that it is now black and white.

## Script Explanation

Here is a detailed explanation of the `bw_convert.py` script:

```python
from PIL import Image
import sys

def convert_to_bw(image_file):
    try:
        # Open the image file
        img = Image.open(image_file)
        # Convert the image to grayscale
        bw_img = img.convert('L')
        # Save the grayscale image
        bw_img.save(f"bw_{image_file}")
        print(f"Black & white image saved as bw_{image_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bw_convert.py <image_file_name>")
    else:
        image_file = sys.argv[1]
        convert_to_bw(image_file)
```

### Breakdown of the Script

- **Importing Libraries**:
    ```python
    from PIL import Image
    import sys
    ```

- **Function to Convert Image to Black & White**:
    ```python
    def convert_to_bw(image_file):
        try:
            # Open the image file
            img = Image.open(image_file)
            # Convert the image to grayscale
            bw_img = img.convert('L')
            # Save the grayscale image
            bw_img.save(f"bw_{image_file}")
            print(f"Black & white image saved as bw_{image_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
    ```

- **Main Block**:
    ```python
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python bw_convert.py <image_file_name>")
        else:
            image_file = sys.argv[1]
            convert_to_bw(image_file)
    ```

## Notes

- The script takes the image file name as a command-line argument.
- The output grayscale image is saved with the prefix `bw_` added to the original file name.
- Ensure the image file is in the same directory as the script or provide the full path to the image file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
