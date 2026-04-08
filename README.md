# GEA1000 Project – Quantitative Reasoning with Data

**AY2025/2026 Semester 2**  
**Tutorial E38 Group 1**
---

## 📌 Overview

This project was completed as part of the course **GEA1000: Quantitative Reasoning with Data** in NUS.  

The project explores **health behaviours** through both **literature review** and **data analysis**, with the goal of generating insights that can inform policies to improve student well-being.

According to the project brief, the assignment consists of three parts:  
- **Part A:** Critical thinking with data (evaluation of a research paper)  
- **Part B:** Analysing data (exploratory data analysis on a health dataset)  
- **Part C:** Communicating with data (presentation and data storytelling)  

This repository contains the working files and final report for Part A and Part B.

---

## 📃 Chosen Research Paper (Part A)

We based our analysis on the following study:

> *Sleep quality of Singapore residents: findings from the 2016 Singapore mental health study*

This can be accessed [here](data/sleep_quality_study.pdf).

### Key focus:
- Investigates **sleep quality among Singapore residents**
- Examines relationships between sleep and:
  - Mental health
  - Physical health
  - Sociodemographic factors

### What we did:
- Identified **independent and dependent variables**
- Analysed **study design and methodology**
- Evaluated **confounders and sampling process**
- Critically assessed the **strengths, weaknesses, and generalisability**

---

## 📊 Data Analysis (Part B)

We performed **exploratory data analysis (EDA)** on a dataset of university students’ health behaviours.

### Key steps:

#### 1. Data Understanding & Cleaning
- Identified variable types (categorical, numerical)
- Standardised inconsistent entries (e.g., country names)
- Normalised GPA scales across countries
- Removed:
  - Missing BMI values
  - Impossible values (e.g., `BMI` = 0)
  - Outliers in sleep duration

#### 2. Data Visualisation & Analysis
We analysed relationships between health behaviours and outcomes:

- **Physical Activity (`PA_Days`)**
  - Found generally low activity levels among participants
- **BMI Analysis**
  - Compared BMI categories across countries
- **Physical Activity vs BMI**
  - Weak positive correlation observed
- **Hypothesis Testing**
  - Tested claims about:
    - Physical activity vs relaxedness
    - Fruit consumption among students

#### 3. Reflection & Insights
- Conducted additional analysis beyond required tasks
- Proposed new variables for future data collection
- Evaluated strengths and limitations of our analysis

---

## Repo Structure
```
project/
├── data/
│   ├── raw.csv
│   ├── processed.csv
│   └── sleep_quality_study.pdf
├── src/
│   └── preprocessing.py
├── paper/
|   ├── appendix.tex    # Supplementary materials
│   ├── cover.tex       # Cover page with student details
│   ├── main.tex        # Main document
│   ├── parta.tex       # Literature review and critique
│   ├── partb.tex       # Data analysis
│   ├── preamble.tex    # LaTeX packages and formatting
│   ├── references.bib  # Bibliography
│   └── report.pdf      # Final compiled report
└── eda.ipynb           # notebook for EDA
```

Go to [this link](https://www.overleaf.com/read/npbdgvskgcsg#5ae6f2) to view the final report on Overleaf.