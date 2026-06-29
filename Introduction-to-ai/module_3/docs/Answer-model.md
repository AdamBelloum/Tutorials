---
marp: true
theme: default
size: 16:9
paginate: true
header: "Deep Learning – Hands‑on"
footer: "Instructor Model Answers"
---

# Deep Learning – Hands‑on  
## Instructor Model Answers

Model / expected answers for:

- Activity 1 – Feature hierarchy
- Activity 2 – Forward pass
- Activity 3 – Overfitting vs generalization
- Activity 4 – Vanishing & exploding gradients

---

class: lead

# Activity 1  
## Feature Hierarchy – Model Answer

---

# Activity 1 – Expected Layer Mapping

Students’ three boxes:

- **Early Layer**
- **Middle Layer**
- **Late Layer**

Correct (or at least standard) mapping:

- **Early layer**:
  - Short edges, simple corners, color blobs
- **Middle layer**:
  - Eyes, noses, paws, ears (parts / local patterns)
- **Late layer**:
  - Whole animals (cat, dog, horse – class-level concepts)

---

# Activity 1 – Reasoning to Draw Out

Key points to emphasize:

- Deep networks learn **hierarchical representations**:
  - Simple → complex
- Early layers see **small local patches**:
  - They detect low-level visual primitives.
- Middle layers combine low-level features into **parts**.
- Late layers combine parts into **full objects**.

Good student explanations might compare to:

- Text: letters → syllables → words → sentences
- Audio: simple frequencies → phonemes → words

---

class: lead

# Activity 2  
## Forward Pass – Model Answer

---

# Activity 2 – Network Reminder

Hidden layer:

- $$z_1 = 2x_1 + 1x_2 - 1,\quad h_1 = \text{ReLU}(z_1)$$
- $$z_2 = -1x_1 + 2x_2 + 0,\quad h_2 = \text{ReLU}(z_2)$$

Output:

- $$\hat{y} = 0.5 h_1 + 0.5 h_2$$

Inputs:

1. (0, 0)
2. (2, 1)
3. (1, 2)

---

# Activity 2 – Case 1: (x₁, x₂) = (0, 0)

Compute:

- $$z_1 = 2\cdot 0 + 1\cdot 0 - 1 = -1$$  
  $$h_1 = \text{ReLU}(-1) = 0$$

- $$z_2 = -1\cdot 0 + 2\cdot 0 + 0 = 0$$  
  $$h_2 = \text{ReLU}(0) = 0$$

Output:

- $$\hat{y} = 0.5\cdot 0 + 0.5\cdot 0 = 0$$

**Expected answer:** $$\hat{y} = 0$$

---

# Activity 2 – Case 2: (x₁, x₂) = (2, 1)

Compute:

- $$z_1 = 2\cdot 2 + 1\cdot 1 - 1 = 4 + 1 - 1 = 4$$  
  $$h_1 = \text{ReLU}(4) = 4$$

- $$z_2 = -1\cdot 2 + 2\cdot 1 + 0 = -2 + 2 = 0$$  
  $$h_2 = \text{ReLU}(0) = 0$$

Output:

- $$\hat{y} = 0.5\cdot 4 + 0.5\cdot 0 = 2 + 0 = 2$$

**Expected answer:** $$\hat{y} = 2$$

---

# Activity 2 – Case 3: (x₁, x₂) = (1, 2)

Compute:

- $$z_1 = 2\cdot 1 + 1\cdot 2 - 1 = 2 + 2 - 1 = 3$$  
  $$h_1 = \text{ReLU}(3) = 3$$

- $$z_2 = -1\cdot 1 + 2\cdot 2 + 0 = -1 + 4 = 3$$  
  $$h_2 = \text{ReLU}(3) = 3$$

Output:

- $$\hat{y} = 0.5\cdot 3 + 0.5\cdot 3 = 1.5 + 1.5 = 3$$

**Expected answer:** $$\hat{y} = 3$$

---

# Activity 2 – Conceptual Points to Emphasize

- For (0,0), both neurons output 0 → network predicts 0.
- ReLU **zeros out negative** pre-activations (e.g., -1 → 0).
- With ReLU, the network behaves **piecewise linearly**:
  - Certain input regions turn some neurons “on” or “off”.
- Without ReLU (i.e., $$h_i = z_i$$), the whole network would remain **linear** overall:
  - Multiple linear layers without non-linearity collapse into a single linear transformation.

Good discussion questions:

- “What regions of (x₁, x₂) space activate which neurons?”
- “How does this enable more complex decision boundaries?”

---

class: lead

# Activity 3  
## Overfitting vs Generalization – Model Answer

---

# Activity 3 – Data Reminder

1D data:

| x  | Label |
|----|-------|
| 0  | 0     |
| 1  | 0     |
| 2  | 1     |
| 3  | 1     |
| 4  | 1     |
| 5  | 0     |
| 6  | 0     |

Students draw ○ (0) and ● (1) on a 1D axis.

---

# Activity 3 – Expected Sketches

**1. Underfitting model:**

- Almost constant prediction, e.g. always 0, or a very basic step that misses the change around x=2–4.
- It ignores clear structure in the data.

**2. Overfitting model:**

- Very wiggly boundary / curve that perfectly fits each data point:
  - Jumps up/down at each x to exactly match 0/1 labels.
- Clearly **too sensitive** to individual points.

**3. Reasonable model:**

- Simple rule that captures the main pattern, e.g.:

  > Predict 1 if x is between about 2 and 4, else 0.

- This might misclassify one point near the edges but captures the overall trend.

---

# Activity 3 – Interpretation to Draw Out

Key messages:

- **Underfitting**:
  - Model too simple.
  - High error on both training and test data.
  - Doesn’t capture pattern that 2–4 → label 1.

- **Overfitting**:
  - Model too complex.
  - Can get 0 training error by memorizing.
  - Likely to perform poorly on new x values (e.g., 2.5, 3.5, 7).

- **Good generalization**:
  - Simple decision rule that captures main structure.
  - Accepts some training error to be more robust.

Then connect to deep learning:

- Deep networks with **too many parameters** and **too little data** can overfit badly.
- Regularization, more data, and good validation practices are necessary.

---

class: lead

# Activity 4  
## Vanishing & Exploding Gradients – Model Answer

---

# Activity 4 – Vanishing Gradients (Multiply by 0.5)

Starting value: gradient = 1.0

Multiply by **0.5** each step:

- After 1 layer: $$1.0 \times 0.5 = 0.5$$
- After 2 layers: $$0.5 \times 0.5 = 0.25$$
- After 5 layers: $$1.0 \times 0.5^5 = 1.0 \times \frac{1}{32} \approx 0.03125$$
- After 10 layers: $$1.0 \times 0.5^{10} = \frac{1}{1024} \approx 0.00098$$

**Observation:**

- The gradient quickly becomes **very close to 0**.
- Earlier layers receive almost **no learning signal**.

---

# Activity 4 – Exploding Gradients (Multiply by 1.5)

Starting value: gradient = 1.0

Multiply by **1.5** each step:

- After 1 layer: $$1.0 \times 1.5 = 1.5$$
- After 2 layers: $$1.5 \times 1.5 = 2.25$$
- After 5 layers: $$1.0 \times 1.5^5 \approx 7.59$$
- After 10 layers: $$1.0 \times 1.5^{10} \approx 57.67$$

**Observation:**

- The gradient grows **very large** as layers increase.
- Weight updates become **huge and unstable**.

---

# Activity 4 – Conceptual Answers

**Why are very small gradients a problem?**

- Early layers hardly change during training.
- Network cannot effectively learn useful low-level features.
- Training appears to “stall”; loss stops decreasing.

**Why are very large gradients a problem?**

- Parameter updates become enormous.
- Loss can bounce around or diverge.
- Training is unstable and may “blow up”.

---

# Activity 4 – Links to Deep Learning Practices

Connect the game to design strategies:

- **Better activations**:
  - ReLU helps maintain gradient flow better than sigmoid/tanh in many cases.
- **Initialization**:
  - Xavier/He initialization aim to keep activations & gradients in a healthy range.
- **Normalization layers**:
  - BatchNorm, LayerNorm stabilize distributions across layers.
- **Residual / skip connections**:
  - Provide “shortcuts” for gradients to flow through deep networks (ResNets).

Key takeaway you want students to state:

> Deep networks are powerful but fragile; we need careful design to avoid vanishing and exploding gradients.

---

# End of Instructor Notes

These model answers are guides:

- Accept any student reasoning that is **conceptually correct**, even if sketches or numbers differ slightly.
- Emphasize **intuition and explanation** over exact numeric precision (except in Activity 2 and the simple gradient multiplications in Activity 4).

---