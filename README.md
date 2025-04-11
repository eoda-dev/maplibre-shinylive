# MapLibre Shinylive

```bash
uv sync

source .venv/bin/activate

shinylive export \
	--subdir getting-started \
	--template-dir template \
	--template-params '{"title": "MapLibre Getting Started"}' \
	--verbose \
	getting-started dist

python3 -m http.server --directory dist --bind localhost 8008
```

