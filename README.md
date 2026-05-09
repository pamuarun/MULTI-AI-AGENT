<div align="center">
  
# 🤖 MULTI-AI AGENT: Enterprise LLMOps Platform

**Next-Generation Agentic AI System with Advanced Orchestration, CI/CD, and AWS ECS Deployment**

[![Python Version](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](#)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-green?logo=chainlink&logoColor=white)](#)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Flows-purple)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](#)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white)](#)
[![SonarQube](https://img.shields.io/badge/SonarQube-Quality%20Gate-4E9BCD?logo=sonarqube&logoColor=white)](#)
[![AWS](https://img.shields.io/badge/AWS-ECS%20Fargate-FF9900?logo=amazonaws&logoColor=white)](#)

</div>

## 📖 Executive Overview

**MULTI-AI AGENT** is an enterprise-grade, highly scalable Agentic AI platform designed to orchestrate complex Language Model workflows using **LangGraph** and **LangChain**. Backed by ultra-fast inference via **Groq** and capable of executing specialized tasks, this repository establishes a robust **LLMOps** standard. 

The architecture encompasses a full lifecycle pipeline—from a containerized **FastAPI** backend and **Streamlit** frontend to automated CI/CD driven by **Jenkins**, code quality analysis via **SonarQube**, and production deployment on **AWS ECS Fargate**.

---

## 🚀 Key Features & Capabilities

### 🧠 Agentic AI & Generative Capabilities
- **LangGraph Orchestration**: Complex multi-agent workflows handling stateful, dynamic routing for LLM tasks.
- **Groq Inference Engine**: Utilizing `langchain-groq` for real-time, low-latency LLM text generation and agent reasoning.
- **Tavily Integration**: Intelligent web search and context retrieval capabilities built directly into the agent pipeline (`langchain-tavily`).
- **Pydantic Validation**: Strict input/output schema validation ensuring deterministic and reliable AI responses.

### ⚙️ LLMOps & Infrastructure
- **Automated CI/CD Pipeline**: Full end-to-end continuous integration and deployment using **Jenkins** inside Docker (DinD setup).
- **Code Quality Gates**: Integrated **SonarQube** analysis to enforce strict code quality and security standards before deployment.
- **Containerization**: Fully modularized Docker architecture with multi-stage builds.
- **Cloud-Native Deployment**: Seamless push to **AWS ECR** and rolling deployments to **AWS ECS Fargate** for highly available, serverless container execution.

---

## 🛠️ Technology Stack

| Domain | Technologies |
| :--- | :--- |
| **Language & Backend** | Python 3.10, FastAPI, Uvicorn |
| **Frontend UI** | Streamlit |
| **AI/ML & Agentic** | LangChain, LangGraph, Groq, Tavily |
| **CI/CD Orchestration** | Jenkins, GitHub Webhooks, SonarQube |
| **Containerization** | Docker, Docker-in-Docker (DinD) |
| **Cloud Infrastructure** | AWS ECS Fargate, AWS ECR, IAM |

---

## 🏗️ System Architecture

The workflow embodies a mature, scalable microservice architecture. 

<div align="center">
  <img src="Architecture/Multi+AI+Agent+Workflow.png" alt="Multi-AI Agent Workflow Architecture" width="800"/>
</div>

### Request Lifecycle:
1. **User Interaction**: Users interact with the sleek **Streamlit** UI.
2. **API Layer**: Requests are routed through the **FastAPI** backend endpoint.
3. **Agentic Orchestration**: **LangGraph** manages the state and routes the prompt to appropriate tools (e.g., Tavily search) or the LLM (Groq).
4. **CI/CD Trigger**: Code pushes trigger **Jenkins** pipelines, leading to a **SonarQube** quality check.
5. **Deployment**: Approved builds are containerized, pushed to **AWS ECR**, and updated live on **AWS ECS Fargate**.

---

## 📂 Project Structure

```text
MULTI-AI-AGENT/
├── app/                      # Core Application Source Code
│   ├── backend/              # FastAPI Server & Routes
│   ├── frontend/             # Streamlit UI Components
│   ├── core/                 # Agentic Logic, LangGraph Nodes, Models
│   ├── common/               # Shared Utilities & Helpers
│   ├── config/               # Configuration & Environment loading
│   └── main.py               # Application Entry Point
├── Architecture/             # System Architecture Diagrams
├── custom_jenkins/           # Jenkins DinD Configuration
├── Outputs/                  # Deployment & Localhost Screenshots
├── Input Queires/            # Evaluation datasets & test queries
├── Jenkinsfile               # Declarative CI/CD Pipeline Configuration
├── Dockerfile                # Production-ready Container Definition
├── requirements.txt          # Core Dependencies (FastAPI, LangChain, etc.)
├── setup.py                  # Project Packaging
└── FULL_DOCUMENTATION.md     # Complete Setup & Infrastructure Guide
```

---

## 📸 Outputs & Visual Proof of Execution

The repository includes visual evidence of local testing, pipeline execution, and cloud deployment maturity.

<details>
<summary><b>🖼️ View System Outputs & Screenshots</b></summary>

### Local Execution
- ![Localhost Interface](Outputs/Localhost%20output.png)
- ![Localhost Interaction 1](Outputs/Localhost%20output1.png)

### CI/CD Pipeline Success
- ![Jenkins Pipeline](Outputs/Jenkins.png)
- ![SonarQube Code Analysis](Outputs/SonarQube.png)

### AWS Infrastructure Setup
- ![IAM User Creation](Outputs/IAM%20User%20Creation.png)
- ![Cluster Creation](Outputs/Cluster%20Creation.png)

### Production Deployment (AWS ECS)
- ![Deployed Output Overview](Outputs/Deployed%20output.png)
- ![Deployed Output Detail](Outputs/Deployed%20Output%204.png)

</details>

---

## 🚦 Getting Started & Documentation

> [!IMPORTANT]
> **A detailed Documentation is Present in `FULL_DOCUMENTATION.md`.** It has been specifically authored by **Antigravity** to guide you through WSL setups, Docker DinD configurations, AWS ECS cluster creation, and Jenkins pipeline integrations.

### Quick Local Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Antigravity/MULTI-AI-AGENT.git
   cd MULTI-AI-AGENT
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Environment Variables (`.env`):**
   ```env
   GROQ_API_KEY=your_groq_key
   TAVILY_API_KEY=your_tavily_key
   ```
4. **Run Application:**
   ```bash
   python app/main.py
   ```

For advanced Cloud deployments and Jenkins setup, **please refer to [`FULL_DOCUMENTATION.md`](./FULL_DOCUMENTATION.md).**

---

## 🛡️ License & Authorship
Developed and Architected for Enterprise LLMOps demonstration. Documentation maintained and engineered by **Antigravity**.
