---
marp: true
theme: default
size: 16:9
paginate: true
header: "Module 3: Deep Learning"
footer: "Deep Learning – Introductory Course"
---

# Module 3  
## Introduction to Deep Learning

- From **machine learning** to **deep learning**
- How **neural networks** are built
- How they **learn** (training & backprop)
- **Gradient issues** in deep networks
- Key **architectures** (CNN, RNN, Transformers)
- Strengths, limits, and **ethical questions**

---

class: lead

# 1. From Machine Learning to Deep Learning

---

# Recap from Module 2

You already know:

- A **model** maps input $$x$$ to output $$y$$.
- We choose a **loss function** to measure error.
- We use **gradient descent** to update weights.
- We worry about **overfitting** and **generalization**.

Deep learning = same ideas, but with **many layers** and **larger models**.

---

# What is Deep Learning?

**Deep Learning** is a subfield of Machine Learning that uses:

- **Neural networks** with **many layers** (deep)
- Lots of data
- Lots of compute

Key idea:

> Let the model **learn its own features** from raw data,  
> instead of manually designing features.

---

# Why Deep Learning?

Deep learning has driven breakthroughs in:

- **Computer vision** (image recognition, medical imaging)
- **Natural language processing** (translation, chatbots)
- **Speech recognition** (digital assistants)
- **Game playing** (Go, StarCraft)
- **Recommendation & personalization**

---

class: lead

# 2. Artificial Neural Networks  
## Neurons and Layers

---

# Artificial Neural Networks (ANNs)

An **Artificial Neural Network** is:

- A collection of simple units called **neurons**
- Organized into **layers**
- Connected by **weights**

Basic structure:

- **Input layer**: receives features
- **Hidden layers**: transform representations
- **Output layer**: produces prediction

---

# ANN as a Function

We view a neural network as a function:

$$
x \to h^{(1)} \to h^{(2)} \to \dots \to h^{(L)} \to \hat{y}
$$

Where:

- $$ x $$ = input vector (e.g. pixels, features)
- $$ h^{(l)} $$ = hidden representation at layer $$l$$
- $$ \hat{y} $$ = output (prediction)

Each layer applies a **transformation** to the previous one.

---

# Intuition: Assembly Line

Think of a neural network as a **factory assembly line**:

- Raw material = input data
- Each station (layer) **adds or transforms** something
- At the end, we get a **finished product** = prediction

Early layers learn **simple patterns**, later layers learn **more abstract concepts**.

---

# Example: House Price Prediction

- Input features:
  - Size, number of rooms, location, etc.
- Hidden layers:
  - Combine features into abstract concepts (e.g. “overall house quality”)
- Output layer:
  - A single number = predicted price

Same pipeline works for many tasks (images, text, audio).

---

class: lead

# 3. Weights, Biases, and Activation

---

# Weights and Biases

Each layer computes:

$$
z^{(l)} = W^{(l)} h^{(l-1)} + b^{(l)}
$$

- $$W^{(l)}$$ = weight matrix (connections strength)
- $$b^{(l)}$$ = bias vector (shifts)
- $$h^{(l-1)}$$ = input to this layer
- $$z^{(l)}$$ = raw output (before activation)

Weights and biases are the **parameters** we learn.

---

# Intuition: Dials and Thresholds

- **Weights**:
  - Like **dials** controlling how strongly each input influences the next neuron.
- **Biases**:
  - Like a **baseline** or threshold.
  - Even if inputs are small, the neuron may still fire if bias is high.

Training = turning all these dials until the network works well.

---

# Activation Functions

After the linear step, we apply a **non-linear** activation:

$$
h^{(l)} = \sigma(z^{(l)})
$$

Common activation functions:

- **ReLU**: $$\text{ReLU}(z) = \max(0, z)$$
- **Sigmoid**: $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
- **Softmax** (for multi-class outputs)

Without non-linearity, many layers collapse into **one big linear model**.

---

# Why Non-linearity?

Non-linear activations allow the network to learn:

- **Curved** decision boundaries
- Complex relationships like “if this AND that OR something else”

Without them, the network can only draw **straight lines / planes** in feature space.

---

# Example: ReLU

ReLU:

- If $$z < 0$$ → output = 0
- If $$z > 0$$ → output = $$z$$

Intuition:

- Negative or irrelevant signals are **shut off**
- Positive signals pass through unchanged

Benefits:

- Simple
- Works well in practice
- Helps training deep networks

---

class: lead

# 4. Forward Pass, Loss, and Training

---

# Forward Pass

Given input $$x$$:

1. Compute layer 1:
   - $$z^{(1)} = W^{(1)} x + b^{(1)}$$
   - $$h^{(1)} = \sigma(z^{(1)})$$
2. Compute layer 2:
   - $$z^{(2)} = W^{(2)} h^{(1)} + b^{(2)}$$
   - $$h^{(2)} = \sigma(z^{(2)})$$
3. Continue until output:
   - $$\hat{y} = h^{(L)}$$

This is the **forward pass**: computing the prediction.

---

# Loss Function (Reminder from Module 2)

The **loss function** measures how wrong the prediction is.

Examples:

- **Regression** (predicting numbers):
  - Mean Squared Error (MSE)
- **Binary classification**:
  - Binary Cross-Entropy
- **Multi-class classification**:
  - Cross-Entropy with softmax outputs

Training = adjust weights to **reduce loss** across many examples.

---

# Optimization: Gradient Descent (Recap)

We update parameters $$\Theta$$ (all weights and biases) by:

$$
\Theta_{\text{new}} = \Theta_{\text{old}} - \alpha \nabla_{\Theta} J(\Theta)
$$

Where:

- $$J(\Theta)$$ = loss over the training set
- $$\nabla_{\Theta} J$$ = gradient (direction of steepest increase)
- $$\alpha$$ = learning rate (step size)

We move **against** the gradient (downhill on the loss surface).

---

# Intuition: Hiking in the Fog

- Loss function = shape of the landscape (mountains and valleys)
- Gradient = direction where the ground slopes upward most steeply
- We want to go **downhill**, so we step in the opposite direction
- Learning rate = how big our steps are

Repeat many steps → (hopefully) reach a **valley** (low loss).

---

class: lead

# 5. Backpropagation and Gradient Issues

---

# What is Backpropagation?

Backpropagation = **Backwards Propagation of Errors**.

Purpose:

- Efficiently compute how **every weight** and **bias** affected the loss.
- Provide gradients needed for **gradient descent**.

High-level steps:

1. Do a **forward pass**, compute loss.
2. Do a **backward pass**:
   - Propagate error signals from output back to earlier layers.
   - Compute gradients for all weights and biases.

---

# Intuition: Passing the Blame Backwards

When the network makes a wrong prediction:

- Output layer gets the **first blame**.
- We ask: which neurons and weights contributed to this error?
- Backpropagation **distributes blame** backward:
  - Adjust output layer weights
  - Then adjust previous layers, and so on

This uses the **chain rule** from calculus, but conceptually it’s just:

> “Who needs to change, and in which direction, to reduce error?”

---

# Example Intuition

Image classifier mistakes a **cat** for a **dog**:

- Last layer: wrong category chosen → adjust these weights.
- Previous layer:
  - Maybe a “dog ear” detector neuron fired too strongly:
  - Backprop reduces its weights for this pattern.
- Even earlier layers:
  - Adjust edge and texture detectors that contributed.

Over time, the network **refines** all layers to better separate cats and dogs.

---

# You Don’t Need the Full Math (Yet)

For this course we focus on:

- What backprop **does**, not the full derivation.
- It gives us the gradient needed for **gradient descent**.
- Modern frameworks (PyTorch, TensorFlow) compute it automatically.

Key takeaway:

> Deep networks can be trained end-to-end because backprop efficiently tells us how to adjust every layer.

---

# Vanishing and Exploding Gradients

In **very deep networks**, gradients can:

- Become **very small** (vanish)
- Become **very large** (explode)

During backprop:

- Gradients are multiplied through many layers.
- Small numbers multiplied repeatedly → almost **zero**.
- Large numbers multiplied repeatedly → **huge** values.

Result:

- **Vanishing gradient**:
  - Early layers barely get updated → training stalls.
- **Exploding gradient**:
  - Updates are unstable → loss oscillates or diverges.

---

# Intuition: Whisper Chain and Feedback Loop

Two analogies:

- **Vanishing gradient**:
  - Like a message whispered through a long line of people.
  - By the time it reaches the start, it is **almost lost**.
- **Exploding gradient**:
  - Like a microphone too close to a speaker.
  - The sound feeds back and becomes **louder and louder**.

Both make it hard to train very deep networks.

---

# Coping with Gradient Problems (High-Level)

Modern deep learning uses several tricks to reduce vanishing / exploding gradients:

- **Better activations**:
  - ReLU and variants help keep gradients from shrinking too much.
- **Careful weight initialization**:
  - Start with weights scaled to keep activations/gradients in a reasonable range.
- **Normalization layers**:
  - Batch Normalization, Layer Normalization help stabilize training.
- **Residual connections** (skip connections):
  - Allow gradients to flow more directly through deep networks (as in ResNets).

You don’t need the formulas now; just know these techniques exist to make deep networks trainable.

---

class: lead

# 6. Training, Overfitting, and Regularization

---

# Train / Validation / Test (Recap)

We split the dataset:

- **Training set**: used to adjust weights
- **Validation set**: used to tune hyperparameters and monitor overfitting
- **Test set**: used once at the end to estimate final performance

For deep learning, this split is even more important because:

- Models are **very powerful** and can easily **overfit**.

---

# Overfitting in Deep Networks

Overfitting = model performs:

- Very well on **training data**
- Poorly on **validation / test data**

Deep networks can:

- Memorize training examples
- Learn patterns that don’t generalize

Symptoms:

- Training loss ↓
- Validation loss ↓ then ↑ (starts getting worse)

---

# Regularization: Keeping Models in Check

Common regularization techniques in deep learning:

- **L2 regularization (weight decay)**:
  - Penalize large weights, encourage simpler models
- **Dropout**:
  - Randomly zero out some neurons during training
- **Early stopping**:
  - Stop training when validation loss stops improving
- **Data augmentation**:
  - Create more varied training examples (especially for images)

---

# Dropout (Intuition)

Dropout:

- During training, each neuron has a chance to be **turned off** for that batch.
- The network cannot rely on any single neuron.
- It must spread knowledge across many neurons.

Result:

- Less memorization
- More robust, **general** features

---

# Data Augmentation (Intuition)

Instead of collecting more data, we:

- Modify existing data in realistic ways:

For images:

- Rotate, flip, crop, change brightness, add noise

Benefits:

- Model sees more **varied examples**
- Learns features that are robust to small changes
- Helps reduce overfitting

---

class: lead

# 7. Deep Learning Architectures

---

# Why Different Architectures?

Basic (fully-connected) networks treat all inputs the same way.

But:

- Images have **spatial structure** (nearby pixels matter together).
- Text and speech have **temporal / sequential structure** (order matters).

Specialized architectures exploit these structures:

- **Convolutional Neural Networks (CNNs)**
- **Recurrent Neural Networks (RNNs)**
- **Transformers**

---

# Convolutional Neural Networks (CNNs)

Designed for data on a **grid**, like images.

Key ideas:

- Use **small filters** (kernels) that slide over the image
- Filters detect local patterns:
  - Edges, corners, textures
- **Weight sharing**:
  - Same filter applied everywhere → fewer parameters

Result:

- Very good at recognizing **objects** in images.

---

# CNN Intuition: Feature Hierarchy

In an image classifier:

- Early layers:
  - Detect simple features (edges, corners)
- Middle layers:
  - Detect parts (eyes, noses, wheels)
- Deeper layers:
  - Detect whole objects (faces, cars, animals)

This **hierarchical feature learning** is a core strength of deep learning.

---

# Recurrent Neural Networks (RNNs)

Designed for **sequences**:

- Text (sentences, documents)
- Speech (audio frames)
- Time series (stock prices, sensor data)

Key idea:

- Maintain a **hidden state** $$h_t$$ that carries information from previous time steps.

Simplified update:

$$
h_t = \sigma(W_{hh} h_{t-1} + W_{xh} x_t + b_h)
$$

---

# RNN Intuition

Imagine reading a sentence word by word:

- At each new word, you **update your understanding**.
- You retain some memory of previous words.

RNNs try to mimic this by:

- Updating a hidden state step by step
- Using that state to make predictions (e.g., next word, sentiment)

---

# Limitations of Simple RNNs

Simple RNNs struggle with:

- Very long sequences
- Remembering information from far in the past
- **Vanishing gradients** across many time steps

Improvements:

- LSTMs (Long Short-Term Memory)
- GRUs (Gated Recurrent Units)
- Transformers (which avoid recurrence completely)

---

# Transformers

Transformers are the current **state-of-the-art** for many sequence tasks.

Key idea:

- Use **self-attention** to let each position in the sequence:
  - Look at **all other positions**
  - Decide which are most important

No recurrence, full parallelism → very efficient on modern hardware.

---

# Self-Attention (Intuition)

For a sentence:

> “The cat that sat on the mat was tired.”

To understand “was tired”, the model needs to focus on **“cat”**, not “mat”.

Self-attention:

- Computes **weights** that tell the model:
  - How much each word should attend to every other word
- Learns dependencies regardless of distance in the sentence.

---

# Transformers in Practice

Transformers power:

- Machine translation
- Large language models (chatbots, code assistants)
- Text summarization
- Many vision tasks (Vision Transformers)

Deep learning today is largely driven by **Transformer-based architectures**.

---

class: lead

# 8. Applications and Ethics

---

# Some Deep Learning Applications

- **Vision**:
  - Face recognition, autonomous driving, medical imaging
- **Language**:
  - Translation, question answering, chatbots
- **Audio**:
  - Speech recognition, music generation
- **Recommendation**:
  - Streaming services, online shops

Deep learning is embedded in many everyday technologies.

---

# Strengths of Deep Learning

- Handles **raw, high-dimensional data** (images, audio, text)
- Learns rich **representations** automatically
- Scales well with **more data** and **compute**
- Flexible: same basic ideas reused across domains

---

# Limitations and Risks

Technical challenges:

- **Vanishing / exploding gradients** in very deep or recurrent networks
- Needs **lots of data** and compute
- Can be **hard to interpret** (“black box”)
- Vulnerable to **adversarial examples**

Societal concerns:

- Can encode and amplify **biases** in data
- Environmental cost (energy use) for very large models

---

# Ethics and Responsibility

Important questions:

- Who is responsible when a deep learning system fails?
- How do we **audit** and **explain** model decisions?
- How do we ensure systems are **fair** across different groups?
- Should there be limits on certain applications?

As future practitioners, you will need to think about **both**:
- Technical performance, **and**
- Social impact

---

class: lead

# 9. Summary and Reflection

---

# Module 3 – Key Takeaways

You should now be able to:

- Explain what **deep learning** is and how it relates to ML
- Describe the structure of an **ANN** (neurons, layers, activations)
- Understand the roles of **weights**, **biases**, **loss**, **backprop**, and **gradients**
- Recognize **vanishing / exploding gradients** and why they matter
- Recognize **overfitting** and basic **regularization** techniques
- Distinguish between **CNNs**, **RNNs**, and **Transformers** at a high level
- Appreciate some **applications**, limitations, and **ethical issues**

---

# Quick Reflection (2–3 minutes)

Write down (or think about):

1. One deep learning concept you feel you **understand well**.
2. One concept you are still **uncertain** about.
3. One application of deep learning you find **exciting** or **concerning**, and why.

We will discuss some of your answers in the next session.

---

# Thank You

Next steps:

- Optional reading: introductory DL resources
- In future sessions: small demos / labs with simple neural networks

Questions?