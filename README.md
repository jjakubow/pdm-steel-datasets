# Data Visualization and Validation for "TCM: Benchmark Datasets for Predictive Maintenance in Steel Manufacturing"

This repository contains the source code for visualization, technical validation, and benchmarking of the dataset "TCM: Benchmark Datasets for Predictive Maintenance in Steel Manufacturing" available on [Zenodo](https://zenodo.org/records/11469702).

## Repository Contents

- **Dataset_Technical_Validation.ipynb**  
  Jupyter notebook presenting the technical validation of the dataset. Primarily contains plots and analyses demonstrating data quality and consistency.

- **Evaluation.ipynb**  
  Benchmarking experiments evaluating batch learning anomaly detection algorithms on the dataset. Includes performance metrics and comparative visualizations.

- **Evaluation Online.ipynb**  
  Benchmarking experiments evaluating online learning anomaly detection algorithms. Designed to assess models that learn incrementally from streaming data.

- **ML_sample.py**  
  Minimal working example of training an anomaly detection model on the dataset. This script provides a quick start for users interested in applying machine learning methods.

## Dataset Access

The original dataset files used in these analyses are stored in Zenodo and can be accessed via the following link:

* `URL`:  https://zenodo.org/records/11469702  
* `DOI`: https://doi.org/10.5281/zenodo.11469701

Please cite the dataset and this repository in any derivative work.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Download the dataset from Zenodo and place the files in the appropriate data directory (details in notebooks).

3. Open the Jupyter notebooks to explore the technical validation and benchmarking results.

4. Use `ML_sample.py` as a starting point for training anomaly detection models.

## Citation

If you use this dataset or the associated code, please cite:

```bibtex
@misc{https://doi.org/10.5281/zenodo.11469701,
  doi = {10.5281/ZENODO.11469701},
  url = {https://zenodo.org/doi/10.5281/zenodo.11469701},
  author = {Jakubowski,  Jakub and Bobek,  Szymon and Nalepa,  Grzegorz J.},
  keywords = {anomaly detection,  predictive maitenance,  steel industry,  machine learning,  industry 4.0,  industry 5.0,  Artificial intelligence},
  title = {TCM: Benchmark Datasets for Predictive Maintenance in Steel Manufacturing},
  publisher = {Zenodo},
  year = {2024},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

## Requirements

- Python 3.x  
- Jupyter Notebook  
- Required Python libraries (listed in `requirements.txt` if available, e.g., numpy, matplotlib, scikit-learn, pandas)
