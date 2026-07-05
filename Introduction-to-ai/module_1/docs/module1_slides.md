---
marp: true
theme: default
paginate: true
header: 'Module 1: The Old Way: Symbolic AI'
footer: 'Evolution Symbolic AI'
---

# Module 1: The Old Way – Symbolic AI  
## From Hard‑Coded Rules to Learned Transformations

**Core focus today**

1. Understand **Symbolic AI / GOFAI**
2. See where it **works** and where it **breaks**
3. Understand why AI moved toward **Machine Learning**
4. Brief preview of the **new learning engines** (next module)

---

# Part I  
## What Is Symbolic AI?

---

# Symbolic AI in One Sentence

> **Symbolic AI** views intelligence as the **manipulation of symbols** using **explicit rules**.

- Knowledge = symbols (e.g. CAT, HUMAN, DISEASE_X)
- Reasoning = applying rules:  
  `IF condition THEN conclusion`
- Goal: mimic human reasoning by encoding our **logic** directly into code.

---

# Origin of “Symbolic AI” and “GOFAI”

- Approach dates back to the **1950s**:
  - John McCarthy, Allen Newell, Herbert A. Simon, others.
- **“Symbolic AI”**:
  - Name used to distinguish these logic‑based systems from later **connectionist** (neural) models.
- **GOFAI – Good Old‑Fashioned AI**:
  - Coined by **John Haugeland** (1985) to describe this dominant paradigm:
    - Intelligence = “mechanical manipulation of meaningful symbols according to syntactic rules”.

---

# The Physical Symbol System Hypothesis

Newell & Simon (1970s):

> A physical symbol system has the **necessary and sufficient** means for general intelligent action.

Implications:

- If we can:
  - Represent concepts as **symbols**, and
  - Encode relations as **rules**,
- Then we can, in principle, build **general intelligence**.

This hypothesis justified decades of focus on symbolic systems.

---

# Why Symbolic AI Was Attractive

- **Transparency**
  - Rules are human‑readable.
  - You can trace *why* a system reached a conclusion.
- **Control**
  - Domain experts decide which rules exist.
- **Philosophical fit**
  - Connects naturally to logic, mathematics, rational reasoning.

Metaphor:

> Symbolic AI treats the computer like a **very literal librarian**:  
> it only knows exactly what is in the rule books.

---

# Part II  
## Symbolic AI in Practice

---

# Early Landmark Systems

Some classic symbolic systems:

- **Logic Theorist (1955)**  
  - Proved mathematical theorems using formal logic.
- **General Problem Solver (GPS) (1957)**  
  - Aimed to be a universal symbolic problem‑solver.
- **ELIZA (1966)**  
  - Pattern‑matching chatbot simulating a psychotherapist.

All built on **symbols + rules**, not learning from data.

---

# Expert Systems: Symbolic AI at Scale

Peak of Symbolic AI: **Expert Systems**

- **Dendral (1960s)**  
  - Helped chemists identify molecules from mass spectra.
- **MYCIN (1970s)**  
  - Diagnosed bacterial infections, recommended antibiotics.
- **XCON (late 1970s–1980s)**  
  - Configured VAX computers at DEC; saved tens of millions of dollars.
- **Deep Blue (1990s)**  
  - Defeated world chess champion Garry Kasparov using search + rule‑based evaluation.

These systems showed symbolic AI **can work very well** in **narrow, structured domains**.

---

# Strengths of Expert Systems

- Perform **expert‑level** reasoning in a narrow domain.
- Very **predictable**:
  - Same inputs → same outputs.
- Easy to **audit**:
  - You can print the rules and inspect them.
- Good fit for:
  - Well‑defined rules
  - Stable environments
  - Low noise

But cracks started to appear…

---

class: lead

# Part III  
## Why Symbolic AI Hit a Wall

---

# The Knowledge Acquisition Bottleneck

Expert Systems required **humans to type every rule**:

- Extracting knowledge from experts is **slow** and **hard**:
  - Experts often use intuition or “gut feeling”.
- “Knowledge engineers” had to:
  - Interview experts
  - Translate intuition into thousands of `IF–THEN` rules
- As domains grew, rule bases reached **tens of thousands** of rules.

Result: the **Knowledge Acquisition Bottleneck**  
→ scaling systems became economically impossible.

---

# Brittleness: No Common Sense

Symbolic systems:

- Operate only inside their **narrow, predefined world**.
- Example:
  - A medical expert system given data from a **rusty engine**:
    - It still tries to diagnose a human disease, because it blindly applies medical rules.
- They cannot:
  - Recognize “this input is outside my domain”
  - Make **educated guesses** in novel situations.

In messy real‑world environments, systems often **shatter** instead of degrading gracefully.

---

# Maintenance Nightmare

As rule bases grew:

- Adding new rules could **conflict** with old ones.
- Unexpected interactions:
  - Rule #10 001 contradicts Rule #452.
- Debugging:
  - Extremely hard to trace errors back to specific rules.
  - Maintenance costs exploded.

Many large expert‑system projects became **unmaintainable** and were eventually scrapped.

---

# The AI Winter

Combined effects:

- Knowledge acquisition bottleneck
- Brittleness in real‑world applications
- Maintenance and debugging complexity
- Over‑promising + under‑delivering

Outcome:

- Funding and enthusiasm for symbolic AI **collapsed** in the late 1980s–1990s.
- This period is known as an **AI Winter**.

The field needed **new engines** for intelligence.

---


# Part IV  
## From Symbolic AI to Machine Learning

---

# Top‑Down vs Bottom‑Up

**Symbolic AI (Top‑Down)**

- Humans **write the rules**. --> The system applies them to data.

**Machine Learning (Bottom‑Up)**

- Humans provide **data + labels**. -->  The system **learns the rules** automatically via optimization.

Example: recognizing a **cat** in images.

- Symbolic AI: Define rules: “pointy ears”, “whiskers”, “four legs”, …
- Machine Learning: Show thousands of **cat / not‑cat** images.  
  - The model **discovers its own representation** of “cat‑ness”.

---

# Why Machine Learning Became Necessary

Three deep limitations of Symbolic AI:

1. **Knowledge acquisition**:
   - Cannot scale to the complexity of everyday knowledge.
2. **Brittleness**:
   - Fails on noisy, high‑dimensional, ambiguous data.
3. **Maintenance**:
   - Huge rule bases become fragile and expensive.

At the same time:

- **Data** exploded (web, sensors, logs).
- **Compute** improved (GPUs, clusters).
- **Statistics & optimization** matured.

>  It became more effective to **learn from data** than to write rules by hand.

---

# From Logic to Learning Engines

Modern ML replaces “logic engines” with **learning engines** built on:

- **Matrix transformations**
- **Loss functions**
- **Gradients**
- **Iterative updates**

We stop trying to define “cat” explicitly and instead:

> Let the matrix transformation **discover a useful internal notion** of “cat‑ness” through optimization on data.

---

# Part V (Preview)  
## How Learning Engines Work

*(This part bridges to Module 2: Machine Learning)*

---

# Learning as Calibration

Think of a learning model as a **calibration machine**:

- The model has thousands of internal **dials** (weights).
- The **Loss Function** is the **judge**:
  - It measures how far the model’s prediction is from the truth.
- The **Optimizer**:
  - Tries small changes to the dials.
  - Keeps changes that make the judge **quieter** (lower loss).

Key idea:

> Learning = **automated calibration**, not hand‑written rules.

---

# The Learning Engine: Roles at a Glance

| Concept        | Analogy       | Role in AI                                        |
|----------------|--------------|---------------------------------------------------|
| Loss Function  | The Judge    | Measures performance; defines the goal            |
| Gradient       | The Compass  | Points in the direction of steepest descent       |
| Learning Rate  | Stride Length| Controls how big each update step is             |
| Weights        | The Dials    | Internal parameters being fine‑tuned              |[0]

These components make learning **bottom‑up** and data‑driven.

---

# Example Losses: Regression and Classification

**Regression (house prices)**

- Error = Predicted Price – Actual Price
- **Mean Squared Error**: (Squares the error)
  - Penalizes large mistakes more
  - Avoids positive/negative errors cancelling out

**Classification (spam detection)**

- Model predicts probability of spam (e.g. 0.9).
- **Cross‑Entropy Loss**: Measures the distance between predicted probability and true label (0 or 1).

> Loss gives a **single number** to minimize.

---

# Gradient Descent: Hiking in the Fog

Analogy:

- You are on a mountain at night in thick fog.
- You can’t see the valley, only feel the **slope**.

Concepts:

- **Gradient** = direction of **steepest uphill**.
- To go downhill (reduce loss), step in the **opposite direction**.
- **Learning rate** = stride length:
  - Too big → overshoot the valley.
  - Too small → take forever, might get stuck in a small dip.

<!--This is how models **improve themselves** step by step.-->

---

# Update Rule: Turning the Dials

Backpropagation + gradient descent give the update:

$$
w_{\text{new}} = w_{\text{old}} - (\text{learning rate} \times \text{gradient})
$$

Interpretation:

- If a weight’s gradient is **large**, it had a big effect on the error → update it more.
- If its gradient is **near zero**, it had little effect → update it less.

Over many iterations:

- Random weights become a **useful transformation**.
- The system **learns** instead of being programmed.

---

# Data Quality and Metrics (Why Rules Aren’t Enough)

Because learning is data‑driven:

- **Bad data → bad models** (“Garbage In, Garbage Out”).
  - Example: Walmart floor scrubbers failed when not trained on real‑world store chaos.
- **Wrong metrics → misleading success**.
  - Fraud detection:
    - Predict “no fraud” for everything → 99.985% accuracy, but useless.
    - Need metrics like **precision** and **recall**, not just accuracy.

These issues simply **do not show up in the same way** in small, rule‑based symbolic systems.

---

# Conclusion

---

# Symbolic AI vs Machine Learning – Big Picture

**Symbolic AI / GOFAI**

- Intelligence as **symbol manipulation + rules**
- Transparent, logical, controllable
- Strong in **narrow, clean, rule‑bound domains**
- Limited by **brittleness**, **knowledge acquisition**, and **maintenance**

**Machine Learning**

- Intelligence as **learned transformations** from data
- Less transparent, but far more **scalable and adaptable**
- Enabled by loss functions, gradients, and optimization
- Highly dependent on **data quality** and **metric choice**

---

# Looking Ahead

In the next modules, we will:

- Dive into the **learning engines** in detail:
  - Regression, classification, loss, optimization, evaluation.
- See how different model families (SVMs, decision trees, neural nets)  
  implement the idea of **learning transformations**.
- Connect back to:
  - Why symbolic rules are still useful
  - How **hybrid systems** can combine both worlds.

---

# Takeaway for Module 1:
 
We moved from **writing rules** to **learning transformations** because symbolic AI hit structural limits that data‑driven methods could overcome.
