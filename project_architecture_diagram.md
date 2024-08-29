# Project Architecture Diagram

```mermaid
graph TD;
    A[Data Source] -->|Load Data| B[main.py];
    B -->|Process Data| C[Extract Restaurants];
    B -->|Process Data| D[Extract Restaurant Events];
    B -->|Process Data| E[Determine Rating Thresholds];
    C -->|Save to File| F[restaurants.csv];
    D -->|Save to File| G[restaurant_events.csv];
    E -->|Print Output| H[Rating Thresholds];

    subgraph Outputs
        F
        G
        H
    end

    subgraph Docker and CI/CD
        I[Dockerfile] -->|Containerize| B;
        J[GitHub Workflows] -->|Trigger Build & Tests| B;
        J -->|Trigger Docker Build| I;
    end
