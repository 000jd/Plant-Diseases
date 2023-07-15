import streamlit as st
import requests
from io import BytesIO
from PIL import Image
from predict import predict_diseases
from utils.classes import disease_dict
from streamlit_lottie import st_lottie


def main():
    st.set_page_config(
        page_title="PlantDiseases",
        page_icon="🌿",
    )

    uploaded_file = None

    col1, col2 = st.columns([1, 4])

    # Lottie Animation
    with col1:
        animation_url = "https://lottie.host/14ccf5bb-59d6-4b1f-91e0-d7956860b2a8/SeJ6BssdME.json"
        animation = st_lottie(animation_url, height=170,
                              width=170, key="lottie")
    # Title
    with col2:
        st.title('Plant Disease Classification')

    col3, col4 = st.columns(2)

    # Image Source Selector
    with col3:
        image_source = st.radio('Select Image Source:', ('Upload', 'URL'))

    # Image Uploader
    with col4:
        if image_source == 'Upload':
            uploaded_file = st.file_uploader(
                'Choose an image file', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        st.image(image, caption='Uploaded Image',
                 use_column_width=True, width=300)

        # Predict button
        if st.button('Predict'):
            with st.spinner('Predicting...'):

                try:
                    predict_disease_name = predict_diseases(image)
                    disease_name = disease_dict.get(predict_disease_name)
                    st.success(f'Predicted Disease: {disease_name}')
                    
                except Exception as e:
                    st.warning('Sorry, something went wrong...', icon="🤖")
            st.empty()  # Remove the Lottie animation from the UI once prediction is complete

    elif image_source == 'URL':
        image_url = st.text_input('Enter Image URL:')

        if st.button('Predict'):
            try:
                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))

                st.image(image, caption='Image from URL',
                         use_column_width=True, width=300)

                with st.spinner('Predicting...'):
                    try:
                        predict_disease_name = predict_diseases(image)
                        disease_name = disease_dict.get(predict_disease_name)
                        st.success(f'Predicted Disease: {disease_name}')

                    except Exception as e:
                        st.warning('Sorry, something went wrong...', icon="🤖")
                st.empty()  # Remove the Lottie animation from the UI once prediction is complete

            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == '__main__':
    main()