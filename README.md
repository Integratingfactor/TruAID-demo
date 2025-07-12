# truaid-demo

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
1.  (Option 1) -- run the agent's service endpoint
    ```
    (source .env; uvicorn service-agent.main:app --reload)
    ```
1.  (Option 2) -- use ADK web
    ```
    (source .env; adk web)
    ```
