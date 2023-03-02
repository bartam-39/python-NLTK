# Python NLTK Notebook

This notebook uses machine learning algorithms

## Setup

- Install [Anaconda](https://www.anaconda.com/)
- Set the channel priority to strict to avoid issues with the environment creation taking forever.
  - `conda config --set channel_priority strict`
- Run the following commands (in either the terminal or an Anaconda Prompt):
  - `conda env create -f python-nltk.yml`
  - `conda activate python-nltk`
  - `conda install python=3`
- In VS Code, open the [Titanic.ipynb](Titanic.ipynb) file and connect to the golden_scenario_env kernel

You need to setup the environment as an `ipykernel` to use it from the Jupyter notebook. To do it run inside of the conda activated environment:

`python -m ipykernel install --user --name golden_scenario_env --display-name "Golden Scenario Env"`

Also if you want to support PDF export from jupyter you need to setup LaTeX:

`sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic`
