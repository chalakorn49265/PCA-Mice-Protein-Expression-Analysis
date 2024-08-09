# Regression Analysis Comments

## Notable Differentiators

The absolute magnitude of the coefficients indicates the relevance of the association between protein expression and class differentiation. A positive coefficient suggests a positive association, while a negative coefficient indicates an inverse relationship.

## Class-Specific Insights

### Class 0 (c-CS-s)
- **Key Characteristics**: Most protein expressions have positive coefficients.
- **Notable Proteins**:
  - **Positive**: pP70S6_N (highest positive coefficient)
  - **Negative**: Tau_N, DYRK1A_N, and GluR4_N
- **Insight**: These characteristics distinguish class 0 from other classes.

### Class 1 (c-CS-m)
- **Key Characteristics**: Positive coefficients for specific proteins.
- **Notable Proteins**:
  - **Positive**: EGR1_N, PSD95_N, and GFAP_N
  - **Negative**: Tau_N
- **Insight**: EGR1_N and GFAP_N play a key role in defining this class.

### Class 2 (c-SC-s)
- **Key Characteristics**: Strong negative coefficients.
- **Notable Proteins**:
  - **Negative**: EGR1_N and GFAP_N
- **Insight**: These proteins significantly distinguish this class in the opposite direction compared to others.

### Class 3 (c-SC-m)
- **Key Characteristics**: Significant negative coefficients.
- **Notable Proteins**:
  - **Negative**: EGR1_N, PSD95_N, and GluR4_N
- **Insight**: These proteins are key in differentiating this class.

### Class 4 (t-CS-s)
- **Key Characteristics**: Large divergence in coefficients.
- **Notable Proteins**:
  - **Divergent**: EGR1_N and GFAP_N
- **Insight**: These proteins distinguish this class.

### Class 5 (t-CS-m)
- **Key Characteristics**: Large positive and negative coefficients.
- **Notable Proteins**:
  - **Positive**: EGR1_N and GFAP_N
  - **Negative**: pPKCG_N and DYRK1A_N
- **Insight**: EGR1_N and GFAP_N are important for this class.

### Class 6 (t-SC-s)
- **Key Characteristics**: Positive coefficients for many predictors.
- **Notable Proteins**:
  - **Positive**: Especially high for Tau_N and DYRK1A_N
- **Insight**: These proteins are a key differentiation for this group.

### Class 7 (t-SC-m)
- **Key Characteristics**: All coefficients are negative.
- **Notable Proteins**:
  - **Negative**: Very large negative coefficient for pP70S6_N
- **Insight**: This protein is a prominent feature of this class.

## Conclusion

With the help of PCA, the 77 protein expressions were narrowed down to just 9 expressions. However, even with the dimensionally reduced features from PCA, there remains significant overlap between classes, as evident by the scatter plot for different principal components (PC1 and PC2).

Implementing a logistic regression model with a Lasso penalty helped identify subsets of proteins that are prominent in each class. This analysis helps to distinguish classes based on the size and sign of the coefficients. Certain predictors, like EGR1_N, PSD95_N, GFAP_N, and Tau_N, show significant coefficients (both positive and negative) across multiple classes, suggesting these proteins are crucial in differentiating between classes. The variation in the direction (positive or negative) of their coefficients across classes underscores the complexity of their roles in the biological processes under study.
