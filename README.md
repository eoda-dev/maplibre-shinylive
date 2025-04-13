# MapLibre for Python Shinylive Example Apps

Deploy locally:

```bash
uv sync

source .venv/bin/activate

# Export shinylive apps
python ./scripts/deploy.py export 

# Render main 'index.html'
python ./scripts/deploy.py render > dist/index.html '

# Serve site
python -m http.server --directory dist --bind localhost 8008
```

Run apps locally without deployment:

```bash
shiny run apps/getting-started/app.py
```
