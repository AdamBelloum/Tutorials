---
marp: true
theme: default
paginate: true
header: "Module: Brief History of AI"
footer: "From Rules to Learning"
---

# A Brief History of AI  
## From Foundations to Generative AI

- Presenter: Expert AI  
- Based on IEEE vTools material and historical sources
- Core idea: to understand today’s AI, we must know its **history and shifts**

> “A generation which ignores history has no past – and no future.”  
> — Robert A. Heinlein

---

# The Elusive Definition of Intelligence

- “As soon as it works, no one calls it AI anymore.” — John McCarthy  
- Intelligence is a **moving target** as technologies become routine.
- Today: AI literacy is no longer only for computer scientists.
- Students in **all disciplines** must:
  - Evaluate when AI is appropriate
  - Defend or challenge model choices for their domain

---

# Roadmap of This Talk

- **Foundations of Computing**
  - Traditional programming vs. data‑centric learning
- **The Scaling Problem**
  - Data, storage, and compute infrastructure
- **The AI Landscape**
  - AI vs. Machine Learning vs. Deep Learning
- **Historical Milestones**
  - From early neural nets to Transformers
- **Trust, Safety & Boundaries**
  - Adversarial risk, privacy, and ethics (high‑level preview)

---

class: lead

# SECTION I  
## The Paradigm Shift in Computing

---

# From Rules to Optimization

- Core question:  
  **How do we get machines to do what we want?**
- Old paradigm:  
  Humans **write explicit rules** the machine follows.
- New paradigm:  
  Machines **learn rules** via **mathematical optimization** on data.
- Enabler:  
  Big Data + large‑scale compute (data centers, clusters, GPUs).

---

# The Traditional Approach: Explicit Programming

**Workflow**

- Humans design and script fixed **rules**.
- Rules + input **data** are executed by the computer.
- System outputs an **answer**.

**Design profile**

> [Rules] + [Data] → **Program** → [Answers]

**Limitation**

- Works only when humans can **precisely specify** the rules  
  (e.g. sorting numbers, tax calculations, chess search).

---

# The Machine Learning Approach

**Inversion of control**

- Instead of coding rules:
  - Provide **data** + **target answers** (labels).
- A learning algorithm:
  - Adjusts internal parameters via iterative **training**.
- Result:
  - Learned **rules / model** (e.g. fitted equation, decision boundary).

**Design profile**

> [Data] + [Answers] → **ML Training** → [Rules / Model]

---

# The Dual Fuel of Modern AI

To discover useful rules **without explicit programming**, we need:

- **Massive datasets (Big Data)**
  - Many diverse examples → better generalization
- **Massive processing power (Data Centers)**
  - Billions of matrix operations
  - Highly parallel hardware (GPUs, TPUs, clusters)

Without enough **data** or **compute**, many ML methods fail in practice.

---

# Taxonomy of Machine Learning

Three broad families:

- **Supervised Learning**
  - Learn from labeled examples (input → known output).
- **Unsupervised Learning**
  - Discover structure in unlabeled data.
- **Reinforcement Learning**
  - Learn to act via rewards and penalties over time.

We’ll briefly illustrate each.

---

# Supervised Learning

**Goal**

- Learn a mapping from inputs to outputs  
  using labeled example pairs.

**Data**

- Requires **human‑labeled** or otherwise verified targets.

**Common tasks**

- **Classification**
  - Fraud detection, image labeling, medical diagnosis.
- **Regression**
  - Predicting prices, demand, or continuous trends.

---

# Unsupervised Learning

**Goal**

- Find **hidden structure** or distributions in unlabeled data.

**Data**

- Only raw inputs; no explicit labels.

**Common tasks**

- **Clustering**
  - Group customers by behavior patterns.
- **Dimensionality reduction**
  - Compress high‑dimensional data into fewer, informative features.

---

# Reinforcement Learning

**Goal**

- Train an **agent** to choose actions that maximize long‑term reward.

**Mechanism**

- Trial‑and‑error interaction with an **environment**.
- Receives **rewards / penalties** rather than labeled examples.

**Key ideas**

- Agent–environment loop
- Value functions: estimated future reward

**Applications**

- Robotics, autonomous driving, game playing (Go, Atari, chess)

---

# What Is Machine Learning?

> “Machine Learning is the scientific discipline concerned with algorithms that can **learn from data**.”

Two phases:

1. **Model building (training)**
   - Use historical data to fit an empirical model.
2. **Inference (deployment)**
   - Use the model to make predictions on **new** data  
     instead of following fixed, hand‑coded logic.

---

class: lead

# SECTION II  
## Data Pipelines & Workflows

---

# The Reality of Data

Raw data is **not** ready for ML:

- **Heterogeneous formats**
  - Images, audio, text, logs, tables
- **Missing values**
  - Gaps in records, broken rows
- **Noise**
  - Sensor errors, outliers, typos
- **Feature transformation**
  - Encoding categories, scaling, normalizing, engineering features

Much of ML practice = **data cleaning and preparation**.

---

# The End‑to‑End ML Workflow

High‑level pipeline:

1. **Input training data**
2. **Feature extraction / preprocessing**
3. **Train / fit model**
4. **Create trained model**

Then:

1. **Input test (or new) data**
2. Same **feature extraction**
3. **Evaluate / score** with the model

Goal: good performance on **unseen** data, not only training data.

---

# Generalization: Underfitting vs Overfitting

**Underfitting (High Bias)**

- Model too simple → misses important patterns.
- Example: straight line fitted to a highly curved relationship.

**Overfitting (High Variance)**

- Model too complex → memorizes noise and outliers.
- Example: high‑degree polynomial that hits every training point but fails on new data.

Good models strike a **balance**.

---

# Validation Strategies

To measure generalization properly:

- **Train / Test split**
  - Simple: e.g. 75% train, 25% test.
- **Train / Validation / Test**
  - Train: fit parameters  
  - Validation: tune hyperparameters  
  - Test: final unbiased evaluation
- **Cross‑validation (e.g. K‑fold)**
  - Rotate which subset acts as validation.
- Variants:
  - Stratified CV, nested CV, time‑series splits.

Never evaluate on the **same data used for training**.

---

# Algorithm Choice and Complexity (Overview)

Different models have different costs:

- **Linear models**
  - Fast to train and predict; low memory footprint.
- **Instance‑based methods (e.g. KNN)**
  - Almost no training cost; slow prediction; high memory.
- **Tree‑based models (e.g. decision trees)**
  - Training cost grows with number of samples and features.
  - Prediction cost grows with tree depth.

Choosing an algorithm means balancing:

- Data size and dimensionality
- Memory and latency constraints
- Required accuracy and interpretability

---

# Beyond Superficial AI Skills

**Superficial use**

- Treats AI as a black box.
- Knows how to call `.fit()` and `.predict()` on standard libraries.

**Engineering reality**

- When models fail in production, we must:
  - Diagnose data issues and pipeline bugs.
  - Understand model behavior (e.g., bias/variance tradeoff, feature effects).
- For advanced systems (deep learning, Transformers), this includes:
  - Backprop dynamics, vanishing/exploding gradients
  - Embeddings, attention, and model architecture choices.

Deep understanding turns AI from a **gadget** into a **reliable tool**.

---
---
class: lead

# SECTION III  
## Data Infrastructure & Storage Realities

- Data grows from **kilobytes** to **yottabytes**
- Moving data is limited by **physics** (bandwidth, latency)
- Computing on data needs **parallelism** (clusters, GPUs, TPUs)

---

# The Scale of Modern Big Data

- Storage units grow by factors of **10³**:

  $$
  \text{KB} \rightarrow \text{MB} \rightarrow \text{GB} \rightarrow 
  \text{TB} \rightarrow \text{PB} \rightarrow \text{EB} \rightarrow 
  \text{ZB} \rightarrow \text{YB}
  $$

- 1 **Terabyte (TB)** = $10^{12}$ bytes  
- 1 **Zettabyte (ZB)** = $10^{21}$ bytes  
  - Roughly the order of **global internet traffic** in a year

---

# What Does 1 TB Look Like?

Approximate capacity of a **1 TB drive**:

- ≈ **200,000** high‑quality audio files  
  - ~17,000 hours of music
- ≈ **256** standard‑definition 2‑hour movies  
  - ~500 hours of video
- ≈ **310,000** standard‑resolution photos

Even a **single TB** is a lot of real‑world content.

---

# Global Data Ingestion (Examples)

Why scalable infrastructure matters:

- **Google**:  
  - >20 **Petabytes/day** processed in distributed systems
- **Facebook** (Meta):  
  - >2.5 **PB/day** of user activity in data lakes
- **CERN – Large Hadron Collider**:  
  - ~15 **PB/year** of raw detector data

Modern AI is tied to this scale of data flow.

---

# The “Sneakernet” Bandwidth Paradox

Moving huge datasets over networks is hard:

- Transferring **hundreds of TB** over typical links hits hard bandwidth limits
- 2013 perspective:
  - Shipping physical **hard drives by plane** could be **faster** than the internet

Example:

- A 1 TB SSD ≈ 78 g  
- A plane full of drives → effective rate ≈ **150 EB/day**  
  - ≈ **14 Pb/s**, about **100×** average internet throughput (2013)

---

# Network Transfer Latency – Thought Experiments

**Case 1: 18 TB (≈ 60 human genomes)**

- Over a **1 Gbps** line:
  - Transfer takes **days**, even with perfect utilization

**Case 2: 1 Exabyte (EB = $10^6$ TB)**

- Over a dedicated **10 Gbps** link:
  - ≈ **26 years** of continuous upload

**Reality:**  
Cloud providers use **physical transfer** tools (e.g. AWS Snowmobile trucks) to move EB‑scale data in **weeks**.

---

# Processing Latency: The Terabyte Sort

How long to sort **1 TB** of data?

- **Single machine**
  - Disk read/write ≈ 100 MB/s
  - Idealized processing: ≈ **341 minutes** (~5.6 hours)

- **Large distributed cluster**
  - 2008 benchmark (MapReduce on 910 nodes):
  - 1 TB sort in **68 seconds**

Parallelism can turn **hours into seconds**.

---

# Does Adding CPUs Always Help?

Computational scaling behaviors:

- **Linear scaling**
  - 2× cores → ~2× speedup
- **Super‑linear scaling**
  - Better than linear (e.g. data now fits in caches across nodes)
- **Sub‑linear scaling (Amdahl’s Law)**
  - Diminishing returns:
    - Sequential parts of the code
    - Network communication overhead
    - Synchronization costs

More hardware ≠ unlimited speedup.

---

# Hardware Acceleration: GPUs & TPUs

**CPUs**

- Optimized for **sequential**, diverse tasks
- Great for control logic, but slow for massive matrix math

**GPUs / TPUs**

- Thousands of simple arithmetic units
- Designed for **parallel** operations:
  - Millions of multiply‑adds in parallel
- Essential for:
  - Deep learning training
  - Large‑scale simulations

Example:

- Complex biomedical simulations that take hours on a CPU  
  can be sped up dramatically using OpenCL/CUDA on GPUs.

---

class: lead

# SECTION IV  
## Historical Evolution of AI

---

# AI Roots (1940s–1950s)

Foundational ideas:

- **1943 – McCulloch & Pitts**
  - First mathematical model of a **neuron**
  - Basis for artificial neural networks
- **1950 – Alan Turing**
  - Proposes the **Turing Test**:
    - Can a machine’s conversation be indistinguishable from a human’s?
- **1956 – Dartmouth Workshop**
  - McCarthy, Minsky, Rochester, Shannon
  - Coins the term **“Artificial Intelligence”**

---

# Mapping the AI Landscape

Nested vocabulary (conceptual diagram):

- **Artificial Intelligence**
  - Rule‑based systems, search, logic
  - ⮡ **Machine Learning**
    - Linear/logistic regression, random forests, SVMs
    - ⮡ **Deep Learning**
      - MLPs, CNNs, RNNs, LSTMs, autoencoders
      - ⮡ **Generative AI**
        - GANs, Transformers, Large Language Models (LLMs)

Not all AI is ML; not all ML is deep learning; not all deep learning is generative.

---

# Inside the Black Box: Deep Learning

Deep learning models:

- Stack many **hidden layers** to learn complex features from raw data.

Two passes:

- **Forward pass**
  - Data flows through layers to produce an output
  - Compute loss (e.g. MSE, cross‑entropy) vs. ground truth
- **Backward pass (backpropagation)**
  - Use the **chain rule** to compute gradients layer by layer
  - Update weights to reduce loss

Key training issues:

- **Vanishing gradients**: updates become too small in early layers
- **Exploding gradients**: updates become excessively large

---

# From Hand‑Crafted to Learned Features

Evolution in **computer vision**:

- Early era:
  - Hand‑crafted features + probabilistic models (e.g. HMMs for sequences)
- Deep learning era:
  - **Convolutional Neural Networks (CNNs)**:
    - Automatically learn spatial patterns (edges, textures, objects)
    - Dramatically outperform manual feature pipelines

CNNs shifted vision from **feature engineering** to **feature learning**.

---

# LeNet‑5 and MNIST (1998)

**MNIST dataset**

- Handwritten digits 0–9
- Became a standard benchmark for image recognition

**LeNet‑5 (Yann LeCun)**

- Introduced:
  - Local receptive fields
  - Shared weights (convolutions)
  - Subsampling / pooling
- Achieved ≈ **99% accuracy** on digit recognition
- Proof‑of‑concept that deep CNNs can learn visual hierarchies.

---

# Beyond Digits: CIFAR Datasets

**CIFAR‑10 / CIFAR‑100 (2009)**

- Small natural images across many classes:
  - Animals, vehicles, everyday objects
- Posed a harder challenge than MNIST:
  - Complex backgrounds
  - Varying lighting, viewpoints, clutter

These datasets tested whether models could **generalize** to realistic, high‑variation images.

---

# ImageNet: The Deep Learning Breakthrough

**ImageNet Large Scale Visual Recognition Challenge (ILSVRC)**

- Annual competition (2010–2017)
- Millions of images, 1000+ categories

**2012 Inflection Point**

- **AlexNet** (Krizhevsky, Sutskever, Hinton):
  - Deep CNN, trained on GPUs
  - Beat traditional methods by a **huge margin**
- Sparked the modern **deep learning boom** in vision and beyond.

---

# Deep Reinforcement Learning Milestones

**Deep Q‑Networks (DQN) – 2013**

- Mnih et al. (DeepMind)
- Combined:
  - Deep neural nets + Q‑learning
- Learned Atari games directly from **pixels** via trial and error.

**AlphaGo – 2016**

- DeepMind’s system defeated **Lee Sedol**, Go world champion.
- Combined:
  - Deep learning, Monte‑Carlo tree search, reinforcement learning
- Showed deep RL can master extremely complex strategy spaces.

---

# Encoder–Decoder Architectures

Why encoder–decoder?

- **Encoder**:
  - Compresses high‑dimensional input (image, audio, text)  
    into a compact **feature representation**.
- **Decoder**:
  - Expands that representation into a new output format:
    - Pixel‑wise segmentation map
    - Translated sentence
    - Synthesized audio

Example:

- **U‑Net** (2015):  
  - Encoder–decoder CNN for medical image segmentation  
  - Produces **pixel‑level** output from image inputs.

---

class: lead

# SECTION V  
## The Era of Generative AI & LLMs

*(Content to follow in the next batch of slides)*

---
---
class: lead

# SECTION V  
## Generative AI & Large Language Models

- Generating **new** content, not just classifying data
- Multi‑modal synthesis (text, image, audio, code)
- GANs, Transformers, and the rise of **LLMs**

---

# What Is Generative AI?

**Definition**

- Subfield of AI focused on **creating new data**:
  - Natural language text
  - Images and video
  - Audio and music
  - Code and other artifacts

**High‑level flow**

- Massive training data → **GenAI model** → new synthetic outputs
- Model learns **patterns**, not exact copies of training data.

---

# Multi‑Modal Output Capabilities

Modern generative models can produce:

- **Audio**
  - Text‑to‑speech, music composition, voice cloning
- **Video**
  - Short clips from text prompts, trailer generation, restoration
- **Images**
  - Concept art, style transfer, in‑painting, design assets
- **Text**
  - Creative writing, summarization, translation, code generation

Same core idea: map a **prompt** → a **new artifact**.

---

# Generative Adversarial Networks (GANs)

Two‑network competitive setup:

- **Generator**
  - Tries to create fake samples that look real.
- **Discriminator**
  - Tries to distinguish **real** vs **fake** samples.

Training loop:

1. Generator produces synthetic data.
2. Discriminator scores it.
3. Both networks update based on each other’s performance.

Result:

- Increasingly **realistic** outputs (faces, artworks, etc.).

---

# Language Models & Embeddings

**Language Models (LMs)**

- Neural networks trained on large text corpora.
- Goal: model the **probability** of word sequences.

**Embeddings**

- Map words/tokens → dense numeric vectors.
- Words with similar meaning appear **close** in embedding space:
  - “Grandparent” near “elderly”, “adult”
  - “Infant” near “baby”, “child”

Embeddings turn discrete language into **continuous geometry**.

---

# Context Problems in Static Embeddings

Early embeddings gave **one fixed vector per word**:

- Word “mean” had a single representation, regardless of context:

  - “What do you **mean**?” (verb)
  - “You are being **mean**.” (adjective)
  - “The **mean** absolute error.” (math term)

Limitation:

- Model loses **context‑specific meaning** → confusion and errors.

---

# The Transformer Revolution

**Transformers** (Vaswani et al., 2017 – “Attention Is All You Need”):

- Replaced recurrence with **attention mechanisms**.
- Key ideas:
  - **Self‑attention**: each token can look at **all other tokens**.
  - Learn which parts of the input are most relevant for each position.

Benefits:

- Handles long‑range dependencies.
- Captures context so “mean” next to “absolute error” is clearly mathematical.

---

# Self‑Attention: Disambiguating “Bank”

Attention weights connect words to their **context clues**.

Example A (financial):

> “I put my **money** in the **bank**.”

- Attention links “bank” strongly to “money” → financial institution.

Example B (river):

> “The **river** overflowed its **bank**.”

- Attention links “bank” to “river” → geographic feature.

The same word gets **different internal representations** depending on context.

---

# Large Language Models (LLMs)

Characteristics:

- **Billions+** of parameters
- Trained on **hundreds of GBs** of text
  - Equivalent to tens of thousands of full book series

Emergence:

- Above certain scale, models show **unexpected abilities**:
  - Multi‑step reasoning
  - Few‑shot learning from just a handful of examples
  - Following complex natural language instructions

---

# GPT and Next‑Token Prediction

**GPT = Generative Pre‑trained Transformer**

Core mechanism:

- Given previous tokens, predict the **next token**.
- Repeat many times → full paragraph, answer, or dialogue.

Training phases:

1. **Pre‑training**
   - Learn general language statistics from massive unlabeled text.
2. **Fine‑tuning / alignment**
   - Specialize on tasks, instructions, or safety goals.

Simple objective → surprisingly rich behavior.

---

# From Base Model to Assistant

Alignment pipeline (conceptual):

1. **Unsupervised pre‑training**
   - Learn generic language patterns.
2. **Supervised fine‑tuning**
   - Train on curated Q&A and instructions.
3. **Reward modeling**
   - Learn what humans prefer in responses.
4. **RLHF (Reinforcement Learning from Human Feedback)**
   - Optimize the model to be:
     - Helpful
     - Honest
     - Safer

This turns a raw LLM into a **useful assistant**.

---

# Timeline of LLM Capabilities

- **2018–2019**
  - Early GPT models show promise of Transformers for text.
  - Assistive robots like CIMON support astronauts on the ISS.
- **2020**
  - GPT‑3 (175B parameters) demonstrates strong few‑shot skills.
  - AlphaFold solves key protein‑folding benchmarks.
- **2023+**
  - GPT‑4 and multimodal models (text + image + more) become widely available.
  - Millions of users access powerful AI tools daily.

---

# Text‑to‑Image Generation

Modern diffusion and transformer‑based image models:

- Turn detailed **text prompts** into images.
- Control:
  - Style (photorealistic, sketch, anime, etc.)
  - Composition and layout
  - Lighting and atmosphere

Example:

> “A cinematic night‑time Tokyo street scene, neon lights, rainy reflections”  
→ model generates multiple matching images.

---

# Generative Video Capabilities

Recent video models can:

- Generate **short clips** directly from text prompts.
- Maintain **temporal coherence**:
  - Objects persist across frames
  - Motion appears natural
- Approximate simple **physics**:
  - Lighting changes
  - Camera pans and zooms
  - Basic interactions

Potential uses: pre‑visualization, VFX, education, rapid prototyping.

---

# Changing Academic Workflows

Expert projections:

- By mid‑2020s, advanced AI assistants can:
  - Help explore conjectures
  - Sketch proofs and counterexamples
  - Generate code and experiments

Implications:

- Human researchers focus more on:
  - Problem formulation
  - Conceptual insight
  - Checking and interpreting AI‑generated work

AI shifts from **tool** to **collaborator**.

---

class: lead

# SECTION VI  
## System Safety, Exploits & Vulnerabilities

---

# Hallucinations in LLMs

**Hallucination**

- LLM outputs that are:
  - Fluent and confident
  - But **factually wrong or invented**

Why it happens:

- Models optimize for **likely text**, not for truth.
- They do not have built‑in verified knowledge bases.

Real‑world example:

- In *Mata v. Avianca*, a lawyer used ChatGPT to find cases.
- The model fabricated legal citations → court sanctions.

---

# Logic & Reasoning Failure Modes

Pure language models can:

- Follow common text patterns
- But sometimes fail at **precise logical reasoning**

Example:

> “A juggler juggles 16 balls. Half are golf balls, and half of the golf balls are blue. How many blue golf balls?”

- Incorrect shortcut: “Half of 16 → 8” (ignores the second “half”)  
- Correct reasoning:  
  - 16 balls → 8 golf balls → 4 blue golf balls.

Modern reasoning‑tuned models do better, but the limitation is fundamental:  
models track **token probabilities**, not explicit symbolic logic.

---

# Mitigating Hallucinations in Practice

Defensive strategies:

- **Contextual constraints**
  - System prompts with explicit rules and boundaries.
- **Conversation framing**
  - Keep the model within a known domain or document scope.
- **Sampling controls**
  - Lower “temperature” or adjust decoding to reduce wild outputs.
- **Post‑processing**
  - Sanity checks, format validation, or secondary verification tools.

Goal: encourage **grounded**, not speculative, answers.

---

# Static Knowledge vs Dynamic Reality

Limitations of static training:

- After training, an LLM’s internal knowledge is **frozen** at a **cutoff date**.
- It cannot:
  - Natively know post‑cutoff events
  - Provide sources or citations for its statements.

Trust issues:

- Without external grounding, users cannot easily:
  - Verify where an answer came from
  - Check if it is up to date

This motivates hybrid architectures like **RAG**.

---

# Retrieval‑Augmented Generation (RAG)

How RAG works:

1. **User query**
   - e.g., “Summarize the latest policy from document X.”
2. **Retrieval**
   - Search external databases / documents for relevant passages.
3. **Augmented prompt**
   - Combine user question + retrieved context.
4. **Generation**
   - LLM answers *using that specific context*.
5. **Citations**
   - System can point back to retrieved sources.

Benefit:

- Answers are **grounded** in actual documents, reducing hallucinations and updating knowledge without retraining.

---

# Adversarial Security Exploits (Intro)

LLM systems also face **security threats**:

- **Prompt injection**
  - User tries to override system instructions.
- **Jailbreak attempts**
  - Crafted prompts to bypass safety filters.
- **Data exfiltration**
  - Extracting confidential information from integrated systems.

Mitigation requires:

- Careful system prompts and guardrails
- Input/output filtering
- Separation of sensitive tools and data

*(Deeper security patterns can be expanded in a dedicated session.)*

---

---

# Security Threats: Prompt Injections & Jailbreaking

As LLMs are wired into tools and workflows, new security risks appear:

- **Prompt injection attacks**
  - Malicious text tries to override system instructions and safety rules.
- **Indirect injection**
  - Hidden instructions embedded in web pages / documents that the LLM reads.
- **Common attack patterns**
  - Jailbreak prompts
  - Context manipulation (“ignore previous instructions…”)
  - Obfuscated code or data to exfiltrate secrets
  - Attempts to extract credentials or internal configuration

Defensive design is as important as model accuracy.

---

class: lead

# SECTION VII  
## Privacy, Trust & Governance

---

# The Myth of Simple Anonymization

Removing obvious identifiers (name, ID) is **not enough**:

- **Linkage attacks**
  - Cross‑link “anonymous” data with public sources to re‑identify people  
    (e.g., Netflix Prize dataset deanonymization).
- **A‑priori knowledge**
  - Attacker uses a few known facts about someone to locate their record.
- **Composition attacks**
  - Combine multiple releases over time to triangulate identities.

Conclusion: privacy must be **designed**, not assumed.

---

# Federated Learning: Decentralized Training

Goal: train a **shared model** without centralizing sensitive data.

- **Local training**
  - Each site (e.g. hospital, bank branch) keeps data on‑prem.
  - Trains a model update on its own data.
- **Central aggregation**
  - Only **model updates / weights** are sent to a server.
  - Server aggregates into a global model.

Risks:

- Malicious or poisoned updates
- Information leakage through model parameters

Federated learning improves privacy but does **not** solve it alone.

---

# Differential Privacy: Math‑Backed Protection

Differential Privacy (DP) gives **formal guarantees**:

- **Core idea**
  - Whether or not any single person’s data is in the training set  
    should barely change the model’s outputs.
- **Mechanism**
  - Add carefully calibrated **noise** to:
    - Data
    - Gradients
    - Query answers

Example:

- **Randomized response**
  - Individuals sometimes flip answers according to a known probability.
  - Protects individuals while preserving accurate **aggregate statistics**.

---

# Model Inversion & Reconstruction Risks

Without privacy controls, models can **memorize** data:

- **Reconstruction attacks**
  - Adversary probes a trained model to reconstruct training examples:
    - Faces, text snippets, health records, etc.
- **Membership inference**
  - Attacker infers whether a specific person’s data was in the training set.

Mitigation:

- Train with **differential privacy** and regularization.
- Limit access to model internals and predictions.

---

# Explainable AI (XAI)

Why we need explanations:

- High‑stakes decisions (credit, hiring, medicine, justice)  
  require **justification**, not just accuracy.

Approaches:

- **Global explanations**
  - Which features matter overall?
- **Local explanations**
  - Why this particular prediction?

Example method:

- **Feature attribution** (e.g. RISE–style masking)
  - Randomly mask parts of an input (pixels, words)
  - See how prediction changes
  - Highlight the regions that contribute most to the decision.

---

# The Future of Autonomous Agents

Beyond static chat:

- **Traditional LLMs**
  - Reactive: answer questions, translate, summarize.
- **Agentic LLMs**
  - Can:
    - Call tools and APIs
    - Browse the web
    - Write and run code
    - Plan and execute multi‑step tasks

Research example:

- **Stanford small‑town simulation**
  - Dozens of LLM‑powered agents lived in a sandbox world.
  - They independently:
    - Planned a party
    - Invited others
    - Coordinated schedules
    - Held the event
  - Demonstrated emergent social behavior.

---

# Prompt Engineering: Interacting with LLMs

**Prompt engineering** = designing prompts to steer model behavior  
without changing model weights.

High‑level flow:

- **Target objective** + **system context**  
  ↓
- **Optimized prompt** (instructions, examples, format)  
  ↓
- **High‑precision output** (more reliable and on‑task)

Good prompts act as a **user‑level programming language** for LLMs.

---

# Core Prompting Strategies

Common patterns:

- **Basic task prompts**
  - Summarization, classification, translation, role‑playing.
- **Zero‑shot prompting**
  - Ask directly, no examples.
- **Few‑shot prompting**
  - Include a handful of input–output examples in the prompt.
- **Chain‑of‑Thought (CoT)**
  - Tell the model: “Think step by step.”
  - Encourages explicit reasoning → often **better accuracy** on logic problems.

Prompt design is now a core **practical skill** for using LLMs effectively.

---

# Conclusion & Core Takeaways

- **Paradigm shift**
  - From hand‑coded rules → data‑driven optimization and learning.
- **Infrastructure realities**
  - AI is bounded by data volume, network bandwidth, and compute hardware.
- **Safety & governance**
  - Hallucinations, privacy leaks, and prompt injections require  
    careful system design and monitoring.
- **Path forward**
  - Combine **scale and capability** with:
    - Privacy and security
    - Explainability and governance
    - Thoughtful human oversight

AI’s future impact depends not just on what we **can** build,  
but on what we **choose** to build and how we deploy it.

---