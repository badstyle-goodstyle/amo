#!/bin/bash

# Run data_creation.py to generate character data
python3 data_creation.py

# Run model_preprocessing.py to preprocess the training data
python3 model_preprocessing.py

# Run model_preparation.py to create and train the model
python3 model_preparation.py

# Run model_testing.py to test the model on the test data
python3 model_testing.py

# Clean up the "train" and "test" folders
rm -rf train
rm -rf test
