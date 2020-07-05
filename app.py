from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('deployment_2_07052020')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    #from PIL import Image
    #image = Image.open('logo.png')
    #image_hospital = Image.open('hospital.jpg')

    #st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict car mileage')
    #st.sidebar.success('https://www.pycaret.org')
    
    #st.sidebar.image(image_hospital)

    st.title("Car Mileage Prediction App")

    if add_selectbox == 'Online':

        cylinders = st.number_input('Cylinders', min_value=1, max_value=100, value=8)
        displacement = st.number_input('Displacement', min_value = 0, max_value = 500, value =  100)
        horsepower = st.number_input('Horsepower',min_value = 0, max_value = 1000, value =  200)
        weight = st.number_input('Weight',min_value = 0,max_value = 6000, value = 3000)
        acceleration = st.number_input('Acceleration', min_value = 0,max_value = 100, value = 10)
        origin = st.selectbox('Origin (1:USA, 2:Europe, 3:Japan)',[1,2,3])


        output=""

        input_dict = {'cylinders' : cylinders, 'displacement' : displacement, 'horsepower':horsepower, 'weight' : weight, 'acceleration' :           acceleration, 'origin' : origin}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = output

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()