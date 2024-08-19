# Poker Hand Classification

## Project Overview
The Poker Hand Classification project aims to classify poker hands into 10 predefined classes based on the rank and suit of cards. The project leverages machine learning classification algorithms to accurately identify the type of poker hand from a given set of cards. This project includes data preprocessing steps such as Feature Transformation and Feature Construction to ensure the data is machine-friendly and to handle data imbalance, significantly improving model accuracy.

## Features
- **Card Rank**: The rank of each card (e.g., 2, 3, 4, ... , King, Ace).
- **Card Suit**: The suit of each card (e.g., Hearts, Diamonds, Clubs, Spades).
- ## Project Structure
- `Data/`: Contains the dataset used for training and testing the models. This directory also includes:
  - `Data/Unique_combination/Code/26lakhs_possible_data.py`: Script that generates all possible unique combinations of poker hands.
  - `Data/Unique_combination/Dataset/unique_poker.zip`: The dataset containing the unique poker hand combinations.
- `Model/`: Contains `POKER_HAND_main.ipynb`, a Jupyter notebook for data preprocessing, feature engineering, and model development.
- `Presentation/`: Contains presentation slides.
- `Report/`: Contains the project report.
- `README.md`: Project overview and documentation (this file).

## Usage


### Data Preprocessing
- **Feature Transformation**: Applied transformations to convert raw card rank and suit into a format suitable for machine learning algorithms.
- **Feature Construction**: Created new features to enhance model learning.


### Model Training
- Train the  model using various machine learning algorithms such as Decision Trees, Random Forest, ADaBoost,KNN etc. Experiment with different algorithms to compare their performance on the dataset.

### Model Evaluation
- Evaluated the models' performance using metrics such as Confusion Matrix, precision, recall, and F1-score. 

### Prediction
- Use the trained model to classify for new poker data.

## Contact

If you have any questions or feedback, please feel free to contact me at rakeshnemu237@gmail.com.
