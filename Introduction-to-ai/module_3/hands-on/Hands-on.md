---
marp: true
theme: default
size: 16:9
paginate: true
header: "Deep Learning – Hands‑on"
footer: "Student Slides"
---

# Deep Learning – Hands‑on Activities

In this session you will:

- Explore **layered representations**
- Run a **forward pass** in a tiny neural network
- Visualize **overfitting vs generalization**
- Experience **vanishing / exploding gradients** with a simple game

No coding required – mostly paper, pen, and discussion.

---

class: lead

# Activity 1  
## Feature Hierarchy in Deep Networks

---

# Activity 1 – Goal

Understand how different layers in a deep network learn:

- **Low-level** features
- **Mid-level** features
- **High-level** concepts

You will **match features to layers** and explain your choices.

---

# Activity 1 – Setup

Imagine a deep network that recognizes **animals in images**.

Possible features:

1. Short edges, simple corners, color blobs  
2. Eyes, noses, paws, ears  
3. Whole animals (cat, dog, horse)

In small groups, answer:

1. Which features are likely learned by **earlier layers**?
2. Which by **middle** layers?
3. Which by the **deepest** layers?

---

# Activity 1 – Task

1. On a sheet of paper, draw **three boxes**:

   - “Early Layer”
   - “Middle Layer”
   - “Late Layer”

2. Place each of these into one of the boxes and justify:

   - Short edges / corners / color patches  
   - Eyes / noses / paws  
   - Entire animals (cat, dog, horse)

3. Write 1–2 sentences explaining **why** you chose that ordering.

You will be asked to share your reasoning.

---

# Activity 1 – Discussion Prompt

As a group, discuss:

- Why does it make sense to **build up** from simple patterns to complex ones?
- How is this different from writing **manual features** in classic machine learning?

Be ready to explain your analogy to the class (e.g., letters → words → sentences).

---

class: lead

# Activity 2  
## Forward Pass in a Tiny Network

---

# Activity 2 – Goal

Understand how a neural network:

- Combines inputs with **weights and biases**
- Applies an **activation function** (ReLU)
- Produces an **output prediction**

You will compute a **forward pass by hand**.

---

# Activity 2 – Network Description

We have a very small network:

- **Inputs**: $$x_1, x_2$$
- **Hidden layer**: 2 neurons with ReLU activation
- **Output**: 1 neuron (linear)

Hidden layer:

- Neuron 1:  
  $$z_1 = 2x_1 + 1x_2 - 1$$  
  $$h_1 = \text{ReLU}(z_1)$$

- Neuron 2:  
  $$z_2 = -1x_1 + 2x_2 + 0$$  
  $$h_2 = \text{ReLU}(z_2)$$

Output layer:

- $$\hat{y} = 0.5 h_1 + 0.5 h_2$$

---

# Activity 2 – Task

For each input, compute the output of the network:

1. $$(x_1, x_2) = (0, 0)$$  
2. $$(x_1, x_2) = (2, 1)$$  
3. $$(x_1, x_2) = (1, 2)$$  

Steps for each input:

1. Compute $$z_1, z_2$$  
2. Apply ReLU: $$h_1, h_2$$  
3. Compute $$\hat{y} = 0.5 h_1 + 0.5 h_2$$

Work in pairs and compare results.

---

# Activity 2 – Reflection Questions

After computing:

- For which inputs did ReLU output **0**? Why?
- How would the output differ if we had **no ReLU** (i.e., $$h_i = z_i$$)?
- How do multiple layers + ReLU allow **non-linear** behaviour?

Be prepared to share your intuition, not just the numbers.

---

class: lead

# Activity 3  
## Overfitting vs Generalization (Doodles)

---

# Activity 3 – Goal

Visualize:

- **Underfitting**: model too simple  
- **Overfitting**: model too complex  
- **Good fit**: balances both

You will sketch different “decision boundaries” for the same toy dataset.

---

# Activity 3 – Setup

Consider a 1D input $$x$$ and binary labels (0 or 1):

| x  | Label |
|----|-------|
| 0  | 0     |
| 1  | 0     |
| 2  | 1     |
| 3  | 1     |
| 4  | 1     |
| 5  | 0     |
| 6  | 0     |

Imagine we want a model to predict label from $$x$$.

---

# Activity 3 – Task (On Paper)

On a piece of paper:

1. Draw a **horizontal line** for $$x$$ from 0 to 6.
2. Mark the data points at their x-positions:
   - Use ○ for label 0, ● for label 1.

Then sketch three possible models:

1. **Underfitting model**:
   - Very simple rule (e.g., almost constant prediction).
2. **Overfitting model**:
   - A very “wiggly” rule that tries to exactly match every point.
3. **Reasonable model**:
   - Simple but still captures the main pattern.

Label each sketch clearly.

---

# Activity 3 – Discussion Questions

In small groups, discuss:

- Which sketch is likely to perform **worst on new unseen points**? Why?
- Which one generalizes best to new $$x$$ values?
- How does this relate to **deep networks** with too many parameters and too little data?

You will share your conclusion with the class.

---

class: lead

# Activity 4  
## Vanishing & Exploding Gradients Game

---

# Activity 4 – Goal

Intuitively understand:

- **Vanishing gradients** (getting too small)
- **Exploding gradients** (getting too large)

You will simulate backpropagation using simple **number chains**.

---

# Activity 4 – Setup

Imagine a deep network with many layers.

In backpropagation, each layer **multiplies** the gradient by some factor.

We will simulate two cases:

1. Multiply by **0.5** at each step (shrinking)
2. Multiply by **1.5** at each step (growing)

---

# Activity 4 – Task A: Vanishing Gradient

1. Start with gradient = **1.0**
2. For each “layer” (step), multiply by **0.5**

Compute the gradient after:

- 1 layer
- 2 layers
- 5 layers
- 10 layers

Write down the values.

Question:

- What happens to the gradient as the number of layers grows?

---

# Activity 4 – Task B: Exploding Gradient

1. Start again with gradient = **1.0**
2. For each “layer” (step), multiply by **1.5**

Compute the gradient after:

- 1 layer
- 2 layers
- 5 layers
- 10 layers

Write down the values.

Question:

- What happens to the gradient as the number of layers grows?

---

# Activity 4 – Discussion

In groups, answer:

- Why are **very small** gradients a problem for learning?
- Why are **very large** gradients a problem?
- How might this connect to:
  - Difficulty training **very deep** networks
  - The need for design tricks like **ReLU**, **normalization**, and **skip connections**?

Be ready to explain your reasoning in simple language.

---

class: lead

# Wrap‑Up

---

# Wrap‑Up – What You Practiced

Today you:

- Matched features to **layers** (feature hierarchy)
- Computed a **forward pass** in a tiny network
- Sketched **overfitting vs generalization**
- Simulated **vanishing / exploding gradients**

These activities connect to:

- Network structure (layers, activations)
- Training (forward pass, gradients)
- Practical challenges in deep learning (overfitting, gradient issues)

Think about which activity gave you the **strongest intuition** and why.

---