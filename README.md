# GovTech Assessment

This repository contains the code and configurations for the GovTech Assessment project. The project involves processing restaurant data, extracting restaurant events, and determining rating thresholds based on aggregate ratings.

## Table of Contents
- Project Overview
- Assumptions
- Requirements
- Setup and Installation
  - Running the Application Locally
    - Method 1: Using Conda with Poetry (Suitable for Development)
    - Method 2: Building the Docker Image and Running the Container (Suitable for Users)
  - Viewing the Application on GitHub Pages


## Project Overview

The GovTech Assessment project is designed to:
- Extract restaurant data and save it to a CSV file.
- Extract restaurant events and save them to a CSV file.
- Determine rating thresholds based on the aggregate ratings.

The code is written in Python and utilizes pandas for data processing. Docker is used to containerize the application, and GitHub Actions is set up for continuous integration and deployment.

For deployment using cloud services, a summary can be found in cloud_deployment.md and its corresponding architecture diagram in cloud_architecture_diagram.md.

An architecture diagram for this project can be found in project_architecture_diagram.md

## Assumptions

1. **Output Files for Tasks:**
   - As only Task 1 and Task 2 specify a requirement for an output CSV file, there is no output file for Task 3. Instead, the `rating_thresholds` table is printed directly to the console for local running.

2. **Handling Country Codes in Task 1:**
   - For Task 1, some entries in the restaurant data contain country codes that do not appear in the provided country code source file. These entries are treated as dummy data and are excluded from the final output.

3. **Output Display on GitHub Pages:**
   - A downstream web page has been set up where all three outputs (from Task 1, Task 2, and Task 3) can be viewed in tabular form. This is achieved by running the containerized application using GitHub workflows, which automates the extraction and deployment process.

4. **Decision to Use GitHub Workflows:**
   - The decision to use GitHub workflows was made because the repository is already hosted on GitHub, and this approach avoids overcomplicating the deployment infrastructure for this project. By leveraging GitHub Actions, we streamline the CI/CD process, allowing for automated builds and deployments directly to GitHub Pages.


## Requirements

Before setting up the project, ensure you meet the following requirements:

### For All Systems:
- **Python 3.10** or higher (if using Conda or Poetry)
- **Git** (for cloning the repository)
- **Internet Connection** (for downloading dependencies and Docker images)

### For Windows Users:
- **Windows Subsystem for Linux (WSL)** is recommended if running on a Windows environment.
  - [Installation Guide for WSL](https://docs.microsoft.com/en-us/windows/wsl/install)
- **Conda** installed OR
- **Docker** installed and Docker daemon is running
  - [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)

Ensure that either Conda is installed and properly configured, or Docker is installed with the Docker daemon running. For Docker, you can verify that the daemon is running.

## Setup and Installation

**Firstly, clone the Repository:**
    ```
    git clone https://github.com/<your-username>/GovTech-Assessment.git
    cd GovTech-Assessment
    ```

### 1. Running the Application Locally

This section is intended for developers and users who want to run the application on their local machine. There are two methods provided:

#### Method 1: Using Conda with Poetry (Suitable for Development)

**Conda Setup:**

1. **Create a new Conda environment:**
    ```bash
    conda create --name govtech-assessment python=3.10
    ```
2. **Activate the environment:**
    ```bash
    conda activate govtech-assessment
    ```
3. **Install poetry:**
    ```bash
    pip install poetry
    ```
4. **Install dependencies using poetry:**
    ```bash
    poetry install
    ```
5. **Run the application:**
    ```bash
    python main.py --extract_restaurants --extract_restaurant_events --determine_rating_thresholds --local
    ```
5. **Run unit tests using pytest:**
    ```bash
    pytest tests/
    ```

#### Method 2: Building the Docker Image and Running the Container (Suitable for Users)

1. **Build the Docker image:**
    ```bash
    docker build -t govtech-assessment .
    ```
2. **Run the Docker container with all flags:**
    ```bash
    docker run -v $(pwd):/app  govtech-assessment --extract_restaurants --extract_restaurant_events --determine_rating_thresholds --local
    ```
    
   - This method is more suitable for end-users who do not want to set up a Python environment locally and prefer to run the application in an isolated Docker container.

Using either method will output 2 files, restaurants.csv and restaurant_events.csv, in the output_data/ directory, as well as print out the rating_thresholds in the terminal.

### 2. Viewing the Application on GitHub Pages

This section is intended for users or developers who want to view the output on GitHub Pages or trigger a new deployment by pushing changes to the repository.

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/pkpaing/GovTech-Assessment.git
    cd GovTech-Assessment
    ```

2. **Make Changes (Optional):**
   - You can modify the code, for example, update the data processing logic, adjust the workflow, or customize the output.

3. **Push Changes to the Repository:**
   - If you make changes and want to trigger the GitHub Actions workflow to build and deploy the output to GitHub Pages, follow these steps:
   
    ```bash
    git add .
    git commit -m "Your commit message"
    git push origin master
    ```

   - This push will trigger the GitHub Actions workflow defined in `.github/workflows/deploy.yml`. The workflow will:
     - Build the Docker image.
     - Run the application with the specified flags.
     - Deploy the generated output to the `gh-pages` branch.

4. **View the Output on GitHub Pages:**
   - After the workflow runs successfully, the output will be available at:
   ```text
   https://pkpaing.github.io/GovTech-Assessment/
