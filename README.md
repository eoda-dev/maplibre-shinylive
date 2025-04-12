# MapLibre Shinylive

Deploy locally:

```bash
uv sync

source .venv/bin/activate

shinylive export \
	--subdir getting-started \
	--template-dir templates/app \
	--template-params '{"title": "MapLibre Getting Started"}' \
	--verbose \
	getting-started dist

python ./scripts/rendersite.py > dist/index.html

python -m http.server --directory dist --bind localhost 8008
```

