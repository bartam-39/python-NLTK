# Python Natural Language Processing with NLTK

This repository use NLTK to implement some of the most popular NLP algorithms.
Additionally, we run the application inside a Docker container. This is not mandatory, you can use python venv instead.
If you like to run the code in a container you need the following:
- docker installed in your local machine,
- vscode extension ms-vscode-remote.remote-containers installed in your vscode, to boot the dev containers.

Otherwise, you simply need to create a venv and then pip install the requirements.txt file.

## Installing NLTK Data

After installing the NLTK package, please do install the necessary datasets/models for specific functions to work.

If you’re unsure of which datasets/models you’ll need, you can install the “popular” subset of NLTK data, on the command line type python -m nltk.downloader popular, or in the Python interpreter import nltk; nltk.download('popular')

For details, see https://www.nltk.org/data.html
