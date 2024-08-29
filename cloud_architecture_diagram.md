# Cloud Architecture Diagram

```mermaid
graph TD;
    A[Data Source] -->|Retrieve Data| B[API/Client Database];
    B -->|Push Data| C[S3 Bucket];
    C -->|Load Data| D[AWS Redshift];
    E[Run main.py] -->|Containerized Pipeline| F[AWS ECR];
    F -->|Orchestrate| G[AWS Step Functions];
    G -->|Trigger Jobs| H[AWS Batch];
    H -->|Schedule| I[AWS EventBridge];
    I -->|Incremental Load| D;
    subgraph Infrastructure Management
        F
        G
        H
        I
        C
        D
    end
    subgraph Infrastructure as Code
        J[Terraform]
    end
    J --> F
    J --> G
    J --> H
    J --> I
    J --> C
    J --> D