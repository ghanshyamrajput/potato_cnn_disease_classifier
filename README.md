# Potato Leaf Disease Detection Using CNN

## About the Project

This is a Deep Learning project developed to detect diseases in potato leaves using a Convolutional Neural Network (CNN).

The model takes a potato leaf image as input and predicts whether the leaf is affected by Early Blight, Late Blight, or is Healthy.

I have also created a simple web application using Streamlit where users can upload an image and check the prediction along with confidence scores.

## Classes

The model identifies three classes:

- Early Blight
- Late Blight
- Healthy

## Tools and Technologies

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Pillow (PIL)
- Streamlit

## Model Details

I built a CNN model using the following layers:

- Conv2D
- Batch Normalization
- ReLU Activation
- MaxPooling2D
- Global Average Pooling
- Dense Layer
- Dropout
- Softmax

The model takes images of size 128 × 128 with 3 RGB channels.

## Data Preprocessing

Before training, I performed the following steps:

- Loaded images from the dataset.
- Resized images to 128 × 128.
- Converted images into RGB format.
- Split the dataset into 80% training and 20% validation.
- Applied image normalization.

## Data Augmentation

To make the model learn from different image variations, I used:

- Random Flip
- Random Rotation
- Random Zoom
- Random Contrast

## Model Training

The model was trained using:

- Optimizer: Adam
- Learning Rate: 0.00001
- Loss Function: Sparse Categorical Crossentropy
- Batch Size: 32
- Epochs: 40

I also used Early Stopping and ReduceLROnPlateau to improve the training process.

## Model Evaluation

After training, I checked the model performance using:

- Training Accuracy
- Validation Accuracy
- Training Loss
- Validation Loss
- Confusion Matrix

## Streamlit Application

I created a Streamlit application for disease prediction.

**Application features:**

- Upload a potato leaf image.
- View the uploaded image.
- Click on the Predict Disease button.
- Get the predicted disease name.
- View confidence scores for Early Blight, Late Blight, and Healthy.

## Project Structure

```text
Potato-Leaf-Disease/
│
├── data/
│   ├── Potato___Early_blight/
│   ├── Potato___Late_blight/
│   └── Potato___healthy/
│
├── app.py
├── potato_cnn_model.keras
├── classification_report.txt
└── README.md
```

## How to Run the Project

**1. Clone the repository**

```bash
https://github.com/ghanshyamrajput/potato_cnn_disease_classifier
```

**2. Install the required libraries**

```bash
pip install tensorflow numpy matplotlib pillow streamlit
```

**3. Run the Streamlit application**

```bash
streamlit run app.py
```

## Future Scope

- Improve prediction accuracy.
- Add more plant disease categories.
- Include disease prevention information.
- Deploy the application online.

## Author

**Ghanshyam Rajput**

Project: Potato Leaf Disease Detection

Technologies: Python, Deep Learning, CNN, TensorFlow, Streamlit
