[![DOI](https://zenodo.org/badge/1168122092.svg)](https://doi.org/10.5281/zenodo.18974390)

# PhD-Oceanography
Code and datasets for reproducing the analysis and figures presented in my PhD thesis.

# Data Processing Workflow: Barros et al. (2026)

This repository contains the numerical workflow used to process and analyze ADCP and MicroCTD (MCTD) data as presented in **Barros et al. (2026)**.

## Getting Started

### Local Path Configuration

To adapt these notebooks to your local environment, please update the root directory path in the initial cells of each notebook. The original structure used during development was:
`deboragadelha/Jupyter/barros_et_al_2026/Notebooks`

### Prerequisites

These notebooks were developed in Python. You can install libraries as needed if you encounter an ImportError. The core requirements typically include:

* numpy,  matplotlib, cmocean, time, datetime, scipy, os, rasterio and pickle.

---

## Processing Steps

The notebooks should be executed in the following order:

### 1. Preprocessing Phase

* **STEP1_MCTD_Preprocessing.ipynb**
* Purpose: Opens raw MicroCTD data and performs the initial preprocessing required before synchronization with ADCP data.


* **STEP2_ADCP_Preprocessing.ipynb**
* Purpose: Opens raw ADCP data and performs the second step of preprocessing.


* **STEP3_DRIFT_sinc_MCTD+ADCP.ipynb**
* Purpose: Synchronizes MCTD and ADCP data to create a unified dataset for analysis.



### 2. Analysis & Calculation Phase

* **STEP4_Calc_Froude.ipynb**
* Purpose: Calculates the Internal Froude Number (requires Steps 1, 2, and 3).


* **STEP5_Calc_Transect_areas.ipynb**
* Purpose: Calculates transect areas along the thalweg of the channel (requires Steps 1, 2, and 3).



### 3. Visualization Phase

* **STEP6_PlotingFigures.ipynb**
* Purpose: A dedicated environment to handle processed data carefully (without affecting original result notebooks) and experiment with different color palettes and graphical layouts for the paper's figures.



---

## Data Access

* **Input Data:** The primary extra input files required for the notebooks are available in this repository.
* **MCTD & ADCP Data:** Due to the large file sizes, the raw MicroCTD and ADCP datasets are not hosted here. To request access to these data for reproduction purposes, please contact: **debor@furg.br**.

---

## Citation & Licensing

If you use these notebooks, the methodology, or the results in your research, please provide attribution by citing:

> **Barros, D.: Codebase for Barros et al. 2026 (v1.0.0), Zenodo [code], https://zenodo.org/records/18974391, 2026.**



This code is provided under the **MIT License**.

---

**Conseguiu visualizar agora?** Se precisar que eu mude qualquer termo ou adicione mais algum passo, é só falar!
