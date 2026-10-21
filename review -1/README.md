# Review 1: Credit Card Default Risk Analytics
**Course:** 23CSE351 — Foundations of Data Science  
**Lab Evaluation:** Evaluation 1  
**Dataset:** Default of Credit Card Clients Dataset (UCI Machine Learning Repository)  
**Origin:** Taiwanese Credit Card Issuer (30,000 customers × 24 features)  

---

## 📋 Overview
This project presents a complete statistical and analytical investigation of credit card default risk without training complex black-box classifiers. Using the customer demographic profiles, billing statements, and past repayment statuses, the analysis uncovers behavioral patterns and evaluates parameter confidence using probability distributions and sampling theory.

## 📂 Folder Contents
- **`Credit_Card_Risk_Analytics_Master.ipynb`**: Complete, fully executed Jupyter Notebook with student-friendly, moderate-English explanations, pre-rendered charts, and 15 answered questions.
- **`dataset/default of credit card clients.xls`**: Clean source dataset file.
- **`default_card/default of credit card clients.xls`**: Compatibility mirror path.

## 🔬 Key Methodological Topics Covered
1. **Data Preprocessing:**
   - Null and duplicate audit
   - Anomaly handling for undocumented category codes in education and marriage
   - Categorical label mapping and standard feature scaling (`StandardScaler`)
   - Principal Component Analysis (PCA) scree plot and 2D projection
   - Age discretization into standard demographic cohorts
2. **Vector and Matrix Operations (with "Why we need it:" callouts):**
   - Customer feature vectors
   - Vector addition and subtraction (Defaulters vs. Non-Defaulters average vectors)
   - Vector magnitude (`np.linalg.norm`)
   - Euclidean distance from the average customer
   - Dot product alignment
   - Matrix representation, transpose ($X$ and $X^T$), and matrix multiplication ($X^T X$)
   - Covariance and correlation matrices with heatmap visualization
3. **Exploratory Data Analysis (EDA):**
   - 15 framed analytical questions answered with Seaborn charts and concise plain-English interpretations.
4. **Probability Modeling:**
   - Statistical independence check using the multiplication rule: $P(A \cap B)$ vs. $P(A) 	imes P(B)$
   - Conditional probability curves comparing high-risk segments to the 22.12% baseline
   - Binomial distribution model ($n=10, p=0.2212$) with $k=2$ highlighted
5. **Sampling and Central Limit Theorem (CLT):**
   - Estimation precision and 95% margin of error across sample sizes ($n \in [50, 100, 500, 1000, 5000]$)
   - Sample variability reduction demonstration
   - $2 	imes 2$ subplot grid demonstrating normal curve emergence from sample means
