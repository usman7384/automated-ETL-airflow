# **ETL Pipeline with Apache Airflow, Docker & DVC**  

🚀 A **scalable, automated ETL pipeline** using **Apache Airflow, Docker, and DVC** for data versioning and orchestration. This project extracts **news articles from BBC** (`https://www.bbc.com`), processes the data, and stores it in a **data warehouse**—ensuring **reproducibility, scalability, and monitoring**.  

## 📌 **Features**  
✅ **Containerized Deployment** – Uses Docker & Docker Compose for easy setup & scalability  
✅ **Data Versioning** – Tracks datasets with **DVC** and stores them in **Google Drive**  
✅ **Web Scraping** – Extracts news articles from **BBC** (`https://www.bbc.com`)  
✅ **Extract** – Pulls data from BBC using **BeautifulSoup / Scrapy**  
✅ **Transform** – Cleans, tokenizes, and extracts key information  
✅ **Load** – Stores processed data in a warehouse (PostgreSQL, BigQuery, Snowflake)  
✅ **Workflow Orchestration** – Uses Apache Airflow DAGs to manage dependencies  
✅ **Monitoring & Logging** – Tracks execution, logs errors, and enables alerts  

---

## 🏗️ **Tech Stack**  
- **Apache Airflow** 🌀 (Orchestration)  
- **Docker & Docker Compose** 🐳 (Containerization)  
- **DVC (Data Version Control)** 🔄 (Dataset Management)  
- **Google Drive** ☁️ (Remote Storage)  
- **BeautifulSoup / Scrapy** 📰 (Web Scraping)  
- **Python** 🐍 (Transformation Logic)  

---

## 🚀 **Getting Started**  

### **1️⃣ Clone the Repository**  
```bash
https://github.com/usman7384/automated-ETL-airflow.git
cd automated-ETL-airflow
```

### **2️⃣ Set Up Environment Variables**  
Rename `.env.example` to `.env` and update configurations if needed.

```bash
cp .env.example .env
```

### **3️⃣ Set Up DVC with Google Drive**  
First, install **DVC** if you haven’t already:  
```bash
pip install dvc
```

#### **Initialize DVC**  
```bash
dvc init
```

#### **Configure Google Drive as Remote Storage**  
```bash
dvc remote add -d gdrive_remote gdrive://your-drive-folder-id
dvc remote modify gdrive_remote gdrive_use_service_account true
```
To authenticate with Google Drive, follow the [DVC Google Drive Guide](https://dvc.org/doc/user-guide/setup-google-drive-remote).  

#### **Pull Data from Remote Storage**  
```bash
dvc pull
```

#### **Track New Data Files**  
```bash
dvc add data/bbc_articles.csv
git add data/bbc_articles.csv.dvc .gitignore
git commit -m "Added BBC scraped articles"
git push origin main
dvc push
```

---

### **4️⃣ Start Airflow Services**  
Run the following command to start Apache Airflow with Docker Compose:  
```bash
docker-compose up -d
```
This will start all necessary containers, including the **Airflow scheduler, web server, and PostgreSQL database**.

### **5️⃣ Access the Airflow UI**  
Once the services are running, open your browser and go to:  
📌 **Airflow UI:** [`http://localhost:8080`](http://localhost:8080)  
📌 **Username:** `airflow` | **Password:** `airflow` (default)  

### **6️⃣ Deploy Your DAGs**  
Place your DAG files inside the `dags/` folder. Airflow will automatically detect and execute them based on the defined schedule.

### **7️⃣ Monitor Logs & Status**  
Check logs for debugging:  
```bash
docker-compose logs -f
```
List running containers:  
```bash
docker ps
```

### **8️⃣ Stop Services**  
To stop all running containers:  
```bash
docker-compose down
```
