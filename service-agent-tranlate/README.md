## Language Translation Service Agent

### Running the Service Agent
1.  (Option 1) -- use ADK web
    ```
    (source .env; adk web --port 8080)
    ```
1.  (Option 2) -- run the agent's service endpoint
    ```
    (source .env; uvicorn service-agent-tranlate.main:app --reload --port 8080)
    ```

### Using the Service Agent

```
curl http://localhost:8080/translate \
-H "Content-Type: application/json" \
-d '{"text" : "hello world!", "target_language" : "french"}' 
```
