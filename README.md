\# 🎨 AI Image Colorization



A deep learning project that automatically converts grayscale images into color images using a Convolutional Neural Network (CNN).



\## 📌 Project Overview



This project uses a trained CNN model to predict realistic colors for grayscale images.



The model takes a \*\*128 × 128 grayscale image\*\* as input and produces a \*\*128 × 128 RGB color image\*\* as output.



\## 🧠 Model Architecture



The project uses an encoder-decoder style CNN.



\* Input: 128 × 128 × 1 grayscale image

\* Convolutional layers for feature extraction

\* Max pooling for downsampling

\* UpSampling layers for image reconstruction

\* Final output: 128 × 128 × 3 RGB image



\### Model Parameters



\*\*1,330,307 trainable parameters\*\*



\## 📊 Training



The model was trained using:



\* Training images: 10,000

\* Validation images: 1,000

\* Image size: 128 × 128

\* Batch size: 32

\* Maximum epochs: 20

\* Early stopping: Enabled

\* Best validation model: Saved automatically



The best model achieved a validation loss of approximately \*\*0.00869\*\* during the final training run.



\## 🖼️ How It Works



```text

Grayscale Image

&#x20;      ↓

&#x20;  CNN Encoder

&#x20;      ↓

Feature Extraction

&#x20;      ↓

&#x20; CNN Decoder

&#x20;      ↓

Color Prediction

&#x20;      ↓

RGB Colorized Image

```



\## 🚀 Run the Application



Install the required packages:



```bash

pip install -r requirements.txt

```



Run the application:



```bash

python app.py

```



The Gradio interface allows the user to upload a grayscale image and generate a colorized result.



\## 📁 Project Structure



```text

AI-Image-Colorization/

│

├── app.py

├── best\_colorization\_model.keras

├── requirements.txt

└── README.md

```



\## 🛠️ Technologies Used



\* Python

\* TensorFlow / Keras

\* NumPy

\* Pillow

\* Gradio

\* Convolutional Neural Networks



\## 🎯 Project Goal



The goal of this project is to demonstrate how deep learning can be used for automatic image colorization and to provide a simple web interface for testing the trained model.



\## 👨‍💻 Project



AI Image Colorization — Deep Learning Project



