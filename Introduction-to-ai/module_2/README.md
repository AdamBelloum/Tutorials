# Module 2: Foundations of Machine Learning

## Overview
When logic rules fail to scale, we must build systems that extract architecture directly from empirical observation. This module covers classical **Supervised Machine Learning**, exploring how statistical models map feature spaces into stable predictions by treating learning as a geometric optimization problem.

##  Learning Objectives
* Distinguish between **parametric** models (fixed capacity) and **non-parametric** estimators (data-dependent scaling).
* Formulate mathematical loss functions (Mean Squared Error, Cross-Entropy) as operational measures of model deviation.
* Conceptualize space transformations where matrices rotate and stretch spaces to isolate mixed data coordinates.
* Maximize model generalization using robust training, validation, and test splits.

##  Core Theoretical Focus
* **Geometric Space Realignment:** Interpreting matrix multiplication as a spatial transformer designed to make features linearly separable.
* **Optimization Dynamics:** Walking downhill through loss landscapes using gradient descent updates ($w_{\text{new}} = w_{\text{old}} - \alpha \nabla J$).
* **Generalization Trade-offs:** Tracking the delicate boundary between structural underfitting (rigidity) and overfitting (memorizing stochastic noise).
* **Societal Amplification:** Identifying how objective mathematical transforms freeze and amplify historical data biases.

##  Assets & Resources
* **Lecture Material:** [Module 2 Slides](./doc/module2_slides.md)
* **Hands-on Lab:** [Interactive Decision Boundary Notebook](./hands-on/Hands-on-v1.0.md)
  * *Prerequisites:* `numpy`, `matplotlib`, `scikit-learn`
  * *Objective:* Programmatically build linear models, decision trees, and neighborhood estimators to observe their shifting decision boundaries under different hyperparameter constraints.

---
[⬅️ Back to Module 1](../module_1/README.md) | [Return to Main Directory](../README.md) | [Proceed to Module 3 ➡️](../module_3/README)
s