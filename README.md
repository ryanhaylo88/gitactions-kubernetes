# DevOps Portfolio - Local K3s Deployment

## Overview
This project demonstrates a fully automated **local CI/CD pipeline** with:

- FastAPI app
- Docker container
- Local K3s cluster
- GitHub Actions using self-hosted runner
- GHCR image registry

## How It Works
1. Push to `main` branch triggers GitHub Actions on local runner
2. Workflow builds Docker image and pushes to GHCR
3. Deployment manifests updated (`APP_VERSION` reflects commit)
4. K3s deployment is applied → pod restarts with new image

## Access App
http://<your-node-ip>:30007

## Tech Stack
- Docker
- Kubernetes (K3s)
- GitHub Actions
- FastAPI (Python)