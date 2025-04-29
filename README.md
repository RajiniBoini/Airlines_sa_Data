# ✈️ JetBlue Airline Sentiment Intelligence – ETL Data Pipeline

This project presents an end-to-end automated ETL pipeline for JetBlue Airlines, designed to capture, process, analyze, and visualize customer sentiment data from X (formerly Twitter) in near real-time.

---

## 📌 Project Overview

**Goal:**  
Enable JetBlue to understand customer feedback by analyzing public tweets and turning raw data into actionable insights.

**Solution Highlights:**
- Real-time tweet ingestion using the X API.
- Automated orchestration with GitHub Actions.
- Scalable data storage using Amazon S3.
- Metadata cataloging and ETL with AWS Glue.
- Sentiment classification using a trained ML model.
- Interactive dashboards powered by Amazon Athena and Power BI.

---

## 🛠️ Technologies Used

- **X (Twitter) API** – Live tweet extraction  
- **GitHub Actions** – Automation and scheduling  
- **Amazon S3** – Centralized cloud storage  
- **AWS Glue** – Schema inference and ETL  
- **Custom ML Model** – Sentiment classification  
- **Amazon Athena** – Serverless querying  
- **Power BI** – Business dashboarding

---

## 🔁 Pipeline Architecture


The architecture ensures:
- Seamless automation from data ingestion to reporting
- Scalable, low-maintenance infrastructure
- Real-time insights for proactive decision-making

---

## 📂 Project Structure

```bash
Airline_Sentiment_Pipeline/
├── github-workflows/
│   └── tweet_ingestion.yml           # GitHub Action for automated ingestion
├── scripts/
│   ├── sentiment_model.py            # Sentiment classification model
│   ├── glue_job_script.py            # Data cleaning and transformation
├── dashboards/
│   └── powerbi_dashboard.pbix        # Power BI report (exported)
├── data/
│   └── sample_tweets.csv             # Sample dataset for testing
├── README.md
└── architecture_diagram.png          # Visual workflow of the pipeline
