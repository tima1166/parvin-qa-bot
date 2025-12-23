# 🖋️ Parvin E'tesami QA Bot

This repository contains a small NLP project that builds a question answering (QA) bot about the life and work of Parvin E'tesami, a famous Iranian poet.  
The bot uses a pre-trained transformer model to answer questions given a short English context.

---

## 🚀 Features

- Transformer-based QA using distilbert-base-cased-distilled-squad
- Two ways to run the project:
  - Jupyter Notebook demo
  - Command-line (CLI) app with app.py
- Confidence scores for each answer (how sure the model is)

---

## 📂 Project Structure

- notebooks/parvin_qa_demo.ipynb  
  Interactive notebook showing:
  - loading the QA model  
  - defining an English context about Parvin E'tesami  
  - asking several questions and printing answers + confidence scores  

- app.py  
  Command-line QA bot. When you run it:
  - loads the QA model  
  - prints a short intro  
  - lets you type questions like  
    - *"When was Parvin E'tesami born?"*  
    - *"What is she known for?"*  
  - shows the answer and confidence  
  - exits when you type quit, exit, or stop

- requirements.txt  
  List of Python dependencies for this project.

---

## 🛠️ Setup

```bash
# (Optional but recommended) create and activate a virtualenv

pip install -r requirements.txt