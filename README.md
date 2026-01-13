📦 EcoPackAI: AI-Powered Sustainable Packaging Recommendation System
📘 Introduction

EcoPackAI is an AI-powered sustainable packaging recommendation system that helps businesses choose the best packaging material based on product requirements, material durability, cost efficiency, and environmental impact (CO₂).
It reduces dependency on non-biodegradable packaging by using a structured database + feature engineering pipeline to support eco-friendly decision-making.

🎯 Project Objectives

Build a structured and validated PostgreSQL database

Store eco-friendly material & product attribute data

Perform data cleaning and ensure integrity

Engineer sustainability-related features:

CO₂ Impact Index

Cost Efficiency Index

Material Suitability Score

Create a foundation for ML-based material ranking & recommendation

Make the project scalable for future dashboard + API deployment

🧱 System Architecture Overview

EcoPackAI follows a modular pipeline:

Raw Data Collection (CSV datasets)

Database Storage (CSV → PostgreSQL)

Schema Validation & Data Integrity

Data Cleaning

Feature Engineering

Recommendation Scoring (Rule/Index-based)

(Future) ML Model Integration + BI Dashboard

🗃️ Database Design

Database: PostgreSQL

Database Name: ecopackai

✅ Key Design Principles

Clean relational schema

Strong constraints (NOT NULL, CHECK, UNIQUE)

Referential integrity via Foreign Keys

Ready for future AI model + dashboard integration

📋 Table Schema Design
🔹 materials Table

Stores physical, environmental, and economic packaging material attributes.

Primary Key: material_id

Key Columns:

material_type

strength_mpa

weight_capacity

co2_emission_kg_per_kg

biodegradability_score

recyclability_pct

cost_inr_per_kg

material_category

✅ Data Integrity:

Numeric range validation using CHECK

No missing critical values using NOT NULL

Unique material types using UNIQUE

🔹 products Table

Stores product-specific requirements that help match suitable packaging.

Primary Key: product_id
Foreign Key: current_packaging_material → materials.material_type

Key Columns:

product_name

product_category

product_weight_g

product_volume_cm3

fragility_level (Low/Medium/High)

temperature_sensitivity (Low/Medium/High)

moisture_sensitivity (Low/Medium/High)

shelf_life_days

packaging_format

✅ Ensures product-material linking for recommendation logic.

🔄 Data Engineering Process
📂 Data Sources

Sustainable packaging material dataset (CSV)

Product attribute dataset (CSV)

📈 Data Flow

CSV files stored in /data/raw

Imported into PostgreSQL database tables

Exported and loaded into Pandas for processing

Cleaned and engineered datasets saved into /data/processed

✅ Data Validation

Validation checks performed before feature engineering:

Dataset shape verification (rows/columns)

Missing value detection

Duplicate record checks

Range validation for CO₂, cost, strength

Referential validation between products & materials

✅ Result: Dataset marked ML-ready

🧹 Data Cleaning

Cleaning was applied to maintain real-world data quality:

Cleaning Steps

Handling missing values (NULL checks)

Duplicate removal

String normalization (trim/case)

Data type fixing (numeric, categorical)

Range checks (CO₂, cost must be valid)

🛠️ Feature Engineering

EcoPackAI generates sustainability and efficiency-based engineered features:

✅ Key Engineered Features

Strength Level

Low / Medium / High based on strength (MPa)

Normalized Metrics

CO₂ normalization

Cost normalization

Strength normalization

Sustainability Score

A composite score combining CO₂, recyclability, and cost

Used for ranking materials in recommendation

📁 Project Folder Structure
EcoPackAI/
│
├── data/
│   ├── raw/
│   │   ├── materials.csv
│   │   └── products.csv
│   │
│   └── processed/
│       ├── materials_cleaned.csv
│       ├── products_cleaned.csv
│       └── materials_feature_engineered.csv
│
├── notebooks/
│   ├── 01_data_validation.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_summary_validation.ipynb
│
├── sql/
│   └── EcoPackAI_Database.sql
│
├── screenshots/
│
├── src/
│   ├── db_connect.py
│   └── pipelines/
│
├── requirements.txt
├── .gitignore
└── README.md


🚦 Current Project Status

✅ PostgreSQL database schema created

✅ Data inserted into tables

✅ Row count + sample queries verified

✅ Python connection using psycopg2

✅ Data loaded into Pandas

✅ Data cleaning completed

✅ Feature engineering completed

🔜 ML model training (RandomForest/XGBoost)

🔜 Flask API integration

🔜 Frontend UI + Dashboard

🔜 Deployment & Documentation

🛠️ Tech Stack

Python

Pandas / NumPy

Scikit-learn

PostgreSQL

psycopg2

VS Code

Git & GitHub

## 🚦 Current Project Status

* ✅ PostgreSQL database schema created
* ✅ Tables created (`materials`, `products`) with constraints
* ✅ Sample data inserted into database
* ✅ SQL file added to GitHub repository
* 🔜 Data cleaning & feature engineering (in progress)
* 🔜 ML model training (RandomForest/XGBoost)
* 🔜 Flask API integration
* 🔜 Frontend UI development
* 🔜 BI Dashboard + Sustainability Reports
* 🔜 Deployment & Documentation

🔮 Future Scope

Train ML models for cost + CO₂ prediction

Rank materials using AI-based scoring

Build Flask REST API for recommendations

Integrate BI dashboard (Power BI / Tableau)

Deploy full-stack EcoPackAI on cloud (Render/Heroku)