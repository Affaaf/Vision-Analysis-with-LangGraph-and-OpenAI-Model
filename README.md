# 🧠 Vision Analysis with LangGraph & OpenAI

This project compares **pairs of property images** using a **LangGraph pipeline** and **OpenAI's vision model**, then generates a detailed report of the visual differences.

---


## 🚀 Features

- Load multiple image pairs (`pair1imageA.png`, `pair1imageB.png`, etc.)
- Analyze visual differences using GPT-4 Vision
- Aggregate and save results into a final report
- Dockerized for consistent environment

---


## 🛠️ Requirements

- Python 3.10+ (for local runs)
- Docker (for containerized runs)
- OpenAI API key

---
## Root Directory

```env
cd vision-analysis
```
---

---

## 🔐 .env File

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key_here
```

> ⚠️ Make sure there are no spaces before or after the key name/value.

---

## 🧪 Run Locally (No Docker)

Install dependencies (use a virtualenv ):

## 🧪 Run Locally (No Docker)

### Step 1: Create & activate a virtual environment

**On macOS/Linux:**

```bash
python3 -m venv env
source env/bin/activate
```

**On Windows:**

```bash
python -m venv env
env\Scripts\activate
```


```bash
pip install -r requirements.txt
```
---

## 📸 Image Naming Convention

Add your images in `utils/images/` following this format:
It currently works with .png files and supports only 4 pairs.

- `pair1imageA.png`
- `pair1imageB.png`
- `pair2imageA.png`
- `pair2imageB.png`
- `pair3imageA.png`
- `pair3imageB.png`
- `pair4imageA.png`
- `pair5imageB.png`
---

```bash
python main.py
```

Output report will be saved to:

```
./outputs/final_report.txt
```

---

## 🐳 Run with Docker

### 1. Build Docker image:

```bash
docker build -t vision-analysis .
```

### 2. Run the container with `.env` and output folder mount:

```bash
docker run --rm -it \
  --env-file .env \
  -v $(pwd)/outputs:/app/outputs \
  vision-analysis
```

> This mounts your local `outputs/` folder to the container so the final report is accessible after the container exits.

---

## 📄 Access the Output Report

After the Docker run, check:

```
./outputs/final_report.txt
```

> This file contains the aggregated analysis of all image pairs.

---
