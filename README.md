# EcoPackAI – AI-Powered Sustainable Packaging Recommendation System

EcoPackAI is an AI-powered sustainable packaging recommendation system that helps businesses choose the best packaging material based on **product requirements**, **material durability**, **cost efficiency**, and **environmental impact (CO₂)**.  
The project is built with a structured **PostgreSQL database**, proper constraints for data integrity, and a modular codebase ready for future AI/ML integration.

---

## 🎯 Project Objectives
- Store eco-friendly packaging materials and product requirements in a structured database
- Validate and clean data for better consistency
- Engineer sustainability metrics for ranking and recommendation
- Build a scalable foundation for ML-based predictions (cost & CO₂)
- Support sustainable decision-making for greener supply chains

---

## 🧱 System Architecture (High-Level)
1. Raw Data (CSV)
2. PostgreSQL Database (materials + products)
3. Data Validation (constraints + checks)
4. Feature Engineering (sustainability metrics)
5. Recommendation Logic (ranking)
6. Future Scope: ML Models + Flask API + Dashboard + Deployment

---

## 🗄️ Database Design (PostgreSQL)

### ✅ Tables
- **materials**  
  Stores packaging material attributes:
  - strength_mpa, weight_capacity
  - co2_emission_kg_per_kg
  - biodegradability_score
  - recyclability_pct
  - cost_inr_per_kg

- **products**  
  Stores product attributes:
  - product_name, category
  - product_weight_g, product_volume_cm3
  - fragility_level, moisture_sensitivity, temperature_sensitivity
  - shelf_life_days
  - current_packaging_material (linked to materials)

### ✅ Integrity Constraints Used
- `PRIMARY KEY`
- `UNIQUE`
- `NOT NULL`
- `CHECK` constraints
- `FOREIGN KEY` relationship (products → materials)

---

## 📁 Project Structure
```bash
EcoPackAI/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── screenshots/
│
├── sql/
│   └── EcoPackAI_Database.sql
│
├── src/
│
├── venv/
│
└── README.md
🚦 Current Project Status

✅ PostgreSQL database schema created

✅ Tables created (materials, products) with constraints

✅ Sample data inserted into database

✅ Row count & sample queries verified

✅ SQL file added to GitHub repository

🔜 Data cleaning & feature engineering (in progress)

🔜 ML model training (RandomForest/XGBoost)

🔜 Flask API integration

🔜 Frontend UI development

🔜 BI Dashboard + Sustainability Reports

🔜 Deployment & Documentation

🛠️ Tech Stack

Python

PostgreSQL

Pandas / NumPy (future)

Scikit-learn / XGBoost (future)

psycopg2 (database connectivity)

VS Code

Git & GitHub
