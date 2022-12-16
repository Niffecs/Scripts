# Import the necessary libraries
from sklearn import *
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np

def is_photo_or_drawing(image):
  # Load the image and convert it to grayscale
  img = Image.open(image).convert('L')
  
  # Resize the image to a standard size
  img = img.resize((200, 200))

  # Flatten the image into a 1D array
  img_array = np.array(img).flatten()

  # Standardize the values in the array
  scaler = StandardScaler()
  img_array = scaler.fit_transform(img_array.reshape(-1, 1))

  # Create a logistic regression model and train it on a dataset of photos and drawings
  model = make_pipeline(LogisticRegression())
  model.fit(X, y)

  # Use the trained model to make a prediction on the input image
  y_pred = model.predict([img_array])

  # Return the predicted class (1 for photo, 0 for drawing)
  return y_pred[0]
