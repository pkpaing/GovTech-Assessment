# Cloud Architecture Design and Deployment

## Summary

In this project, I propose a cloud-based architecture using AWS services to efficiently handle data ingestion, processing, and storage. As the data source evolves from static files to dynamic sources such as APIs or client databases, additional configurations will be implemented to connect and retrieve the data seamlessly.

## Data Ingestion and Storage

### AWS S3 for Data Storage

The ingested data will be stored in AWS S3 buckets in parquet format with date partitioning. AWS S3 is chosen for its scalability, durability, and cost-effectiveness in storing large datasets. Partitioning the data by date enhances query performance and reduces costs by allowing selective access to relevant data.

### AWS Redshift for Data Warehousing

Data stored in S3 can be loaded into AWS Redshift, a fully managed data warehousing service. Redshift is ideal for this use case due to its ability to handle fast and scalable querying of large datasets, making it suitable for analytics and reporting. The ETL process from S3 to Redshift ensures that the data is transformed and structured optimally for downstream applications requiring high-performance querying.

## Data Processing Pipeline

### Containerization with AWS ECR

The entire data pipeline, managed by running `main.py`, will be containerized, with the image stored in AWS Elastic Container Registry (ECR). This setup facilitates easy deployment, version control, and consistency across environments.

### Workflow Orchestration with AWS Step Functions

To automate and manage the data ingestion process, AWS Step Functions will be employed to orchestrate different data ingestion tasks. State machines within Step Functions will handle various parameters passed to `main.py`, allowing flexibility in either pushing data to S3 or pulling data from Redshift. AWS Step Functions provide a scalable and reliable method to manage complex workflows with clear visibility into each step.

### Scheduling with AWS EventBridge

These workflows can be triggered by AWS EventBridge, enabling scheduled execution of state machines at specific intervals—daily, weekly, or monthly—depending on data ingestion needs. EventBridge targets will include AWS Batch jobs, which are responsible for executing the data ingestion tasks, ensuring that data is incrementally added to Redshift and keeping the warehouse current.

## Infrastructure Management

### Infrastructure as Code with Terraform

The entire infrastructure, encompassing AWS ECR, Step Functions, Batch, EventBridge, IAM Roles, Redshift, and S3, will be managed using Terraform. By defining infrastructure as code within an `infra/` folder with separate files (e.g., `ecr.tf`, `step.tf`, `batch.tf`, etc.), we ensure a repeatable, scalable, and version-controlled deployment. Terraform automates resource provisioning, reducing human error and improving deployment efficiency. Additionally, the Terraform state files and any log files generated from the step-batch jobs can be saved their own S3 buckets.

## Conclusion

This cloud architecture leverages AWS services to provide a scalable, efficient, and flexible solution for managing data ingestion and processing. The infrastructure is designed to evolve and scale as data sources and requirements grow, ensuring the system remains robust and efficient.
