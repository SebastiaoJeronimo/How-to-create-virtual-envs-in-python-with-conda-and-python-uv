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

