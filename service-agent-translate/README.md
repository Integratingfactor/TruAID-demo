## Language Translation Service Agent

### Running the Service Agent
1.  (Option 1) -- use ADK web
    ```
    (source .env; adk web --port 9001)
    ```
1.  (Option 2) -- run the agent's service endpoint
    ```
    (source .env; uvicorn service-agent-translate.main:app --reload --port 9001)
    ```

### Using the Service Agent

```
curl http://localhost:9001/translate \
-H "Content-Type: application/json" \
-d '{"text" : "hello world!", "target_language" : "french"}' 
```
