import pandas as pd
import pickle
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the preprocessed data
preprocessed_data = pd.read_pickle('preprocessed_data.pkl')

# Extract the training data and labels
X_train = preprocessed_data['X_train']
y_train = preprocessed_data['y_train']

# Create a Support Vector Classifier (SVC) model
model = SVC(kernel='rbf', C=1.0, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Save the trained model to a file
filename = 'trained_model.pkl'
pickle.dump(model, open(filename, 'wb'))

print(f"Trained model saved to {filename}")

# Evaluate the model on the training data
y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
print(f"Train Accuracy: {train_accuracy}")
