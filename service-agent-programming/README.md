## Programming Service Agent

### Running the Service Agent
1.  (Option 1) -- use ADK web
    ```
    (source .env; adk web --port 9002)
    ```
1.  (Option 2) -- run the agent's service endpoint
    ```
    (source .env; uvicorn service-agent-programming.main:app --reload --port 9002)
    ```

### Using the Service Agent

```
curl http://localhost:9002/programming \
-H "Content-Type: application/json" \
-d '{"text" : "write a mcp tool", "target_language" : "python"}' 
```
