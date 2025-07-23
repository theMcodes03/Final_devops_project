# Final DevOps Project

This project demonstrates core **DevOps principles** through the **containerization** of a Flask application with Docker, its exposure via an **Nginx reverse proxy**, and an exploration of **cloud deployment** on AWS EC2.

-----

## Key Features

  * **Dockerized Flask Application**: A lightweight, portable container for the backend service.
  * **Nginx Reverse Proxy**: Efficiently manages and routes web traffic to the Flask application.
  * **Docker Compose Orchestration**: Streamlines the setup, linking, and management of multi-container environments.
  * **Local Development Ready**: Easily deployable and testable on any local machine.
  * **Cloud Deployment Showcase**: Configured for straightforward deployment, briefly demonstrated on AWS EC2.

-----

## Project Structure

```
.
├── app/
│   ├── app.py
│   └── requirements.txt
├── nginx/
│   └── nginx.conf
├── Dockerfile
├── docker-compose.yml
└── README.md
```

  * **`app/`**: Contains the Flask application logic and its required Python packages.
  * **`nginx/`**: Houses the Nginx configuration, detailing how web requests are forwarded to the Flask service.
  * **`Dockerfile`**: Defines the build process for the Flask application's Docker image.
  * **`docker-compose.yml`**: The central configuration file for defining and running the multi-service Docker application.

-----

## Getting Started

### Prerequisites

Ensure you have **Docker** and **Docker Compose** installed on your system:

  * [Install Docker](https://docs.docker.com/get-docker/)
  * [Install Docker Compose](https://docs.docker.com/compose/install/)

### Local Deployment

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/theMcodes03/Final_devops_project.git
    cd Final_devops_project
    ```

2.  **Build and run the services**: This command will build the necessary Docker images and start both the Flask and Nginx containers.

    ```bash
    docker-compose up --build
    ```

3.  **Access the application**: Once the services are active, open your web browser and navigate to:

      * **Local URL**: `http://localhost`

    The Nginx proxy, listening on port `80`, directs traffic to the Flask application, which operates internally on port `5000`.

4.  **Stop services**: To halt and remove the running containers:

    ```bash
    docker-compose down
    ```

-----
Azure VM Deployment (Demonstration Only)
This project was successfully deployed on a Microsoft Azure Virtual Machine as a practical demonstration of cloud deployment and DevOps integration. The VM was later deallocated to prevent unnecessary billing.

Azure Deployment Process
Provisioned an Ubuntu VM via the Azure Portal or Azure CLI.

Configured Network Security Groups (NSGs) to allow HTTP (port 80) traffic.

Installed Docker & Docker Compose using the official installation scripts.

Cloned the project repository onto the VM.

Deployed the application using:

bash
Copy
Edit
docker-compose up --build -d
Accessed the app publicly via the VM's public IP.

Additional Azure Tools You Can Integrate:
Azure CLI: To automate VM provisioning and resource management.

Azure DevOps Pipelines: To create CI/CD workflows for build, test, and deployment stages.

Azure Container Instances (ACI) or App Services: For scalable container deployment alternatives.

Azure Monitor: For performance and health insights into your deployed containers.

-----

## Repository & Future Scope

The complete project source code is available on GitHub:

  * [https://github.com/theMcodes03/Final\_devops\_project](https://github.com/theMcodes03/Final_devops_project)

This project's architecture is highly conducive to further development, particularly the integration of **CI/CD pipelines** (e.g., GitHub Actions) for automated testing and continuous deployment to cloud environments or private servers.

-----

## Author

Manisha Shekhawat

-----
