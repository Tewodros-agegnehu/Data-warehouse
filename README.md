# Data Warehouse for Ethiopian Medical Business Data

## Overview
This project involves building a data warehouse to store and analyze Ethiopian medical business data scraped from Telegram channels. The data warehouse will support efficient querying and reporting, enabling businesses to derive actionable insights. The project also integrates object detection using YOLO to enhance data analysis.

## Business Need
As a data engineer at Kara Solutions, you are tasked with developing a robust and scalable data warehouse capable of handling scraped data from Telegram channels. This includes implementing ETL/ELT frameworks, data cleaning, transformation, and object detection to enrich the collected data.

## Key Features
- **Data Scraping & Collection**: Extracting structured and unstructured data from Telegram channels.
- **Data Cleaning & Transformation**: Standardizing, validating, and transforming raw data using DBT.
- **Object Detection with YOLO**: Enhancing image data with object detection.
- **Data Warehouse Implementation**: Designing and integrating a scalable data warehouse.
- **Data Exposure via FastAPI**: Providing a RESTful API for querying the collected data.

## Data and Features
This data warehouse aggregates Ethiopian medical business data, enabling trend analysis, pattern recognition, and informed decision-making.

## Technology Stack
- **Programming Languages**: Python
- **Data Processing**: Telethon, Pandas, DBT
- **Database Management**: SQLAlchemy, PostgreSQL
- **Machine Learning**: YOLO (PyTorch/TensorFlow), OpenCV
- **API Development**: FastAPI, Uvicorn

## Implementation Steps
### 1. Data Scraping and Collection
- Scrape data from Telegram channels using the `telethon` Python package.
- Store raw scraped data temporarily in local databases or files.
- Implement logging to monitor the scraping process.

### 2. Data Cleaning and Transformation
- Remove duplicates, handle missing values, and standardize formats.
- Store cleaned data in a database.
- Use DBT for transformations:
  ```bash
  pip install dbt
  dbt init my_project
  dbt run
  ```

### 3. Object Detection Using YOLO
- Install YOLO and dependencies:
  ```bash
  git clone https://github.com/ultralytics/yolov5.git
  cd yolov5
  pip install -r requirements.txt
  ```
- Use pre-trained YOLO models to detect objects in images.
- Extract relevant data and store detection results in a database.

### 4. Exposing Data via FastAPI
- Install FastAPI and Uvicorn:
  ```bash
  pip install fastapi uvicorn
  ```
- Implement a REST API with FastAPI to expose the collected data.
- Define database models, schemas, and CRUD operations using SQLAlchemy.

## Submission & Deliverables
- Functional data warehouse with integrated ETL/ELT processes.
- Object detection pipeline using YOLO.
- FastAPI endpoints for querying the processed data.

## References
- [Telegram API](https://core.telegram.org/api)
- [YOLOv5 Repository](https://github.com/ultralytics/yolov5)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [DBT Documentation](https://docs.getdbt.com/)

## Contributors
- **Tewodros Agegnehu**
- Kara Solutions Team

## License
This project is licensed under the MIT License.

