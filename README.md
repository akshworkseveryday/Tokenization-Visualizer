# Tokenization Visualizer

## Overview

Tokenization Visualizer is an interactive web application built to explore how different tokenization strategies segment text in Natural Language Processing and modern Large Language Models.

As a student learning Artificial Intelligence, language models, and intelligent systems, I developed this project to apply theoretical concepts in a practical setting. The objective is to better understand how raw text is transformed into tokens before being processed by transformer-based models.

---

## Motivation

Tokenization is a foundational step in NLP pipelines. Different models use different strategies to split text into tokens, and these differences directly affect vocabulary size, token count, and model behavior.

This project was built to:

• Compare classical and modern tokenization methods  
• Observe how the same sentence is segmented differently  
• Understand subword tokenization used in LLMs  
• Strengthen practical intuition about text preprocessing  

---

## Implemented Tokenization Methods

Word Tokenization  

Character Tokenization  

Byte Pair Encoding using GPT-2  

WordPiece using BERT  

Unigram Language Model using T5 and SentencePiece  

These approaches represent techniques widely used in production-grade transformer architectures.

---

## Features

Interactive text input  

Selection between multiple tokenization methods  

Display of total token count and character count  

Token visualization using alternating pastel color blocks  

Optional display of token IDs  

Minimal and clean interface built with Streamlit  

---

## Tech Stack

Python  

Streamlit  

HuggingFace Transformers  

SentencePiece  

---

## Running Locally

Clone the repository:
