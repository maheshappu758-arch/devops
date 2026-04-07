# OCI Python Web Application

A simple Flask-based web application designed for deployment on **Oracle Cloud Infrastructure (OCI)** using OCI DevOps and Container Registry.

## 🚀 Features
- **Flask Web Server**: Simple Python app with basic routing.
- **Dockerized**: Ready to run as a container using the provided `Dockerfile`.
- **OCI DevOps Integration**: Includes `build_spec.yaml` for automated container builds in Oracle Cloud.
- **Gunicorn Implementation**: Production-grade WSGI server configuration.

## 🛠 Project Structure
- `app.py`: Main Flask application.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Instructions to build the application container.
- `build_spec.yaml`: OCI DevOps build pipeline configuration.
- `.gitignore`: Files to exclude from the repository.

## ☁️ Deploying to Oracle Cloud
1. Create a **Code Repository** in OCI DevOps and mirror this GitHub repo or push to it.
2. Create a **Build Pipeline** in OCI DevOps.
3. Add a **Build Stage** and link it to the `build_spec.yaml` in this repository.
4. Configure an **Artifact** to store the built Docker image in **OCI Container Registry (OCIR)**.

## 💻 Local Development
1. **Clone the repository**:
   ```bash
   git clone https://github.com/maheshappu758-arch/devops
   cd devops
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   python app.py
   ```
   Or use Docker:
   ```bash
   docker build -t oci-python-app .
   docker run -p 5000:5000 oci-python-app
   ```
