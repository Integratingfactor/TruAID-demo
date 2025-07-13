## Writing Service Agent

### Running the Service Agent
1.  (Option 1) -- use ADK web
    ```
    (source .env; adk web --port 9003)
    ```
1.  (Option 2) -- run the agent's service endpoint
    ```
    (source .env; uvicorn service-agent-writing.main:app --reload --port 9003)
    ```

### Using the Service Agent

```
curl http://localhost:9003/write \
-H "Content-Type: application/json" \
-d '{"text" : "write stories about unitree dogs"}' 
```
