Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://www.astronomer.io/docs/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.
![Screenshot 2025-03-26 124344](https://github.com/user-attachments/assets/109e554c-d9ab-45f2-afe8-327b63c3f0d4)

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.
![Screenshot 2025-03-26 125404](https://github.com/user-attachments/assets/8b4249e0-f0dc-40f1-aed6-5f5b0331f2ff)

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.
![Screenshot 2025-03-26 124323](https://github.com/user-attachments/assets/a2464d2e-b826-4c03-8565-3b89092e65ac)


![Screenshot 2025-03-26 124829](https://github.com/user-attachments/assets/e2fd63ba-1e50-42b0-ac68-149452d6bb2c)
![Screenshot 2025-03-26 125107](https://github.com/user-attachments/assets/53f9fdf7-ffdf-4998-be6a-4920510c40e5)
![Screenshot 2025-03-26 125147](https://github.com/user-attachments/assets/ebbc1056-649f-470a-ab81-d41d3928ae7f)
![Screenshot 2025-03-26 125221](https://github.com/user-attachments/assets/eb7138ef-57b8-456b-bf32-bc19b57f0b54)
![Screenshot 2025-03-26 125434](https://github.com/user-attachments/assets/e13c7d75-97e2-46d9-b4df-ea4351d6d0d8)


![Screenshot 2025-03-26 132352](https://github.com/user-attachments/assets/f829b959-1a87-4cc4-b459-77433c4962cc)
![Screenshot 2025-03-26 132644](https://github.com/user-attachments/assets/a1ed6879-d90a-4cd7-b897-69bef299d803)
![Screenshot 2025-03-26 132614](https://github.com/user-attachments/assets/cdec04cf-6e92-4702-9f1e-d500a7bae98d)
![Screenshot 2025-03-26 132614](https://github.com/user-attachments/assets/5797465f-1d1d-44d9-9e3a-bbdaccc18700)
![Screenshot 2025-03-26 132644](https://github.com/user-attachments/assets/39eaa845-7b87-4a96-affa-bcc8882bbb3b)
![Screenshot 2025-03-26 132711](https://github.com/user-attachments/assets/b770fe1e-9183-4295-88ef-03fd9dad092d)
![Screenshot 2025-03-26 132726](https://github.com/user-attachments/assets/522aad55-ad77-41b2-a875-b9dbb155a213)
