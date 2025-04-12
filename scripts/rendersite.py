import sys
from jinja2 import Template
from pydantic import BaseModel

class Link(BaseModel):
    text: str
    href: str

class TemplateVariables(BaseModel):
    title: str = "MapLibre for Python"
    links: list[Link] = [
        Link(text="Getting started", href="getting-started")
    ]

def render(filename: str) -> str:
    with open(filename) as f:
        template = Template(f.read())

    kwargs = TemplateVariables().model_dump()
    return template.render(**kwargs)

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "templates/site/index.html"
    print(render(filename))
