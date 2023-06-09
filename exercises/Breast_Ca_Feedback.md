Gene Expression Task
Reviewer: Jess Caterson

General Feedback
- Overall a very comprehensive exercise
- There is a lot of content, but it flows well and the complexity increases gradually
- Sometimes little explanation - possible that students might not be able to follow the steps being performed
- General appearance improved

Focussed Edits

1. Layout
- Capitalised Title
- Kept section headings consistent in language
- Broke up markdown and python script so process is more step-by-step for students
- Added questions & hidden answers to questions already in script
- Markdown styling: `xxx` for code chunks, coloured 'hints' etc.

2. Introduction Section
- Added more of an explanation to sections (assuming students have less knowledge)
- Added exercise requirements section

3. Part 1: Set up/Data Pre-Processing/EDA
- Amended title to add pre-processing
- I would advise referencing the data source and explaining a little what the data is about - Data Scientists should be able to understand what they are analysing in my opinion!
- Added Q&A
- Slight re-wording of instructions/explanations

4. Part 2: LASSO Regression
- Added to description for LASSO to give a better explanation (assuming some students have little or no prior knowledge of this method)
- Explained what a dummy variable is
- Using dictionary & mapping to convert receptor status columns to binary variables (less code than converting to dummies then eliminating negative columns)
- Explained train/test split and k-fold cross-validation
- Explained ELI5 a little (this isn't commonly used so I wouldn't expect students to know about it)
- Add Q&A about '< BIAS >' output from ELI5
- Added 'Optional' to final step

**TBA** - Equations for MSE and R-squared

5. Part 3: Random Forest
- RF is an ensemble method not a CART method, but it uses CARTs to build the forest
**TBA** - Explain gini impurity briefly
- Re-worded the RF description
- Explained what a hyper-parameter is and what the hyperparameters in RF mean (w/ Q&A)
- Change Confusion Matrix to plotted version

6. Part 4: XGBoost
- Re-worded description slightly
- Added random_state to base model 
- Performance didn't improve much for me - not sure if you had a similar issue?
- Formatted feature importance figure so that genes are not overlapping so much



