from __future__ import annotations

import json
import subprocess
import tomllib
from pathlib import Path

import typer
from jinja2 import Template
from pydantic import BaseModel

APPS_ROOT = Path("apps")

app = typer.Typer()


class App(BaseModel):
    title: str
    dir: str


class Site(BaseModel):
    title: str = "MapLibre for Python"
    subtitle: str = "Shinylive"
    apps: list[App]  # = [App(title="Getting started", dir="getting-started")]

    @classmethod
    def read_config(cls, filename: str) -> Site:
        with open(filename, "rb") as f:
            cfg = tomllib.load(f)

        return cls(**cfg["site"])

    def render(self, filename: str) -> str:
        with open(filename) as f:
            template = Template(f.read())

        return template.render(**self.model_dump())


@app.command(help="Render site")
def render(
    input: str = "templates/site/index.html", config: str = "config/site.toml"
) -> None:
    site = Site.read_config(config)
    print(site.render(input))


@app.command(help="Export apps")
def export(config: str = "config/site.toml") -> None:
    site = Site.read_config(config)
    print(site)
    for app in site.apps:
        cmd = [
            "shinylive",
            "export",
            "--subdir",
            app.dir,
            "--template-dir",
            "templates/app",
            "--template-params",
            json.dumps(dict(title=app.title)),
            APPS_ROOT / app.dir,
            "dist",
        ]
        # print(cmd)
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.args)
        print(result.stderr)


if __name__ == "__main__":
    app()
