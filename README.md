# User Defined Decision Tree Classifier

This project is a basic implementation of a Decision Tree Classifier
using Python without directly using Scikit-learn's Decision Tree Classifier.

The project uses the Iris Dataset for classification.

## Project Steps

The program is divided into 7 simple steps:

### Step 01 : Load Dataset
Loads the Iris dataset from the `iris.csv` file and stores the data
using Python dictionaries and lists.

### Step 02 : Get New Point
Takes Sepal Length, Sepal Width, Petal Length and Petal Width
from the user as input.

### Step 03 : Find Best Split
Calculates the average value of each feature and uses the calculated
value as the threshold for splitting the dataset.

### Step 04 : Split Data
Splits the dataset into two groups:

- Left Data
- Right Data

The split is performed using the selected feature and threshold.

### Step 05 : Check Split Result
Checks the number of records present in Left Data and Right Data.

### Step 06 : Find Majority
Counts the different species and finds the majority class from
the selected data.

### Step 07 : Prediction
Uses the new input point, feature and threshold to decide whether
the point belongs to the Left Class or Right Class.

## Dataset

The project uses the Iris Dataset.

Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target:

- Species

Classes:

- Setosa
- Versicolor
- Virginica

## Technologies Used

- Python
- Lists
- Dictionaries
- File Handling
- Basic Machine Learning Logic

## Project Structure

```text
UserDefined-DecisionTree-Classifier/
│
├── UserDefinedDecisionTree_Classifier.py
├── iris.csv
└── README.md

## How to Run

1. Make sure Python is installed.

2. Keep the following files in the same folder:
   - `UserDefinedDecisionTree_Classifier.py`
   - `iris.csv`

3. Open Command Prompt or Terminal in the project folder.

4. Run the program:

```bash
python UserDefinedDecisionTree_Classifier.py

## Author

**Yash Chavan**


