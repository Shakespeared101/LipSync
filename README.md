# LipSync

## Project Overview
LipSync is an advanced system designed for automatic transcript generation using deep learning techniques. The system processes videos of individuals speaking directly to the camera, aligns their mouth movements with corresponding textual annotations, and trains a deep neural network for accurate recognition.

## Features
- **Video Preprocessing**: Utilizes TensorFlow and OpenCV for efficient data loading and preprocessing, aligning mouth movements with text annotations.
- **Deep Learning Architecture**: Employs a Conv3D-based model followed by Bidirectional LSTM layers for robust sequence modeling.
- **Training and Optimization**: Trained with a custom CTC loss function and optimized using the Adam optimizer. Includes learning rate scheduling and checkpointing to enhance training performance.
- **Real-Time Predictions**: Capable of recognizing sign language gestures accurately on test videos.

## Streamlit Integration
The project features a Streamlit frontend that provides an interactive interface for users to visualize model predictions in real-time.

## Future Development
Future enhancements will include the capability to process YouTube links, allowing for transcript generation directly from video mouth movements, which aims to improve transcript accuracy by bypassing audio processing.

## Contributors
- Saranya Sarathy
- Shakthi B

## Access to Resources
For access to training datasets and model checkpoints, please contact the project owners.
