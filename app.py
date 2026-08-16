import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "best_colorization_model.keras"

print("Loading model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")


def colorize_image(image):
    if image is None:
        return None

    gray = image.convert("L")
    gray_resized = gray.resize((128, 128))

    gray_array = np.array(gray_resized, dtype=np.float32) / 255.0
    input_image = gray_array[np.newaxis, ..., np.newaxis]

    prediction = model.predict(input_image, verbose=0)

    colorized = prediction[0]

    colorized = np.clip(
        colorized * 255.0,
        0,
        255
    ).astype(np.uint8)

    result = Image.fromarray(colorized)

    return result


demo = gr.Interface(
    fn=colorize_image,
    inputs=gr.Image(
        type="pil",
        label="Upload Grayscale Image"
    ),
    outputs=gr.Image(
        type="pil",
        label="Colorized Image"
    ),
    title="🎨 AI Image Colorization",
    description=(
        "Upload a grayscale image and the AI model "
        "will automatically generate a colorized image."
    )
)


if __name__ == "__main__":
    demo.launch()