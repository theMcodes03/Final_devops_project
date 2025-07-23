# Final DevOps Project

This project demonstrates core **DevOps principles** through the **containerization** of a Flask application with Docker, its exposure via an **Nginx reverse proxy**, and an exploration of **cloud deployment** using **Microsoft Azure**.

---

## Key Features

* **Dockerized Flask Application**: A lightweight, portable container for the backend service.
* **Nginx Reverse Proxy**: Efficiently manages and routes web traffic to the Flask application.
* **Docker Compose Orchestration**: Streamlines the setup, linking, and management of multi-container environments.
* **Local Development Ready**: Easily deployable and testable on any local machine.
* **Azure Cloud Deployment Showcase**: Configured for straightforward deployment on Microsoft Azure Virtual Machines.

---

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

---

## Getting Started

### Prerequisites

Ensure you have **Docker** and **Docker Compose** installed on your system:

* [Install Docker](https://docs.docker.com/get-docker/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)

### Local Deployment

1. **Clone the repository**:

   ```bash
   git clone https://github.com/theMcodes03/Final_devops_project.git
   cd Final_devops_project
   ```

2. **Build and run the services**:

   ```bash
   docker-compose up --build
   ```

3. **Access the application**:

   Navigate to `http://localhost` in your web browser.

4. **Stop services**:

   ```bash
   docker-compose down
   ```

---

## Azure VM Deployment (Demonstration Only)

This project was successfully deployed on a **Microsoft Azure Virtual Machine** as a practical demonstration of **cloud deployment and DevOps integration**. The VM was later **deallocated** to avoid unnecessary charges.

### Azure Deployment Steps

* **Provisioned an Ubuntu VM** using [Azure Portal](https://portal.azure.com/) or Azure CLI.

* **Configured Network Security Groups (NSGs)** to allow HTTP (port 80) traffic.

* **Installed Docker & Docker Compose** on the VM.

* **Cloned the project repository**.

* **Executed**:

  ```bash
  docker-compose up --build -d
  ```

* **Application Accessed** via the VM’s public IP on port 80.

### Optional Azure Integrations

* **Azure CLI**: For automated resource creation and management.
* **Azure DevOps Pipelines**: CI/CD integration for automated deployment.
* **Azure Container Registry (ACR)**: For storing and pulling Docker images securely.
* **Azure App Service or ACI**: To host containers without managing VMs.
* **Azure Monitor and Log Analytics**: For tracking performance and logs.

---

## Repository & Future Scope

The complete project source code is available on GitHub:

* [https://github.com/theMcodes03/Final\_devops\_project](https://github.com/theMcodes03/Final_devops_project)

### Future Enhancements

* Implement **CI/CD with Azure DevOps or GitHub Actions**.
* Add **SSL (HTTPS)** support via Let's Encrypt or Azure-managed certificates.
* Containerize with **multi-stage builds** for smaller image sizes.
* Integrate monitoring and alerting tools.

---

## Author

**Manisha Shekhawat**

---

