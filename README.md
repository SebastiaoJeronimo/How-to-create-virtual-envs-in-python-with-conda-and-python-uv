# How to Create Virtual Environments in Python with Conda and Python uv

This repository describes **how to create and manage Python virtual environments** using:
- **Anaconda (conda)**  
- **Python built-in virtualenv**
- **Python uv (on Linux / WSL)**  

It also includes examples of running **basic Python scripts** and **Jupyter Notebooks** in different environments (Windows and WSL).

---

## 🧩 Table of Contents
- [Anaconda (Conda)](#anaconda-conda)
- [Python Virtual Environment (venv)](#python-virtual-environment-venv)
- [Linux (WSL) with Python uv](#linux-wsl-with-python-uv)
- [Normal Run (Windows & WSL)](#normal-run-windows--wsl)
- [Links & References](#links--useful-referencesdocumentation)

---

## 🐍 Anaconda (Conda)

### 1. Install Conda
Download and install **Anaconda** or **Miniconda**:

- **Windows / macOS**:  
  👉 [https://www.anaconda.com/download](https://www.anaconda.com/download)

- **Linux (WSL)**:  
  ```bash
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh

### 2 Create a env

How to Create Virtual Environments in Python with Conda and Python environments 
In this repository we will have the matplotlib and the numpy library dependency so it has to be installed in the conda environment.  
If the libraries are not installed in the conda environment you will get an error like this when you run the matplotlib_test.py script:  

```cmd
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 6
      1 """
      2 matplotlib_test.py
      3 A simple script to verify matplotlib plotting works.
      4 """
----> 6 import numpy as np
      7 import matplotlib.pyplot as plt
      9 # Generate data
```      

ModuleNotFoundError: No module named 'numpy'

#### 2.1 Create a new Conda environment 

For Bash / Linux / macOS / WSL  

```bash
conda create -n matplotlib_env python=3.11
```   
-n matplotlib_env names the env matplotlib_env.  
python=3.11 installs Python 3.11 into that env.  
Confirm by typing y when conda asks to proceed.  

For Windows Command Prompt  

```cmd
conda create -n matplotlib_env python=3.11
```
Same as above , but if you get a error message please try.  

```cmd
# initialize conda for PowerShell (run once)
conda init powershell
# then close and re-open PowerShell (or run the new profile)
```  

##### 2.2 Activate the Conda environment

For Bash / Linux / macOS / WSL / Windows PowerShell  
```bash
conda activate matplotlib_env
```  

```cmd
conda info --envs
```
The active environment has a * next to it.  

##### 2.3 Install required libraries
```bash
conda install numpy matplotlib 
```
If you are running jupyter notebooks in this environment, you may also want to install jupyter:  
```bash
conda install notebook
```  

You can also install other libraries as needed using conda install or pip install.  
```bash
pip install numpy matplotlib jupyter
```
Install it inside your activated conda environment.  

##### 2.4 Deactivate the Conda environment
To deactivate the conda environment and return to the base environment, run:
```bash
conda deactivate
```
#### 2.5 Remove the Conda environment
To remove the conda environment when you no longer need it, run:
```bash
conda remove -n matplotlib_env --all
```   

To check the list of existing conda environments, run:
```bash
conda env list
```
#### 2.6 How to share your conda environment
To share your conda environment with others, you can export it to a YAML file:
```bash
conda env export -n matplotlib_env > environment.yml
```

#### 2.7 How to create a conda environment from a YAML file
To create a conda environment from a YAML file, use the following command:
```bash
conda env create -f environment.yml
```

# TODO FINISH THE OTHER CHAPTERS SPECIALLY THE PYTHON UV ONE 
# TODO ALSO ADD A CHAPTER WITH DOCKER USAGE IF POSSIBLE