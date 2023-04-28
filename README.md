# Coding For Medicine (Work-In-Progress)
A series of educational exercises, applying programming to medical problems.


## About these exercises
Each exercise is designed to function as a standalone exercise.

If you are a learner, select an exercise below based on your interests and experience level. The quickest way to get started is click on the link below, then on 'Open in Colab'.

If you are an educator, feel free to adopt and adapt these exercises based on your requirements.

If you are interested in contributing, see the [Contributor Guidelines](#contributor-guidelines).

## Exercises

| Exercise                           | Difficulty   | Concepts                                               | Accompanying material | Created by |
| ---------------------------------- | ------------ | ------------------------------------------------------ | --------------------- | ---------- |
| [Setting up Jupyter Notebook](./exercises/Setting_up_Jupyter_Notebook.ipynb)  | Introductory     | Jupyter Notebook, Google Colab, importing modules | [Official Tutorial for Google Colab](https://www.youtube.com/watch?v=inN8seMm7UI)  | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| [Python Principles](./exercises/Python_Principles.ipynb) | Beginner | Variables, functions, loops, conditionals, data structures |  | [Dr Aaron Smith](https://www.github.com/medic-code) |
| [Coding a medical calculator](./exercises/Coding_Medical_Calculator.ipynb)  | Beginner     | basic Python (input, try/except, if/else/while, print) | [YouTube tutorial](https://www.youtube.com/watch?v=ve9Mz58p4VA)   | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| [Predicting hospital non-attendance](./exercises/Predicting_No_Shows.ipynb)| Intermediate | cleaning data, feature engineering, simple classification model     | [YouTube tutorial](https://www.youtube.com/watch?v=Y9O2_2NQ0RM), [blog post](https://chrislovejoy.me/no-shows/)  | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| [Diagnosing breast cancer](./exercises/Breast_cancer_features.ipynb)         | Intermediate | model training, performance metrics, confusion matrix  | [YouTube tutorial](https://www.youtube.com/watch?v=c8s5GKRrenY) | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| [Creating and querying an EHR database](./exercises/Create_And_Query_EHR_Database.ipynb) | Intermediate | SQL queries, pandas, Levehstein distance |  | [Dr Kelvin Kramp](https://github.com/KelvinKramp) | 
| [Predicting stroke](https://github.com/chris-lovejoy/CodingForMedicine/blob/main/exercises/Stroke_Prediction_Model.ipynb) | Intermediate | dealing with class imbalance, F1 score, underfitting and overfitting,  | | [Dr Lawrence Adams](https://github.com/lawrenceadams) |  
| [Predicting length of stay with logistic regression](https://github.com/chris-lovejoy/CodingForMedicine/blob/main/exercises/Logistic%20Regression%20Basics.ipynb) | Intermediate | logistic regression, odds and odds ratios, dummy variables, confidence intervals | | [Dr Jess Caterson](https://github.com/jjcato9) |
| Cancer gene expression classification | Advanced | exploratory data analysis, feature selection, classification models, prediction metrics | | [Dr Emily Jin](https://github.com/emilyjin11) | 
| [Diagnosing chest X-rays](https://github.com/chris-lovejoy/CodingForMedicine/blob/main/exercises/Diagnosing_Chest_X-Rays.ipynb) | Advanced | image analysis, convolutional neural networks, transfer learning |  |  [Oleksandr Teslenko](https://github.com/AlexTeslenko) | 
| [Extracting insights from Medical Research Papers](./exercises/Extracting%20Insights%20from%20Medical%20Research%20Papers.ipynb) | Advanced | NLP (tokenisation, summarisation, question-answering), APIs | | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| (public health exercise - TBD) | Intermediate | | | |


## Contributor Guidelines

If you would like to contribute an exercise to this repository, please either (A) submit an Issue or (B) submit a Pull Request of the modifed README, with your exercise added to the table.

The core principles are that all exercises should be:

### 1. **Highly descriptive** (but not overly verbose). 

a. All code should be explained, with minimal amounts of assumed knowledge. 

b. It should be easy to understand and complete the notebook with no reference to external material.

c. There should be a good integration between code and explanatory text. Sections of text shouldn't go beyond ~3-4 paragraphs without some code being run. 

### 2. **Interactive** (ie. not "demo" notebooks)

a. Users should be prompted throughout to both (1) modify and complete code and (2) answer questions related to the exercise.

b. Code completions can be filling in gaps ([example](https://github.com/chris-lovejoy/CodingForMedicine/blob/main/exercises/Coding_Medical_Calculator.ipynb)) or writing new functionality from scratch ([example](https://github.com/chris-lovejoy/CodingForMedicine/blob/main/exercises/Predicting_No_Shows.ipynb)).

c. Each sub-section of the exercise should have interactive elements, such as code to complete, 2-3 questions to answer or both.

d. Questions should be a mixture of "open" and "closed" questions. "Explore the dataset further and describe your findings" is an example of an open question, while "How many entries are there in the dataset?" and "Which variable has the most missing values?" are examples of closed questions.  

e. Detailed descriptions of several potential follow-on exercises should be provided at the end of each notebook. These exercises should be more open-ended and with a broader scope than exercises throughout the notebook.

### 3. **Easy to run**.

a. It should be easy and intuitive to run the notebooks both on Google Colab or on local Jupyter Notebooks.

b. Explanations and task descriptions should be unambiguous, such that the challenge lies in *doing* the exercise, not in interpreting it.


[Here is a simple template notebook](./New_Exercise_Template.ipynb) and [here](./exercises/Coding_Medical_Calculator.ipynb) is an example of a well-designed exercise.

If there are significant amounts of code for the user to write, then template 'solution' code can be provided in the 'template_code' folder.
