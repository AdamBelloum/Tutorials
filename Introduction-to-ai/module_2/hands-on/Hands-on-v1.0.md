---
marp: true
theme: default
size: 16:9
paginate: true
header: "Module 2 – Machine Learning"
footer: "Activity: Interactive Decision Boundary"
---

# Module 2 – Machine Learning  
## Hands‑on: Interactive Decision Boundary

In this activity, you will:

- Watch a **model learn a decision boundary**
- Compare **linear vs non‑linear** models
- See how **model complexity** affects performance
- Get an intuition for **underfitting** and **overfitting**

---

class: lead

# Tools

---

# Activity Tool

We will use one (or both) of these interactive tools:

- **Interactive‑ML**  
  https://www.interactive-ml.com/

- **ML Visualiser – Decision Boundary**  
  https://ml-visualiser.vercel.app/decision-boundary

You can:

- Choose different **datasets**
- Select a **machine learning algorithm**
- Adjust **hyperparameters** (tree depth, K in KNN, etc.)
- Watch the **decision boundary** and **error** change

---

class: lead

# Step 1  
## Simple Linear Model

---

# Step 1 – Goal

See how a **linear model** behaves on a simple problem:

- Two clearly separated clusters
- Linear model (Logistic Regression or Linear SVM)
- Mostly good performance and a **straight boundary**

---

# Step 1 – Instructions

1. Choose a **simple 2‑class dataset**:
   - Two separated clusters / blobs.
2. Select a **linear model**:
   - Logistic Regression **or** Linear SVM.
3. Click **Train** (or use the tool’s play button).

Observe:

- How does the **decision boundary** look?
- How does the **error / accuracy** behave?

---

# Step 1 – Questions

Discuss in pairs:

1. Is the decision boundary **straight or curved**?
2. Why must a linear model draw it this way?
3. Do you think this model will generalize well to **similar new points**?

Be ready to share your answers with the class.

---

class: lead

# Step 2  
## Underfitting with Linear Models

---

# Step 2 – Goal

See what happens when a **linear model** is used on a **non‑linear** pattern:

- Dataset is more complex (e.g., circles)
- Same linear model (Logistic Regression / Linear SVM)
- Model **underfits** the data

---

# Step 2 – Instructions

1. Choose a **more complex dataset**, e.g.:
   - Concentric circles (one class inside another),  
     or another non‑linearly separable pattern.
2. Keep the **same linear model**:
   - Logistic Regression **or** Linear SVM.
3. Click **Train**.

Observe:

- Shape of the **decision boundary**
- **Error / misclassifications** on the plot

---

# Step 2 – Questions

In small groups:

1. Can the linear boundary **wrap around** the inner circle?
2. Does the classification error stay **higher** than in Step 1?
3. Why is this an example of **underfitting**?

Write down one sentence that explains underfitting in your own words.

---

class: lead

# Step 3  
## Switch to Non‑Linear Models

---

# Step 3 – Goal

See how **non‑linear models** can fit complex patterns:

- Same complex dataset (e.g., circles)
- Change algorithm to **KNN** or **Decision Tree**
- Increase model **flexibility**

---

# Step 3 – Instructions

1. Keep the **complex dataset** from Step 2.
2. Change the model type to **K‑Nearest Neighbors (KNN)** or **Decision Tree**.
3. Increase model complexity, for example:
   - Decision Tree: set **max depth** relatively high (e.g., 6–8).
   - KNN: set **K** to a small value (e.g., **K = 1 or 3**).
4. Click **Train**.

Observe:

- The new shape of the **decision boundary**
- How the **error** changes

---

# Step 3 – Questions

Discuss:

1. How did the decision boundary change after switching to KNN or Trees?
2. Did the error go **down** compared to the linear model?
3. How does this illustrate the difference between **linear** and **non‑linear** decision boundaries?

Be prepared to explain one concrete difference you observed.

---

class: lead

# Step 4  
## Overfitting (Bonus Challenge)

---

# Step 4 – Goal

Observe **overfitting**:

- Model becomes **too complex**
- Boundary becomes very **jagged / weird**
- Likely to perform poorly on unseen data

---

# Step 4 – Instructions

1. Choose a dataset with:
   - More **noise**, overlapping classes, or irregular shapes.
2. Use a **highly flexible** configuration, e.g.:
   - Decision Tree with **maximum depth**.
   - KNN with **K = 1**.
3. Click **Train**.

Look closely at the **decision boundary**.

---

# Step 4 – Questions

In groups:

1. Do you see **tiny islands** or very jagged shapes in the boundary?
2. Is the model trying to catch **every single training point**, even outliers?
3. If we brought in new unseen data, do you expect this model to perform:
   - **Well**, or  
   - **Poorly**? Why?

Relate your answer to the idea of **overfitting**.

---

class: lead

# Wrap‑Up Discussion

---

# Wrap‑Up – Key Concepts

As a class, we will summarize:

- When **linear models** are appropriate
- How **non‑linear models** can fit complex patterns
- What **underfitting** looks like on the plot
- What **overfitting** looks like (hyper‑complex boundaries)

Think of **one sentence** that connects:
> Model complexity → underfitting / good fit / overfitting

We’ll share a few examples.

---