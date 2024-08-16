# PTT Beauty Board Sponsored Content Analysis

## Overview

This project aims to analyze whether posts on the PTT Beauty board are sponsored content. The study utilizes a combination of sentiment analysis, retrieval-augmented generation (RAG), and fine-tuning of large language models to gain insights into sponsored posts.

## Project Structure

- **data/**: Directory containing raw data used for analysis.
- **docker/**: Docker configurations and files.
- **note/**: Notes and documentation related to the project.
- **finetune_1.finetune_data_prepare.ipynb**: Notebook for preparing data for fine-tuning.
- **finetune_2.Llama_3_1_8b_finetuning.ipynb**: Notebook for fine-tuning the LLaMA 3.1-8B model.
- **main.py**: Main Python script for executing the analysis.
- **milvus_demo.db**: Database file for Milvus vector store demo.
- **milvus_playground.ipynb**: Notebook exploring Milvus vector search.
- **RAG_1.ETL.ipynb**: Notebook for ETL processes related to RAG.
- **RAG_2.RAG.ipynb**: Notebook for RAG model implementation.
- **sentiment_Analysis_2.bert_predect.ipynb**: Notebook for sentiment analysis prediction using BERT.
- **sentiment_Analysis_2.bert_train.ipynb**: Notebook for sentiment analysis training using BERT.

## Key Components

### Retrieval-Augmented Generation (RAG)
- **Langchain** and **vector search** are utilized to analyze brand-related data.
- Utilizes large language models like **GPT-4** and **Claude 3.5** to enhance analysis.

### Sentiment Analysis
- Conducted using **PaddleNLP** and **Chinese BERT**.
- Includes binary and ternary classification experiments on PTT comments.
- Fine-tuned models to improve accuracy.

### Fine-Tuning Meta-LLaMA-3.1-8B
- Fine-tuned to generate articles in the style of PTT forum discussions.
- Utilizes 4-bit quantization for memory efficiency.

## Data Source
- **Source**: PTT Beauty Board
- **Data Range**: 2010-2020
- **Total Posts**: 30,254 posts categorized as "心得" (reviews)

## Applications
- Analyzing PTT Beauty Board posts for sponsored content.
- Understanding brand competitors, products, and reviews.
- Predicting next season's best-selling products based on sentiment analysis.

## Future Work
- Enhancing accuracy through additional fine-tuning.
- Expanding analysis to other forums and product categories.

## Contributors
- Arden (Lead Developer)

