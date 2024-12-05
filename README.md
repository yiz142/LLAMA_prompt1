# LLAMA_prompt1 Project

This project evaluates different prompting methods and models on various datasets using the LLAMA models.
This project explores the use of LLAMA models from SambaNova's prompting API for classification tasks across various datasets from the XClass repository. We aim to evaluate the performance of different prompting methods using 1B, 3B, and 8B LLAMA models, comparing accuracy under multiple prompt strategies.

## Directory Structure

- `config/`: Configuration files for different datasets.
- `data/`: Contains rdata
- `notebooks/`: Jupyter notebooks
- `src/`: Source code modules.
- `results/`: Output results
- `run.py`: Main script to execute the evaluations.
- `requirements.txt`: Python dependencies.

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/LLAMA_prompt1.git
   cd LLAMA_prompt1

2. **Create a virtual environment**:

    ```bash
    conda create -n myenv python=3.9 
    conda activate myenv

    bash
    pip install -r requirements.txt
    Set up environment variables:

    Create a .env file in the root directory.
    Add your SAMBANOVA_API_KEY:
    SAMBANOVA_API_KEY=your_api_key_here


## Running the Project

To run the evaluation, use the `run.py` script