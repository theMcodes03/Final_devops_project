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

## AWS EC2 Deployment (Demonstration Only)

This project was successfully deployed on an AWS EC2 instance as a practical demonstration of **cloud integration**. The instance was **subsequently terminated** to optimize resource usage and prevent ongoing charges.

The deployment process involved:

  * Provisioning an Ubuntu EC2 instance.
  * Installing Docker and Docker Compose.
  * Cloning this repository onto the instance.
  * Executing the application using `docker-compose`.
  * Configuring AWS Security Groups to allow public access on port 80.

-----

## Repository & Future Scope

The complete project source code is available on GitHub:

  * [https://github.com/theMcodes03/Final\_devops\_project](https://github.com/theMcodes03/Final_devops_project)

This project's architecture is highly conducive to further development, particularly the integration of **CI/CD pipelines** (e.g., GitHub Actions) for automated testing and continuous deployment to cloud environments or private servers.

-----

## Author

Manisha Shekhawat

-----
