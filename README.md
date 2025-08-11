 Insight Engine: An Interactive Supply Chain Data Explore

 An interactive web application built with Python (Flask) and PostgreSQL, all containerized with Docker. This tool allows users to perform complex analytical queries on a supply chain database through a user-friendly interface.

 ![Project Demo GIF](assets/demo.gif)



 ## ✨ Features

- **Interactive Data Explorer:** View raw data from any table (`suppliers`, `parts`, `customers`, etc.) directly in the UI.
- **Customer Analysis by Color:** Filter and find customers who have placed orders involving parts of a specific color.
- **Single-Supplier Part Analysis:** List all orders for parts that are supplied by only one exclusive vendor.
- **Order Leader Analysis:** Identify the top customer by total quantity ordered for each individual part, using advanced SQL Window Functions.
- **Above-Average Price Analysis:** Find suppliers who are pricing a part higher than the average market price for that part.
- **Visual Documentation:** Each analysis page includes a flowchart explaining the logic of the underlying SQL query.


## 🛠️ Technologies Used
![Python](https://img.shields.io/badge/python-3.9-blue.svg?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)



## 🚀 How to Run Locally

To run this project on your local machine, please ensure you have **Docker Desktop** installed and running.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/OzdemirMirza/Supply-Chain-Data-Explorer.git
    cd Supply-Chain-Data-Explorer
    ```

2.  **Run the application using Docker Compose:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the application:**
    Open your web browser and navigate to `http://localhost:5005`





 ## 🎯 Project Purpose & Learning Journey

This project serves as a practical milestone in my "baby steps" approach to mastering Data Engineering. The primary goal was to demonstrate proficiency in designing and building a data-intensive application from the ground up.

This application showcases the ability to:
- Design a relational database schema in PostgreSQL.
- Author complex, analytical SQL queries to derive business insights.
- Develop a data-driven, interactive web application using Python and Flask.
- Containerize a multi-service application (web server + database) with Docker and Docker Compose for portability and reproducibility.