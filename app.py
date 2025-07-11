import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image

labels = ['Downy Mildew Diease', 'Fresh Leaf', 'Leaf Curl Diease', 'Mosaic Diease','Red beetle Diease']

@st.cache_resource
def load_deep_learning_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except OSError as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_image(img):
    img = img.resize((224, 224))
    img = img.convert('RGB')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def predict_class(model, img):
    img_array = preprocess_image(img)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    predicted_label = labels[predicted_class]
    return predicted_label

def main():
    # Reduce title size using markdown (you can modify the size as you like)
    st.markdown("<h1 style='font-size: 24px;'>Sweet pumpkin leaf disease detection using deep learning approaches</h1>", unsafe_allow_html=True)

    model_path = '/content/drive/MyDrive/personal work/asif/complete/sweet pumkin/Web/best_model.h5'
    model = load_deep_learning_model(model_path)

    if model is None:
        st.error("Failed to load the model. Please check the model path or re-upload the model.")
        return

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        
        img = img.resize((500, 500))  
        st.image(img, caption="Resized Image", width=500)

        predicted_label = predict_class(model, img)
        
        st.write(f"Predicted Class: **{predicted_label}**")

if __name__ == "__main__":
    main()
