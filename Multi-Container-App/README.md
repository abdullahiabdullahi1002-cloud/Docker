# Multi-Container-App

## Description

**Multi-Container-App** is a multi-container web application built with [Flask](https://flask.palletsprojects.com/) and [Redis](https://redis.io/), demonstrating containerized development using Docker Compose. It showcases a Flask + Redis setup for tracking visitor counts in an isolated and reproducible environment.

Key components:

- [`app.py`](./app.py) — Flask application with `/` (welcome message) and `/count` (increments and displays visit count stored in Redis)
- [`templates/`](./templates) — HTML templates for Home, Count, and About pages
- [`static/`](./static) — CSS styling and images
- [`Dockerfile`](./Dockerfile) — Defines Flask container build steps
- [`docker-compose.yml`](./docker-compose.yml) — Orchestrates Flask and Redis containers with environment variables, volumes, and scaling
- [`nginx.conf`](./nginx.conf) — Optional reverse proxy configuration

---

# Multi-Container Web Application Deployment

## Objective

Provide a reproducible process for deploying a multi-container web application using:

- **Flask** web application
- **Redis** database
- **Docker** and **Docker Compose** for orchestration
- **NGINX** (optional) for load balancing

---

## Key Features

- Multi-container setup (Flask + Redis)
- Persistent data storage via Docker volumes
- Scalable Flask service
- Easy setup and testing
  
---

## Technologies Used

- Python / Flask
- Redis
- Docker & Docker Compose
- HTML/CSS
- NGINX (optional for reverse proxy)

---

## Setup & Testing Steps

## 1. Prepare Project Files

- **Flask App (`app.py`)**: Define `/` and `/count` routes.
- **HTML & CSS**:  
  - Place templates in `templates/`  
  - Place static files in `static/css/` and `static/images/`
- **Dockerfile**: Containerize the Flask app.
- **Docker Compose (`docker-compose.yml`)**: Define services for Flask (`web`) and Redis. Configure environment variables, volumes for Redis persistent storage, ports, and scaling.
- **NGINX (`nginx.conf`)** *(optional)*: Reverse proxy configuration for load balancing multiple Flask instances.

> **Explanation:** Ensures all project files are prepared and correctly structured before running Docker commands.

---

## 2. Configure Docker Compose for Flask and Redis

Use `docker-compose.yml` to define the Flask application (`web`) and Redis service.

**Configuration:**
- Environment variables to allow Flask to connect to Redis.
- Volumes for Redis data persistence.
- Ports to expose Flask and Redis services.
- Scaling options for Flask instances if needed.

> **Explanation:** Prepares the container orchestration, persistent storage, and inter-service communication.

---

## 2. Update Docker Compose for NGINX and Load Balancing

To enable load balancing, update your `docker-compose.yml` and add an NGINX configuration. Follow these sections as a single step:

---

### **A. Add NGINX Service to `docker-compose.yml`**

Add the following service definition to your `docker-compose.yml`:

```yaml
services:
    nginx:
        image: nginx:latest
        ports:
            - "5002:5002"
        volumes:
            - ./nginx.conf:/etc/nginx/nginx.conf:ro
        depends_on:
            - web
```

> **Note**  
> NGINX listens on port 5002 and proxies requests to Flask containers.

---

### **B. Create `nginx.conf` for Load Balancing**

Create an `nginx.conf` file in your project root with this content:

```nginx
events {}

http {
        upstream flask_app {
                server web:5000;
                # Docker Compose will add more 'web' containers automatically if scaled
        }

        server {
                listen 5002;

                location / {
                        proxy_pass http://flask_app;
                }
        }
}
```

> **Tip:**  
> Scaling Flask service automatically enables NGINX load balancing.

---

### **C. Build and Start Containers (with Optional Scaling)**

1. **Build all service images:**
   Before starting, ensure all images are built from your `docker-compose.yml` configuration:  
   ```bash
        docker-compose build
        ```
        

2. **Start the containers(standard or scaled Flask service):**
        - **Standard start (one Flask instance):**
      ```bash
        docker-compose up
      ```
      - Starts 1 container for the web service.

   **Scale Flask service start (multiple instances for load balancing):**
     ```bash
          docker-compose up --scale web=3 -d
     ```
      
      - `--scale web=3` runs 3 Flask containers.
      - `-d` runs containers in the background.
    
    Difference: Both commands start the application, but scaling runs multiple containers instead of just one useful for handling more traffic or improving reliability.

---

## 4. Test Application Functionality

1. **Home Page**  
Visit [http://localhost:5002/](http://localhost:5002/) — The main landing page.  

![Home Page](https://github.com/user-attachments/assets/ad1efd49-b605-4cb0-8d8f-ae35ea6dabee)  

---

2. **Counter Page**  
Visit [http://localhost:5000/count](http://localhost:5002/count) — A page where the counter increments with each refresh.  

![Counter Page](https://github.com/user-attachments/assets/1dd18a9e-fc63-4076-9107-f720205df2d9)  

Refresh the page to see the counter increment in action:  

![Counter Increment](https://github.com/user-attachments/assets/8547783b-4f6b-47db-aebb-080ac70a32db)  

---

3. **About Page**  
Visit [http://localhost:5000/about](http://localhost:5002make a/about) — Displays information about the application.  

![About Page](https://github.com/user-attachments/assets/cdbc8bdf-9de8-4037-b9ff-10d033f90fed)




## 5. Test Persistent Storage for Redis

1. **Stop the running containers:**

    ```bash
    docker-compose down
    ```

2. **Start the containers again:**

    ```bash
    docker-compose up -d
    ```

3. **Verify persistence:**

    Check if your previous Redis data (e.g., counters or keys) is still available.  
    This confirms that the Redis volume (`redis-data`) is persisting data across container restarts.



---

## 6. Shutdown Containers

- Stop and clean up:
    ```bash
    docker-compose down
    ```
- Optional: Remove volumes as well:
    ```bash
    docker-compose down -v
    ```

---

## Verification Checklist

- ✅ Home and Count pages work.
- ✅ Redis data persistence verified via volume.
- ✅ Optional NGINX routing and load balancing confirmed.

---

## Security Best Practices

- 🔒 Avoid exposing Redis publicly.
- 🔒 Limit exposed Docker Compose ports.
- 🔒 Use environment variables for sensitive data.

---





  
