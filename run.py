import sys
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(notebook_path, output_path):
    """Execute a Jupyter notebook and save the executed notebook."""
    # Check if the notebook file exists
    if not os.path.exists(notebook_path):
        print(f"Notebook not found: {notebook_path}")
        return

    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Create an ExecutePreprocessor
    ep = ExecutePreprocessor(timeout=-1, kernel_name='python3')

    # Execute the notebook
    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
    except Exception as e:
        print(f"Error executing the notebook {notebook_path}: {e}")
        return

    # Save the executed notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"Notebook executed and saved: {output_path}")


def main():
    # Define a list of notebooks to execute
    notebooks = [
        {"name": "dbpedia", "path": "notebooks/dbpedia_prompt.ipynb"},
        {"name": "nyt_locations", "path": "notebooks/nyt_locations_prompt.ipynb"},
        {"name": "nyt_topics", "path": "notebooks/nyt_topics_prompt.ipynb"},
        {"name": "yelp", "path": "notebooks/yelp_prompt.ipynb"},
    ]

    # Iterate through notebooks and execute each one
    for notebook in notebooks:
        notebook_name = notebook["name"]
        notebook_path = notebook["path"]
        output_path = f"executed_{notebook_name}.ipynb"

        print(f"Running notebook: {notebook_name}")
        run_notebook(notebook_path, output_path)

    print("All notebooks executed.")


if __name__ == "__main__":
    main()
