---
marp: true
theme: default
size: 16:9
paginate: true
header: "Module 2 – Machine Learning"
footer: "Instructor Model Answers"
---

# Interactive Decision Boundary  
## Instructor Model Answers

Model / expected observations for:

- Step 1 – Simple linear model
- Step 2 – Underfitting
- Step 3 – Non‑linear models
- Step 4 – Overfitting (bonus)

---

class: lead

# Step 1  
## Simple Linear Model – Answers

---

# Step 1 – Expected Observations

Dataset:

- Two clearly separated clusters / blobs.

Model:

- Logistic Regression **or** Linear SVM.

Expected:

- Decision boundary is a **single straight line** (in 2D).
- Loss/error:
  - Starts higher, then decreases as model trains (depending on tool).
  - Final error is **low**; almost all points are correctly classified.

Key conceptual answer:

- Linear models can only create **linear (straight) boundaries** in feature space.
- When data is linearly separable, this is enough.

---

# Step 1 – Key Questions (Model Answers)

1. **Boundary shape?**  
   - Straight line (or flat hyperplane in higher dimensions).

2. **Why must it be straight?**  
   - The decision function is linear in the input features (e.g., sign of $$w^\top x + b$$).  
   - Level sets of a linear function are straight lines/planes.

3. **Generalization?**  
   - For similar future data (same pattern of two blobs), a linear boundary should generalize **well**.

---

class: lead

# Step 2  
## Underfitting – Answers

---

# Step 2 – Expected Observations

Dataset:

- **Concentric circles** or similarly non‑linearly separable pattern.

Model:

- Same **linear** model (Logistic Regression or Linear SVM).

Expected:

- Decision boundary remains a **straight line**.
- It cannot bend to separate inner vs outer ring.
- Many points from both classes will be on the **wrong side**.
- Error stays **significantly higher** than in Step 1.

Key conceptual answer:

- The model is **too simple** to capture the true pattern → **underfitting**.

---

# Step 2 – Key Questions (Model Answers)

1. **Can the linear boundary wrap around the inner circle?**  
   - No. A straight line cannot enclose a circle.

2. **Is error higher?**  
   - Yes. The model misclassifies a substantial number of points.

3. **Why is this underfitting?**  
   - The model’s functional form (linear) is fundamentally unable to represent the circular structure, no matter how we tune its parameters.

Good student sentence:

> “Underfitting is when a model is too simple to capture the important patterns in the data, leading to high error even on the training set.”

---

class: lead

# Step 3  
## Switching to Non‑Linear Models – Answers

---

# Step 3 – Expected Observations

Dataset:

- Same **concentric circles** or complex pattern.

Models:

- **KNN** (e.g., K=1 or 3), or
- **Decision Tree** (depth ≈ 6–8).

Expected:

- Decision boundary becomes **curved** (for KNN) or **stepped** (for trees).
- Boundary now wraps around the circle (or follows complex shapes).
- Classification error drops **much lower** than for the linear model.
- Visual improvement: clear separation of inner vs outer ring.

Key conceptual answer:

- Non‑linear models can approximate **non‑linear decision boundaries**, fitting complex patterns that linear models cannot.

---

# Step 3 – Key Questions (Model Answers)

1. **How did the boundary change?**  
   - From a single straight line to:
     - A curved boundary (KNN) following the data distribution, or
     - Piecewise-constant regions (Decision Tree) that conform to the rings.

2. **Did error go down?**  
   - Yes. Significantly lower error than the linear model on the same dataset.

3. **Relation to linear vs non‑linear boundaries?**  
   - Linear models: only straight lines / planes.
   - Non‑linear models: can form **bent** or **stepped** boundaries that match more complex patterns.

Good student explanation:

> “By switching to a non‑linear model like KNN or a decision tree, we gave the model enough flexibility to draw a decision boundary that wraps around the circular class, which a straight line can’t do.”

---

class: lead

# Step 4  
## Overfitting – Answers

---

# Step 4 – Expected Observations

Dataset:

- With added **noise**, overlapping shapes, or irregular clusters.

Model:

- Very flexible:
  - Decision Tree with **max depth** (or no pruning), or
  - KNN with **K = 1**.

Expected:

- Decision boundary becomes very **jagged**.
- Small “islands” or narrow spikes appear in the boundary to capture individual outliers.
- Training error can be **very low** (almost perfect).
- But the boundary looks **unnatural** and overly tailored to the training data.

Key conceptual answer:

- This is **overfitting**: the model fits noise and outliers instead of the underlying pattern.

---

# Step 4 – Key Questions (Model Answers)

1. **Do you see weird “islands”?**  
   - Yes. The boundary may:
     - Surround one or two isolated points.
     - Create long thin regions.
   - These visually indicate the model is “trying too hard” to fit every sample.

2. **Is the model catching every training point?**  
   - Often yes, or nearly so – including outliers.

3. **Generalization to new data?**  
   - Likely **poor**:
     - New points that are close to the true pattern but not exactly at training locations may be misclassified.
     - The model is tuned to training noise, not the general trend.

Good student explanation:

> “The tree with max depth / KNN with K=1 overfits: it draws a very complicated boundary that fits the training points almost perfectly but will probably misclassify many new points, because it learned the noise rather than the underlying structure.”

---

class: lead

# Overall Instructor Summary

---

# Overall Summary – Instructional Points

If students complete the activity successfully, they should be able to:

- Describe how a **linear model** draws a straight boundary and works well on linearly separable data.
- Explain **underfitting** as a mismatch between model simplicity and data complexity.
- Explain how **non‑linear models** (KNN, Decision Trees) can draw more flexible boundaries and reduce error on complex datasets.
- Recognize **overfitting** as hyper‑complex boundaries that match noise and outliers, leading to poor generalization.

You can close by reinforcing:

> Model complexity must be chosen carefully:  
> too simple → underfitting,  
> too complex → overfitting,  
> “just right” → good generalization.

---