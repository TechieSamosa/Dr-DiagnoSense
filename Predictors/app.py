import time
import pandas as pd
import streamlit as st
import joblib
import os
from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64
import pickle

# Constants for Categories
ETHNICITY_OPTIONS = {'Hisp/Latino': 0, 'Not Hisp/Latino': 1, 'Unknown': 2}
IMPTED_CATEGORIES = ['True', 'False']
PTRACCAT_CATEGORIES = ['Asian', 'Black', 'White']
PTGENDER_CATEGORIES = ['Female', 'Male']
APOE_CATEGORIES = ['2,2', '2,3', '2,4', '3,3', '3,4', '4,4']
MODEL_FILE_PATH_ALZHEIMER = 'C:\\Users\\Chimni\\Projects and Coding\\Version Control Systems\\Dr-DiagnoSense\\Notebooks\\Models\\alzheimer_model.pkl'
MODEL_FILE_PATH_BRAIN_TUMOR = 'C:\\Users\\Chimni\\Projects and Coding\\Version Control Systems\\Dr-DiagnoSense\\Notebooks\\Models\\Brain_Tumor.h5'
CLASS_LABELS_BRAIN_TUMOR = ['Glioma', 'Meningioma', 'No tumor', 'Pituitary']

class Conditions:
    AD = "AD"
    LMCI = "LMCI"
    CN = "CN"

abbreviation = {
    Conditions.AD: "Alzheimer's Disease",
    Conditions.LMCI: "Late Mild Cognitive Impairment",
    Conditions.CN: "Cognitively Normal"
}

condition_description = {
    Conditions.AD: "Description for Alzheimer's Disease",
    Conditions.LMCI: "Description for Late Mild Cognitive Impairment",
    Conditions.CN: "Description for Cognitively Normal"
}

def convert_to_one_hot(selected_category, all_categories):
    return [True if category == selected_category else False for category in all_categories]

def predict_condition(input_data, model_path):
    try:
        loaded_model = joblib.load(model_path)
        predictions = loaded_model.predict(input_data)
        return predictions
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return

def load_brain_tumor_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def preprocess_image(img):
    img = img.resize((150, 150))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = img / 255.0  # Normalize pixel values to be between 0 and 1
    img = np.expand_dims(img, axis=0)
    return img

def image_to_base64(img):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_alzheimer', methods=['POST'])
def predict_alzheimer():
    age = request.form['age']
    gender = request.form['gender']
    education = request.form['education']
    ethnicity = request.form['ethnicity']
    race_cat = request.form['race_cat']
    apoe_allele_type = request.form['apoe_allele_type']
    apoe_genotype = request.form['apoe_genotype']
    imputed_genotype = request.form['imputed_genotype']
    mmse = request.form['mmse']

    user_input = [int(age), int(education), int(mmse)]
    user_input += convert_to_one_hot("PTRACCAT_" + race_cat, PTRACCAT_CATEGORIES)
    user_input += convert_to_one_hot("APOE Genotype_" + apoe_genotype, APOE_CATEGORIES)
    user_input += convert_to_one_hot("PTETHCAT_" + ethnicity, list(ETHNICITY_OPTIONS.values()))
    user_input += convert_to_one_hot("APOE4_" + apoe_allele_type, APOE_CATEGORIES)
    user_input += convert_to_one_hot("PTGENDER_" + gender, PTGENDER_CATEGORIES)
    user_input += convert_to_one_hot("imputed_genotype_" + imputed_genotype, IMPTED_CATEGORIES)

    data = pd.DataFrame([user_input])
    predicted_condition = predict_condition(data, MODEL_FILE_PATH_ALZHEIMER)

    return render_template('result.html', predicted_condition=predicted_condition[0], abbreviation=abbreviation[predicted_condition[0]], condition_description=condition_description[predicted_condition[0]])

@app.route('/predict_brain_tumor', methods=['POST'])
def predict_brain_tumor():
    try:
        image = request.files['image']
        model = load_brain_tumor_model(MODEL_FILE_PATH_BRAIN_TUMOR)
        img = Image.open(image.stream)
        img = preprocess_image(img)
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions)
        predicted_label = CLASS_LABELS_BRAIN_TUMOR[predicted_class]
        img_base64 = image_to_base64(Image.open(image.stream))
        return render_template('result_tumor.html', description=predicted_label, image_data=img_base64)
    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
