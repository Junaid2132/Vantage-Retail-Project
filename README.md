# Vantage Retail Data Engineering Pipeline

An enterprise-grade, end-to-end Data Engineering pipeline designed to automate retail transaction logs processing. This repository demonstrates clean production data workflows and containerized orchestration.

---

## 🏗️ Pipeline Flow Chart
```text
┌────────────────┐     ┌────────────────┐     ┌─────────────────────┐
│  Raw Data Logs │ ──> │ Docker Volumes │ ──> │ Airflow Orchestration│
└────────────────┘     └────────────────┘     └─────────────────────┘
                                                         │
                                                         ▼
┌────────────────┐     ┌────────────────┐     ┌─────────────────────┐
│ Looker Studio  │ <── │ Analytical CSV │ <── │ Python / Pandas ETL │
│  (BI Dashboard)│     │  (Clean Storage│     │ (Data Transformation)│
└────────────────┘     └────────────────┘     └─────────────────────┘


⚙️ How Data Moves in the Pipeline:


1. Infrastructure: Multi-container Docker Compose setup isolates Apache Airflow engines.

2. Data Ingestion: Monitors incoming pipeline staging for transaction sheets (raw_retail_data.csv).

3. ETL Task Chain: Python & Pandas automatically handle data cleaning under strict Airflow DAG task management.

4. BI Layer: Structured analytical outputs are fed straight into Looker Studio for corporate visual analytics.


## 🏗️ Pipeline Flow Chart
```text
┌────────────────┐     ┌────────────────┐     ┌─────────────────────┐
│  Raw Data Logs │ ──> │ Docker Volumes │ ──> │ Airflow Orchestration│
└────────────────┘     └────────────────┘     └─────────────────────┘
                                                         │
                                                         ▼
┌────────────────┐     ┌────────────────┐     ┌─────────────────────┐
│ Looker Studio  │ <── │ Analytical CSV │ <── │ Python / Pandas ETL │
│  (BI Dashboard)│     │  (Clean Storage│     │ (Data Transformation)│
└────────────────┘     └────────────────┘     └─────────────────────┘


⚙️ How Data Moves in the Pipeline:

1. Infrastructure:Multi-container Docker Compose setup isolates Apache Airflow engines.

2. Data Ingestion: Monitors incoming pipeline staging for transaction sheets (raw_retail_data.csv).

3. ETL Task Chain: Python & Pandas automatically handle data cleaning under strict Airflow DAG task management.

4. BI Layer: Structured analytical outputs are fed straight into Looker Studio for corporate visual analytics.


📊 Pipeline Task Matrix & Validation Metrics


Pipeline Stage / TaskCore Process AppliedEngineering ToolTarget Executionextract_raw_dataPath tracking, streaming validationsPython Core🟢 Successtransform_retailFixed dates, filled nulls, dropped duplicatesPandas Engine🟢 Successload_to_analyticsStandardized schema exportLocal Storage🟢 Success


📈 Core Metrics Captured:


Log Integrity: 100% data preservation during structural modifications.

Schema Uniformity: Raw string streams converted into query-optimized data formats.

Execution Logs: Airflow tasks strictly track runtime speed and dependency safety.


🛠️ Technology Stack


Orchestration: Apache Airflow

Containerization: Docker & Docker Compose

Data Processing: Python 3 & Pandas Engine

Business Intelligence (BI): Looker Studio (Google Data Studio)


📁 Repository Directory Setup


📁 dags/ - Core Data Engineering files.

📄 my_first_dag.py - Main DAG tracking schedules and operations.

📄 raw_retail_data.csv - Initial raw inputs.

📄 clean_retail_data.csv - Final analytical product.

📄 docker-compose.yaml - Multi-service system rules for Docker container environments.

📄 .gitignore - Safely protects cloud workspace by filtering out localized diagnostic tracks and runtime memory locks.


🚀 How to Launch Project Locally

1. Initialize
git clone [https://github.com/Junaid2132/Vantage-Retail-Project.git](https://github.com/Junaid2132/Vantage-Retail-Project.git)
cd Vantage-Retail-Project

2. Boot Cluster
docker-compose up -d

3. Monitor
Open UI Console: http://localhost:8080

Activate the retail pipeline DAG, and link final output views with Looker Studio panels.