# Vantage Retail Data Engineering Pipeline

A professional end-to-end Data Engineering pipeline designed to orchestrate, clean, process retail transaction data, and visualize insights through an interactive analytics dashboard.

## 🛠️ Tech Stack & Tools
* **Orchestration:** Apache Airflow
* **Containerization:** Docker & Docker Compose
* **Language:** Python (Pandas / PySpark)
* **Data Visualization & BI:** Looker Studio (Google Data Studio)

## 🏗️ Architecture & Data Workflow
1. **Infrastructure:** Spin up Apache Airflow services using a multi-container Docker deployment (`docker-compose.yaml`).
2. **Data Ingestion:** Raw retail transaction logs are ingested into the local data directory.
3. **Data Transformation (DAGs):** Airflow schedules and monitors the ETL process via Python:
   * **Extract:** Load the latest raw retail transaction data.
   * **Transform:** Handle missing values, format dates correctly, and filter duplicates using Pandas.
   * **Load:** Export the clean, analytics-ready dataset into a final storage tier.
4. **Analytics & BI:** Connect the refined dataset to **Looker Studio** to build real-time interactive business dashboards (monitoring sales trends, customer behavior, and key retail KPIs).

## 📁 Repository Structure
* `dags/` - Contains Apache Airflow DAG definitions and data transformation scripts (`my_first_dag.py`).
* `docker-compose.yaml` - Docker infrastructure configuration for the Airflow environment.
* `.gitignore` - Safeguards the repository by ignoring large CSV data files, caches, and local logs.

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/Junaid2132/Vantage-Retail-Project.git](https://github.com/Junaid2132/Vantage-Retail-Project.git)