# SnAI Worksheet 13B – Exploring Python Libraries

## 1. What It Does

This project explores two Python libraries, pyfiglet and Pillow, and combines them to convert user-input text into ASCII art and generate an image containing the text.

## 2. Libraries Used

### 1. pyfiglet
- Converts normal text into ASCII art.
- Generates text banners using different font styles.

### 2. Pillow
- Creates and edits images using Python.
- Allows text to be drawn on images.
- Saves images in formats such as PNG.

## 3. Requirements

Install Python 3 on your system.

Install the required Python libraries:

```bash
python -m pip install pyfiglet Pillow
```

**Prerequisites:**
- Python 3
- pip (Python package installer)
- VS Code (optional)

## 4. How to Run

Clone or download this repository.

Run the following commands from the project folder:

**For v0.1 – pyfiglet:**

```bash
python v0.1/pyfiglet_demo.py
```

**For v0.2 – Pillow:**

```bash
python v0.2/pillow_demo.py
```

**For v0.3 – Combined Project:**

```bash
python v0.3/combined_project.py
```

## 5. Output

- **v0.1:** Displays text in ASCII art format.
- **v0.2:** Creates and saves a lavender PNG image.
- **v0.3:** Converts user-input text into ASCII art and places it on an image using Pillow.

The combined project saves the generated image as `combined_output.png`.

## 6. Limitations

- The project currently supports basic text-to-ASCII conversion.
- Image dimensions are fixed.
- The image styling is limited to basic colours and text.
- The project does not currently provide advanced image editing features.
