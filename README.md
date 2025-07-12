# TruAID Demo 🛡️🤖

**TruAID (Trusted AI Decentralized)** is a platform that enables trusted, auditable, privacy-preserving collaboration between autonomous agents. This demo showcases how agents can communicate securely using Google A2A protocols, log their behavior to a blockchain-based audit trail, and surface model behavior through Weights & Biases — all while preserving PII.

---

## 🔍 What this Demo Shows

- 🤝 Secure **Agent-to-Agent (A2A)** interactions using Google’s A2A protocol.
- 🔗 Blockchain-anchored audit trails with **PII-preserving hash commitments**.
- 📊 Integrated observability using **Weights & Biases** (W&B) for agent behavior and model traces.
- 🚨 Privacy-aware logging system that alerts when **sensitive flows** are detected.

---

## 🧱 Architecture Overview
```
      +------------+       A2A Protocol       +------------+
      |  Agent A   |  <-------------------->  |  Agent B   |
      +------------+                         +------------+
           |                                        |
     [Local Action Logs]                    [Local Action Logs]
           |                                        |
           v                                        v
 +------------------+                  +------------------+
 |  PII-Redaction & |                  |  PII-Redaction & |
 |  Hash Generation |                  |  Hash Generation |
 +------------------+                  +------------------+
           |                                        |
           +-------------------+--------------------+
                               |
                               v
                     +--------------------+
                     |   Merkle Log Root  |
                     |   (batch anchor)   |
                     +--------------------+
                               |
                               |
                               v
                    +------------------------+
                    |     TruAID Dashboard   |
                    |  (via W&B + blockchain)|
                    +------------------------+
```
---

## Usage

### Local Testing

1.  setup python virtual environment
    ```
    python3.12 -m venv .venv
    ```
    ```
    source .venv/bin/activave
    ```

1.  install project dependencies
    ```
    pip install -r requirements.txt
    ```

1.  setup local `.env` file
    ```
    export WANDB_PROJECT_ID="TruAID"
    export GOOGLE_GENAI_USE_VERTEXAI="True"
    export WANDB_API_KEY="<<your weave project API key>>"
    export GOOGLE_CLOUD_PROJECT="<<your GCP project ID>>"
    ```
1.  make sure that you have gcloud authenticated for local use
    ```
    gcloud auth application-default login
    ```

### Running the Service Agent
1.  (Option 1) -- use ADK web
    ```
    (source .env; adk web --port 7000)
    ```
1.  (Option 2) -- run the agent's service endpoint
    ```
    (source .env; uvicorn service-agent.main:app --reload)
    ```
