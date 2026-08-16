# AI Image Colorization

An AI-based image colorization project that converts grayscale images into color images using a Convolutional Neural Network (CNN) trained with TensorFlow/Keras.

## Project Overview

Image colorization is the process of adding realistic colors to grayscale images.

In this project, a CNN is trained to learn the relationship between grayscale images and their corresponding RGB color images. The trained model can take a grayscale image as input and generate a colorized RGB image.

The project also includes a simple Gradio web application that allows users to upload a grayscale image and view the generated colorized result.

## Google Colab Demo

The complete project, including dataset preparation, model training, evaluation, and image colorization, can be viewed in Google Colab.

**Open the Google Colab Notebook:**

https://colab.research.google.com/drive/1D5SEkBPLIO4oQmOd8NQ_NKIlJzKCQTSI?usp=sharing

The notebook contains:

* Dataset preparation
* CNN model architecture
* Model training
* Training and validation results
* Model saving
* Image colorization
* Final colorized output
* Gradio web application demonstration

For the best demonstration, open the notebook and use **Runtime -> Run all**.

## Features

* Upload a grayscale image
* CNN-based image colorization
* Generate a colorized RGB image
* Simple Gradio web interface
* Training and validation monitoring
* Saved trained Keras model
* GPU-supported training using Google Colab

## Model Architecture

The project uses an encoder-decoder style Convolutional Neural Network.

### Encoder

The encoder extracts important visual features from the grayscale input image using convolution and max-pooling layers.

### Decoder

The decoder gradually reconstructs the image using upsampling and convolution layers to produce a 3-channel RGB image.

### Model Summary

| Component         | Details                       |
| ----------------- | ----------------------------- |
| Input             | 128 x 128 x 1 grayscale image |
| Output            | 128 x 128 x 3 RGB image       |
| Framework         | TensorFlow / Keras            |
| Architecture      | CNN Encoder-Decoder           |
| Total Parameters  | 1,330,307                     |
| Training Images   | 10,000                        |
| Validation Images | 1,000                         |

## Dataset

The dataset was divided into training and validation sets.

### Training

* 10,000 grayscale images
* 10,000 corresponding color images

### Validation

* 1,000 grayscale images
* 1,000 corresponding color images

Images were resized to:

```text
128 x 128 pixels
```

The grayscale images were used as model inputs, while the corresponding RGB images were used as target outputs.

## Training

The model was trained using Google Colab with TensorFlow and GPU acceleration.

Training was configured for a maximum of 20 epochs with early stopping.

The best model was selected according to validation loss.

### Final Training Result

The best validation result achieved during training was approximately:

```text
Validation Loss: 0.00869
Validation MAE: 0.0641
```

The model restored the weights from the best-performing epoch.

## Training Progress

The model showed a gradual decrease in training and validation loss during training.

The training process used early stopping to prevent unnecessary training when the validation performance stopped improving.

## Colorization Result

The trained model successfully converts grayscale images into colorized images.

A final test image was processed using the trained model and saved as a colorized PNG image.

## Web Application

The project includes a Gradio-based web application.

The application:

1. Accepts a grayscale image.
2. Converts the image to grayscale.
3. Resizes it to 128 x 128 pixels.
4. Normalizes the input.
5. Passes it through the trained CNN.
6. Generates the color prediction.
7. Converts the prediction into an RGB image.
8. Displays the colorized result.

## Project Structure

```text
AI-Image-Colorization/
|
|-- app.py
|-- best_colorization_model.keras
|-- README.md
|-- requirements.txt
|-- .gitignore
```

### File Description

| File                            | Purpose                                                        |
| ------------------------------- | -------------------------------------------------------------- |
| `app.py`                        | Gradio web application and prediction code                     |
| `best_colorization_model.keras` | Trained CNN model                                              |
| `requirements.txt`              | Python dependencies                                            |
| `README.md`                     | Project documentation                                          |
| `.gitignore`                    | Prevents unnecessary files such as `venv/` from being uploaded |

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pillow
* Gradio
* Google Colab
* Git
* GitHub

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/nagavishwa-spidey/AI-Image-Colorization.git
```

### 2. Open the project directory

```bash
cd AI-Image-Colorization
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment on Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The Gradio application will be available locally at:

```text
http://127.0.0.1:7860
```

## Project Objective

The main objective of this project is to demonstrate how deep learning and convolutional neural networks can be used to automatically restore color information in grayscale images.

The project combines:

**Deep Learning + Computer Vision + Web Application**

into a single working application.

## Future Improvements

Possible improvements include:

* Training with a larger and more diverse dataset
* Using a deeper encoder-decoder architecture
* Adding skip connections
* Using perceptual or color-aware loss functions
* Improving color accuracy and realism
* Deploying the application to a cloud platform
* Supporting higher-resolution images
* Comparing different CNN architectures

## Project Resources

### GitHub Repository

https://github.com/nagavishwa-spidey/AI-Image-Colorization

### Google Colab Notebook

https://colab.research.google.com/drive/1D5SEkBPLIO4oQmOd8NQ_NKIlJzKCQTSI?usp=sharing

## Author

**Nagavishwa**

GitHub:

https://github.com/nagavishwa-spidey

## Conclusion

This project demonstrates a complete AI-based image colorization workflow, from dataset preparation and CNN training to model evaluation and a user-friendly web interface.

The trained model can take a grayscale image and generate a corresponding colorized image.

---

**AI Image Colorization - Deep Learning and Computer Vision Project**
