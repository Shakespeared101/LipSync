# Import all of the dependencies
import streamlit as st
import os 
import imageio 
import base64
import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model

# Set the layout to the Streamlit app as wide 
st.set_page_config(layout='wide')

# Setup the sidebar
with st.sidebar: 
    st.image('https://imageio.forbes.com/specials-images/imageserve/64d24936a0c9451a52034c63/Training-machine-learning-model-concept/960x0.jpg?format=jpg&width=960')
    st.title('Menu')
    selected_page = st.radio("Go to:", ["Your Profile", "Your Subscriptions", "Your Transcripts", "About Us"])

    if selected_page == "Your Profile":
        st.header("Your Profile")
        # Check if a profile picture is uploaded
        if "profile_pic" not in st.session_state:
        # User profile picture uploader
            profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])
            if profile_pic is not None:
            # Store uploaded profile picture in session state
                st.session_state.profile_pic = profile_pic

    # Display profile picture if uploaded
        if "profile_pic" in st.session_state:
            # Display circular profile picture
            encoded_pic = base64.b64encode(st.session_state.profile_pic.read()).decode()
            html = f'<img src="data:image/png;base64,{encoded_pic}" style="width:150px;height:150px;border-radius:50%;">'
            st.markdown(html, unsafe_allow_html=True)

    # User information
        st.write("Name: John Doe")
        st.write("Number of Transcripts Done: 10")

    elif selected_page == "Your Subscriptions":
        st.header("Your Subscriptions")
        st.write("You are currently enrolled in the monthly plan.")

    elif selected_page == "Your Transcripts":
        st.header("Your Transcripts")
        st.subheader("Video Title 1")
        st.write("Transcript: Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        st.subheader("Video Title 2")
        st.write("Transcript: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.")

    elif selected_page == "About Us":
        st.header("About Us")
        st.write("This website uses deep learning for lip reading to generate subtitles.")
        st.write("It allows translation into major languages.")
        st.write("For inquiries, please contact us at example@email.com or +1234567890.")

st.title('LipSync') 
st.header('Generate Subtitles with AI based Lip Reading')

# Add a file uploader section
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Display the file details
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)

# Generating a list of options or videos 
options = os.listdir(os.path.join('..', 'data', 's1'))
selected_video = st.selectbox('Training video set', options)

# Generate two columns 
col1, col2 = st.columns(2)

if options: 

    # Rendering the video 
    with col1: 
        st.info('Step 2: View Selected Video')
        st.write('Select a video from the dropdown menu below.')
        file_path = os.path.join('..','data','s1', selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

        # Rendering inside of the app
        video = open('test_video.mp4', 'rb') 
        video_bytes = video.read() 
        st.video(video_bytes)

    with col2: 
        video, annotations = load_data(tf.convert_to_tensor(file_path))
        # imageio.mimsave('animation.gif', video, fps=10)
        # st.image('animation.gif', width=400) 

        st.info('Predicted Transcript (English)')
        model = load_model()
        yhat = model.predict(tf.expand_dims(video, axis=0))
        decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
        predicted_text = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.text(predicted_text)


selected_language = st.selectbox('Step 4: Select Language', ['English', 'French', 'German', 'Spanish'], help="Select a language to translate the predicted transcript.")

# Translation function
def translate_text(text, target_language):
    # Add translation logic here
    translated_text = f"Translated to {target_language}: {text}"  # Dummy translation for demonstration
    return translated_text

if selected_language != 'English':
    translated_text = translate_text(predicted_text, selected_language)
    st.text(translated_text)
