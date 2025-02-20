# Indirect Racism & Sexism Detection through Text Analysis

## Overview

This project aims to detect indirect racism, sexism, and hate speech in Greek television programs by analyzing transcribed speech. It utilizes **Natural Language Processing (NLP)** techniques and various machine learning models to classify statements into categories such as **hate speech, irony, racism, sexism, or neutral statements**.

## Key Features

- **Automatic Speech Recognition (ASR)** using `WhisperX` to transcribe Greek speech.
- **Text Classification** with multiple models (**SVM, Logistic Regression, Naïve Bayes**) to identify:
  - Hate speech
  - Irony
  - Racism
  - Sexism
  - Neutral statements
- **SMOTE for Imbalance Handling**: Applied only to training data in specific experiments.
- **Dimensionality Reduction (PCA)**: Implemented in certain versions to compare performance with and without PCA.

---

## Repository Structure

├── ML-presentation.pdf # Project presentation (slides)
├── newUploadFiles.py # Script for uploading new datasets 
├── transcribe_with_whisperx.py # ASR pipeline using WhisperX
├── new_labeled_dataset_withNOs.xlsx # Labeled dataset (text annotations)
├── new_approach.ipynb # Multi-class classifier (with PCA)
├── new_approach_no_pca2.ipynb # Multi-class classifier (without PCA)
├── new_approach_binary.ipynb # Binary classifier (with PCA)
├── new_approach_binary_no_pca.ipynb # Binary classifier (without PCA)


---

## Classifiers & Models

The project contains four classification pipelines:

1. **`new_approach_no_pca2.ipynb`**  
   - Multi-class classification (**SVM, LR, NB**)  
   - With and without SMOTE  
   - **Categories:** hate_speech, irony, racism, sexism, no  

2. **`new_approach_binary_no_pca.ipynb`**  
   - Binary classification (**SVM, LR, NB**)  
   - With and without SMOTE  
   - **Categories:** hate_speech, no  

3. **`new_approach.ipynb`**  
   - Same as `new_approach_no_pca2.ipynb`, but **with PCA** applied to the dataset.  

4. **`new_approach_binary.ipynb`**  
   - Same as `new_approach_binary_no_pca.ipynb`, but **with PCA** applied to the dataset.  

---

