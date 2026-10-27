# ==============================================================================
# MODULE 2: MACHINE LEARNING HANDS-ON
# Activity: Interactive Decision Boundaries in Python
# ==============================================================================
# This script guides participants through 4 distinct stages of model complexity:
#   1. Simple Linear Model (Good fit)
#   2. Linear Model on Complex Data (Underfitting)
#   3. Non-Linear Model on Complex Data (Good fit)
#   4. High-Flexibility Model on Noisy Data (Overfitting)
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 0: ENVIRONMENT SETUP & HELPER FUNCTION
# ------------------------------------------------------------------------------
# We import standard data generation, machine learning, and plotting libraries.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def plot_decision_boundary(model, X, y, title_text):
    """
    Helper function to visualize how a model splits feature space.
    It creates a fine dense grid across the data range, predicts the class 
    for every single grid point, and shades the background accordingly.
    """
    # Define bounds for the plotting canvas
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    
    # Generate a coordinate grid of points with a 0.02 step size
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), 
                         np.arange(y_min, y_max, 0.02))
    
    # Predict the class for every single coordinate point on our grid canvas
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid_points)
    Z = Z.reshape(xx.shape)
    
    # Plot background decision regions (Red vs Blue space)
    plt.figure(figsize=(7, 5))
    plt.contourf(xx, yy, Z, alpha=0.25, cmap=plt.cm.coolwarm)
    
    # Overlay the actual training data points onto the canvas
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm, s=40)
    
    # Calculate and display the exact training accuracy
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions) * 100
    
    plt.title(f"{title_text}\nTraining Accuracy: {accuracy:.1f}%")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

print("Setup complete! Helper function 'plot_decision_boundary' is ready.")

# ------------------------------------------------------------------------------
# STEP 1: SIMPLE LINEAR MODEL
# ------------------------------------------------------------------------------
# GOAL: Watch a linear model easily separate two distinct, linear clusters.

# 1. Generate a linearly separable dataset (Two distinct point blobs)
X_simple, y_simple = make_blobs(n_samples=200, centers=2, random_state=42, cluster_std=1.0)

# 2. Select and train a rigid Linear Model (Logistic Regression)
linear_model_step1 = LogisticRegression()
linear_model_step1.fit(X_simple, y_simple)

# 3. Visualize the straight line boundary
plot_decision_boundary(linear_model_step1, X_simple, y_simple, 
                       "Step 1: Logistic Regression on Simple Data")


# ------------------------------------------------------------------------------
# STEP 2: UNDERFITTING WITH LINEAR MODELS
# ------------------------------------------------------------------------------
# GOAL: Observe what happens when a rigid straight line model is forced to 
#       classify a complex, concentric circle pattern.

# 1. Generate a complex non-linear dataset (A circle inside a larger circle)
X_circle, y_circle = make_circles(n_samples=200, noise=0.08, factor=0.4, random_state=42)

# 2. Force the rigid linear model onto this structural circular data
linear_model_step2 = LogisticRegression()
linear_model_step2.fit(X_circle, y_circle)

# 3. Plot to observe how a straight line cannot capture a circle (Underfitting)
plot_decision_boundary(linear_model_step2, X_circle, y_circle, 
                       "Step 2: Linear Model Underfitting Circular Data")


# ------------------------------------------------------------------------------
# STEP 3: SWITCH TO NON-LINEAR MODELS
# ------------------------------------------------------------------------------
# GOAL: Introduce a flexible, non-linear architecture (Decision Tree) to bend 
#       and safely navigate the circular data pattern.

# 1. Use the exact same circular data from Step 2
# 2. Switch algorithm to a Decision Tree with controlled depth (Max Depth = 4)
tree_model_step3 = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model_step3.fit(X_circle, y_circle)

# 3. Plot to observe the dynamic, non-linear boundary grid wrapping the inner cluster
plot_decision_boundary(tree_model_step3, X_circle, y_circle, 
                       "Step 3: Decision Tree (Max Depth=4) on Circular Data")


# ------------------------------------------------------------------------------
# STEP 4: OVERFITTING (BONUS CHALLENGE)
# ------------------------------------------------------------------------------
# GOAL: See how giving a non-linear model *too much* architectural freedom 
#       causes it to overfit by chasing random structural noise and outliers.

# 1. Generate highly chaotic, noisy overlapping circles
X_noisy, y_noisy = make_circles(n_samples=200, noise=0.28, factor=0.5, random_state=12)

# 2. Train an unrestrained Decision Tree (No depth limit = maximum complexity)
overfit_tree_step4 = DecisionTreeClassifier(max_depth=None, random_state=42)
overfit_tree_step4.fit(X_noisy, y_noisy)

# 3. Plot to observe highly jagged boundaries and random decision "islands"
plot_decision_boundary(overfit_tree_step4, X_noisy, y_noisy, 
                       "Step 4: Overfitting Tree (No Depth Limit) on Noisy Data")
