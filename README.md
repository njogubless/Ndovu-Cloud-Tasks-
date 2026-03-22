# 🚀 DevOps Infrastructure Automation

> End-to-end deployment pipeline with IaC, containers, orchestration, CI/CD & monitoring.

![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Containers-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Ansible](https://img.shields.io/badge/Config-Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white)
![Travis CI](https://img.shields.io/badge/CI/CD-Travis_CI-3EAAAF?style=flat-square&logo=travisci&logoColor=white)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

---

## 📋 Overview

A production-grade DevOps pipeline that automates the full lifecycle of application deployment — from infrastructure provisioning to container orchestration, configuration management, CI/CD, and observability.

Every layer of the stack is **codified, version-controlled, and reproducible**:

- **Terraform** provisions cloud infrastructure as code
- **Docker** containerizes workloads for environment consistency
- **Kubernetes (Minikube)** orchestrates containers at scale
- **Ansible** manages server configuration idempotently
- **Travis CI** automates build, test, and deploy on every push
- **Prometheus** monitors system health and metrics
- **Nginx** acts as a reverse proxy (Jinja2 templated via Ansible)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CI/CD Layer                          │
│              Travis CI → deploy.yml → deploy.sh             │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                   Infrastructure Layer                       │
│           Terraform (main.tf) → Cloud Resources             │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                 Configuration Layer                          │
│         Ansible Playbook + Inventory → Server Config        │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                 Orchestration Layer                          │
│    Kubernetes (deployment.yaml + service.yaml) → Pods       │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  Application Layer                           │
│        Docker + Docker Compose → Containerized App          │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                Observability Layer                           │
│         Prometheus (metrics) + Nginx (reverse proxy)        │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
├── main.tf                    # Terraform infrastructure definitions
├── terraform.tfstate          # Terraform state file
├── terraform.tfstate.backup   # State backup for recovery
├── .terraform.lock.hcl        # Provider dependency lock file
├── Dockerfile                 # Application container image
├── docker-compose.yml         # Multi-service container orchestration
├── deployment.yaml            # Kubernetes Deployment manifest
├── service.yaml               # Kubernetes Service manifest
├── .travis.yml                # Travis CI pipeline configuration
├── deploy.yml                 # Deployment automation config
├── deploy.sh                  # Deployment shell script
├── playbook.yml               # Ansible configuration playbook
├── inventory.ini              # Ansible host inventory
├── nginx.conf.j2              # Nginx reverse proxy (Jinja2 template)
├── prometheus.yml             # Prometheus monitoring config
├── manage.py                  # Project utility scripts
├── requirements.txt           # Python dependencies
├── minikube_latest_amd64.deb  # Minikube installer
└── report_db                  # Reporting database artifacts
```

---

## 🛠️ Tech Stack

| File | Tool | Category | Purpose |
|------|------|----------|---------|
| `main.tf` + `terraform.tfstate` | Terraform | IaC | Provision cloud resources declaratively |
| `Dockerfile` + `docker-compose.yml` | Docker | Container | Containerize app for environment parity |
| `deployment.yaml` + `service.yaml` | Kubernetes | Orchestration | Manage pod deployment & service exposure |
| `.travis.yml` + `deploy.yml` + `deploy.sh` | Travis CI | CI/CD | Automate build, test & deploy on push |
| `playbook.yml` + `inventory.ini` | Ansible | Config Mgmt | Idempotent server provisioning |
| `prometheus.yml` | Prometheus | Monitoring | Metrics scraping & alerting |
| `nginx.conf.j2` | Nginx | Proxy | Reverse proxy with dynamic config via Jinja2 |

---

## 🚀 Getting Started

### Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform/install) >= 1.0
- [Docker](https://docs.docker.com/get-docker/) & Docker Compose
- [kubectl](https://kubernetes.io/docs/tasks/tools/) + [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/) >= 2.10
- Travis CI account (for CI/CD pipeline)
- Python 3.x (for `manage.py` utilities)

---

### 1. Provision Infrastructure

```bash
terraform init
terraform plan
terraform apply
```

### 2. Configure Servers

```bash
ansible-playbook -i inventory.ini playbook.yml
```

### 3. Build & Run Containers

```bash
docker-compose up --build -d
```

### 4. Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 5. Verify Deployment

```bash
kubectl get pods
kubectl get services
```

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers the Travis CI pipeline:

```
Push to main
     ↓
[1] Trigger   — Travis CI detects the push
     ↓
[2] Build     — Docker image built from Dockerfile
     ↓
[3] Test      — Automated tests run inside the container
     ↓
[4] Push      — Image pushed to container registry
     ↓
[5] Deploy    — deploy.sh invoked to roll out new version
     ↓
[6] Verify    — Health checks confirm successful deployment
```

---

## 📊 Monitoring & Observability

**Prometheus** is configured to scrape metrics from all running services:

- Real-time metrics collection from application and infrastructure
- Configurable alert rules for threshold-based notifications
- Time-series data retention for trend analysis
- Service discovery via static configs in `prometheus.yml`

**Nginx** acts as a reverse proxy, handling:

- SSL termination and request routing
- Load distribution across pods
- Dynamic config generation via the Jinja2 template (`nginx.conf.j2`) rendered by Ansible

---

## 💡 Key Engineering Concepts

| Concept | Implementation |
|---------|---------------|
| **Infrastructure as Code** | All infra is version-controlled via Terraform — reproducible and auditable |
| **Immutable Deployments** | Docker ensures environment consistency from dev to production |
| **GitOps** | Every infra change flows through version control and CI/CD |
| **Idempotency** | Ansible playbooks run safely multiple times without unintended side effects |
| **Observability-first** | Monitoring is configured alongside the app, not added as an afterthought |
| **Least-privilege Networking** | Nginx proxies all external traffic; services communicate internally |

---

## 📌 Roadmap

- [x] Terraform infrastructure provisioning
- [x] Docker containerization
- [x] Kubernetes deployment manifests
- [x] Travis CI pipeline
- [x] Ansible configuration management
- [x] Prometheus monitoring
- [x] Nginx reverse proxy
- [ ] Helm charts for Kubernetes
- [ ] Grafana dashboards for Prometheus metrics
- [ ] Multi-environment support (staging/production)
- [ ] Secrets management (Vault / AWS Secrets Manager)

---

## 👤 Author

**njogubless**
Nairobi-based software engineer working across the full depth of the stack — mobile, backend, and infrastructure. I ship products that work in the real world: fast, resilient, and built to grow.

---
