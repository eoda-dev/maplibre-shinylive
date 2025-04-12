from __future__ import annotations

import sys
import tomllib

import typer
from jinja2 import Template
from pydantic import BaseModel

app = typer.Typer()


class App(BaseModel):
    title: str
    dir: str


class Site(BaseModel):
    title: str = "MapLibre for Python"
    apps: list[App] = [App(title="Getting started", dir="getting-started")]

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


if __name__ == "__main__":
    app()
