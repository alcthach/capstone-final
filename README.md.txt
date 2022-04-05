Hi!

This is the readme file for Alex Thach's Capstone Project submitted as part of BrainStation's Data Science Diploma Program.

The goal of this project was to predict Spotify skip prediction using machine learning. Logistic regression and Random Forest classifiers were trained with various engineered features in an attempt to solve this problem.

Below is a directory map for the project:

AlexThach-Capstone-Final-RAW-DATA
│   AlexThach-capstone-technical-report.pdf
│   capstone.yml
│   README.md.txt
│
├───assets
│       aicrowd_logo_sm.png
│       brainstation_logo.png
│       edgar-moran-tcTouY4xMoA-unsplash-cassette1.jpg
│       effy-VHf4jqrUu7g-unsplash_lg.jpg
│       effy-VHf4jqrUu7g-unsplash_sm.jpg
│       Spotify_Logo_CMYK_Green.png
│
├───data
│   ├───processed
│   │       .gitkeep
│   │
│   └───raw
│       │   .gitkeep
│       │   7dcfad42-65c6-4481-abe8-5a44339fa305_Dataset Description.pdf
│       │
│       ├───track_features
│       │       ._tf_mini.csv
│       │       tf_mini.csv
│       │
│       └───training_set
│               ._log_mini.csv
│               log_mini.csv
│
├───notebooks
│   │   01-alexthach-introduction.ipynb
│   │   02-alexthach-eda-univariate.ipynb
│   │   03-alexthach-eda-multivariate.ipynb
│   │   04-alexthach-feature-engineering-baseline-modelling.ipynb
│   │   05-alexthach-feature-engineering-modelling-cumulative-average.ipynb
│   │   06-alexthach-feature-engineering-modelling-ewma.ipynb
│   │   07-alexthach-feature-engineering-model-evaluation-conclusion.ipynb
│   │   helper_functions.py
│   │   skip2_emwa.png
│   │
│   ├───.ipynb_checkpoints
│   │       01-alexthach-introduction-checkpoint.ipynb
│   │       02-alexthach-eda-univariate-checkpoint.ipynb
│   │       03-alexthach-eda-multivariate-checkpoint.ipynb
│   │       04-alexthach-feature-engineering-baseline-modelling-checkpoint.ipynb
│   │       05-alexthach-feature-engineering-modelling-cumulative-average-checkpoint.ipynb
│   │       06-alexthach-feature-engineering-modelling-ewma-checkpoint.ipynb
│   │       07-alexthach-feature-engineering-model-evaluation-conclusion-checkpoint.ipynb
│   │
│   └───__pycache__
│           helper_functions.cpython-39.pyc
│
└───scripts
        at-setup.py

- You will find the notebooks in sequential order for viewing in /notebooks
- The raw data for this project is found in /data/raw
- You will also a find a yml file called capstone.yml to create the conda environment required to run the project
- Processed data will be written to /data/processed when the appropriate code cells have been executed 
- If for some reason the processed data cannot be read in, please download the data from: https://www.dropbox.com/s/6wn1u9zve3x6kin/processed.zip?dl=0
- And extract the contents to /data/processed
- The notebooks execute a set-up script called at-setup.py found in /scripts, which handles all the importing, loading of raw data, and other settings
- You will also find some assets that were used in the notebooks and slide deck in /assets

If you have any issues running this project or have questions about my work please reach out to me at alcthach@gmail.com

Enjoy!