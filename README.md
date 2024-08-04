# LipSync: End-to-End Automatic Sign Language Recognition System

## Project Overview

LipSync presents an end-to-end system for automatic sign language recognition using deep learning techniques. The system preprocesses sign language videos, aligns them with corresponding textual annotations, and trains a deep neural network for recognition.

## Key Features

### Data Pipeline
- **Libraries Used:** Integrates TensorFlow and OpenCV for efficient data loading and preprocessing.
- **Architecture:** Utilizes a Conv3D-based architecture followed by Bidirectional LSTM layers for sequence modeling.
- **Optimization:** Trained with a custom CTC loss function and optimized using the Adam optimizer.
- **Augmentation:** Training is enhanced with learning rate scheduling and checkpointing.

### Model Performance
- **Evaluation:** The system is evaluated on a dataset containing diverse sign language gestures and achieves promising results.
- **Real-Time Predictions:** Demonstrates effectiveness in accurately recognizing sign language gestures in real-time test videos.

### Frontend Integration
- **Streamlit:** Uses Streamlit as a frontend to provide an interactive user interface for model interaction and visualization.
- **Future Development:** Potential to include YouTube links to generate transcripts directly from the mouths of speakers for more accurate transcripts, bypassing audio.

## System Components

### Deep Learning Model
- **Conv3D-based Architecture:** For capturing spatial and temporal features in video data.
- **Bidirectional LSTM:** For sequence modeling of the temporal data.
- **Custom CTC Loss Function:** For handling the alignment between video frames and text annotations.
- **Adam Optimizer:** For efficient optimization of the model parameters.

### Data Pipeline
- **Preprocessing:** Efficient data loading and preprocessing using TensorFlow and OpenCV.
- **Training Augmentation:** Includes learning rate scheduling and checkpointing to enhance model performance.

### Evaluation
- **Dataset:** Diverse dataset containing various sign language gestures.
- **Performance Metrics:** Promising results in recognizing sign language gestures accurately in real-time.

## Contributors
- **Saranya Sarathy**
- **Shakthi B**

## Contact Information
Please contact the owners to get access to the training datasets and model checkpoints used in this project.

---

This project showcases the feasibility and efficacy of deep learning in real-world applications, particularly in assisting individuals with hearing impairments through sign language recognition technology. The integration of Streamlit for frontend interaction and potential future enhancements to include direct YouTube link transcription further demonstrate the system's versatility and practical applicability.
```
