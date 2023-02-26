# Coding For Medicine
A series of educational exercises, applying programming to medical problems.


## About these exercises
Each exercise is designed to function as a standalone exercise.

If you are a learner, select an exercise below based on your interests and experience level. The quickest way to get started is click on the link below, then on 'Open in Colab'.

If you are an educator, feel free to adopt and adapt these exercises based on your requirements.


## Exercises

| Exercise                           | Difficulty   | Concepts                                               | Accompanying material | Created by |
| ---------------------------------- | ------------ | ------------------------------------------------------ | --------------------- | ---------- |
| [Setting up Jupyter Notebook](./exercises/Setting_up_Jupyter_Notebook.ipynb)  | Introductory     | Jupyter Notebook, Google Colab, importing modules | [Official Tutorial for Google Colab](https://www.youtube.com/watch?v=inN8seMm7UI)  | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| Python Principles | Beginner | Variables, functions, loops, conditionals, data structures |  |  |
| [Coding a medical calculator](./exercises/Coding_Medical_Calculator.ipynbb)  | Beginner     | basic Python (input, try/except, if/else/while, print) | [YouTube tutorial](https://www.youtube.com/watch?v=ve9Mz58p4VA)   | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| [Predicting hospital non-attendance](./exercises/Predicting_No_Shows.ipynb)| Intermediate | cleaning data, feature engineering, simple classification model     | [YouTube tutorial](https://www.youtube.com/watch?v=Y9O2_2NQ0RM), [blog post](https://chrislovejoy.me/no-shows/)  | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| [Diagnosing breast cancer](./exercises/Breast_cancer_features.ipynb)         | Intermediate | model training, performance metrics, confusion matrix  | [YouTube tutorial](https://www.youtube.com/watch?v=c8s5GKRrenY) | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| Predicting stroke | Intermediate | dealing with class imbalance, F1 score, underfitting and overfitting,  | | [Dr Lawrence Adams](https://github.com/lawrenceadams) |  
| Predicting length of stay | Intermediate | logistic regression, odds and odds ratios, dummy variables, confidence intervals | | [Dr Jess Caterson](https://github.com/jjcato9) |
| Cancer gene expression classification | Advanced | exploratory data analysis, feature selection, classification models, prediction metrics | | [Emily Jin](https://github.com/emilyjin11) | 
| Diagnosing chest X-rays | Advanced | CNNs (TODO) |  |  | 
| [Extracting insights from Medical Research Papers](./exercises/Extracting%20Insights%20from%20Medical%20Research%20Papers.ipynb) | Advanced | NLP (tokenisation, summarisation, question-answering), APIs | | [Dr Chris Lovejoy](https://www.github.com/chris-lovejoy) |
| (bioinformatic exercise - TBD) | Advanced | | | |
| (public health exercise - TBD) | Intermediate | | | |


## Contributor Guidelines

If you would like to contribute an exercise to this repository, please either (A) submit an Issue or (B) submit a Pull Request of the modifed README, with your exercise added to the table.

The core principles are that all exercises should be:

1. **Highly descriptive**. All code should be explained, with minimal amounts of assumed knowledge. It should be easy to understand and complete the notebook with no reference to external material.
2. **Interactive**. Users should be prompted to modify and complete code, or experiment on their own. These are not purely 'demo' notebooks. Aspirationally, users should not be able to run front-to-back before any user modification (although not essential).
3. **Easy to run**. It should be easy and intuitive to run the notebooks both on Google Colab or on local Jupyter Notebooks.

[Here is a simple template notebook](./New_Exercise_Template.ipynb) and [here](./exercises/Coding_Medical_Calculator.ipynb) is an example of a well-designed exercise.

If there are significant amounts of code for the user to write, then template 'solution' code can be provided in the 'template_code' folder.
