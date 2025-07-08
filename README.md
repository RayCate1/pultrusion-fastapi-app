# Pultrusion Workflow App

A unified application for pultrusion process design and machine data generation, combining:

* **Geometry Generation**: Procedurally generate Blender models from input parameters.
* **Machine Data Computation**: Calculate process data (e.g., pull speed, resin ratios).
* **Parts Export**: Produce CAD/STEP files for machine components.

Everything runs through a single API-first service, enabling easy integration and extension.

---

## Features

* Headless Blender geometry export (glTF/.glb)
* Machine-data JSON output
* Parts/assembly STEP or ZIP export
* REST API with FastAPI, auto-generated OpenAPI docs
* Simple static front-end for parameter entry and result download
* Dockerized for easy deployment
* GitHub Actions CI/CD pipeline

---

## Prerequisites

* Python 3.11+
* Blender (compatible CLI version)
* Docker (optional, for containerized deployment)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/pultrusion-app.git
   cd pultrusion-app
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**

   * Copy `.env.example` to `.env` and set paths (e.g. `BLENDER_PATH`, secrets)

---

## Usage

### Run Locally

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

* Front-end: [http://localhost:8000/index.html](http://localhost:8000/index.html)
* API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Docker Compose

```bash
docker-compose up --build
```

* Front-end: [http://localhost:8501/index.html](http://localhost:8501/index.html)

---

## Project Structure

```
pultrusion-app/                  ← repo root
├ README.md                      ← this file
├ LICENSE
├ .gitignore                     ← ignore env, outputs/
├ requirements.txt               ← Python dependencies
├ modules/                       ← core logic modules
│  ├ geometry.py                 ← Blender headless exporter
│  ├ machine.py                  ← machine-data calculator
│  └ parts.py                    ← parts generator
├ backend/                       ← FastAPI application
│  └ main.py
├ static/                        ← front-end assets (HTML, JS)
│  └ index.html
├ docker/                        ← Dockerfiles & compose config
│  ├ Dockerfile.backend
│  └ docker-compose.yml
└ .github/                       ← GitHub Actions workflows
   └ workflows/
      ├ ci.yml                   ← lint, tests, type-check
      └ cd.yml                   ← Docker build & publish
```

---

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/XYZ`)
3. Commit your changes (`git commit -m "Add XYZ feature"`)
4. Push to the branch (`git push origin feature/XYZ`)
5. Open a Pull Request

Please adhere to existing code style and include tests.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
