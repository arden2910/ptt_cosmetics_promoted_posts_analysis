# PTT Cosmetics Promoted Posts Analysis

## Project Description

This project aims to analyze promoted posts (advertorials) on the PTT Cosmetics board. Using BERT for natural language processing, the project includes scripts for both training the model and making predictions.

## Directory Structure

```
ptt_cosmetics_promoted_posts_analysis/
├── data/
│   └── [Your data files will be stored here]
├── bert_predict.ipynb
├── bert_train.ipynb
└── README.md
```

### 1. data/
This directory contains all the data files necessary for the project. Ensure that your dataset is placed here before running the notebooks.

### 2. bert_predict.ipynb
This Jupyter notebook contains the code for using a pre-trained BERT model to predict whether a post is a promoted post (advertorial).

### 3. bert_train.ipynb
This Jupyter notebook contains the code for training a BERT model on your dataset. It includes steps for data preprocessing, model training, and evaluation.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/ptt_cosmetics_promoted_posts_analysis.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd ptt_cosmetics_promoted_posts_analysis
    ```

3. **Install the necessary dependencies**:
    Make sure you have Python and pip installed. Then run:
    ```sh
    pip install -r requirements.txt
    ```

4. **Place your data files in the `data/` directory**.

5. **Run the notebooks**:
    - Open `bert_train.ipynb` to train the model.
    - Open `bert_predict.ipynb` to make predictions using the trained model.

## Dependencies

- Python 3.x
- Jupyter Notebook
- Transformers (Hugging Face)
- PyTorch
- Pandas
- NumPy
- Other dependencies as listed in `requirements.txt`

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
