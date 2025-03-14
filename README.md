# DSCI550 Assignment 1 - Analysis of the Haunted Places Dataset

**Repository for DSCI 550 Group 2**  
**Collaborators:** Eleanor Bi, Maggie Chang, Jessica Deng, Tarun Jagadish, Aaron Kuo, Hengxiao Zhu

---

## Project Overview

This project is part of the USC DSCI 550 course and focuses on analyzing the **Haunted Places dataset**. We integrate **Apache Tika** and **Tika-Similarity** to explore patterns and characteristics of haunted locations using various data analysis techniques.

---

## Key Objectives

- **Data Transformation**: Convert the dataset from CSV to TSV format.
- **Feature Engineering**: Expand the dataset with additional features such as:
  - Audio Evidence (e.g., mentions of noises, sounds)
  - Visual Evidence (e.g., reports of images, videos)
  - Time of Occurrence (e.g., morning, evening, dusk)
  - Event Type (e.g., murder, unexplained phenomena)
  - Apparition Type (e.g., ghost, orb, UFO)
- **Data Integration**: Merge the Haunted Places dataset with at least three external datasets of different MIME types.
- **Data Similarity Analysis**: Use Tika-Similarity to compute and compare:
  - Jaccard Similarity
  - Cosine Distance
  - Edit Distance
- **Clustering and Visualization**: Identify patterns in haunted places based on their descriptions, locations, and features.

---

## Project Structure

- `data/`                     — Contains the datasets used in the project
- `source_code/`              — Source code for data processing and analysis
- `README.md`                  — Project documentation
- `DSCI550_HW_BIGDATA_HAUNTED.pdf` — Assignment details
- `.gitignore`                 — Git ignore file

---

## Datasets Used

- **Primary Dataset: Haunted Places**
  - **Source**: Kaggle - Haunted Places Dataset
  - Contains 21,983 rows and 10 columns, detailing haunted locations across the United States.

---

## Data Similarity & Clustering

We used **Apache Tika-Similarity** to compare haunted locations based on the following metrics:
- Jaccard Similarity
- Cosine Distance
- Edit Distance

---

## Tasks Breakdown

- **Jessica & Hengxiao**: Convert CSV to TSV and expand the dataset with additional features.
- **Aaron & Eleanor**: Identify 3 additional datasets.
- **Tarun & Maggie**: Use Tika-Similarity to convert TSV to JSON and compare similarity metrics.

---

## Conclusion

This project provides insights into the patterns of haunted places by integrating multiple datasets and using **Apache Tika-Similarity** for data clustering. The analysis helps uncover trends in supernatural sightings based on geographic, temporal, and event-related factors.
