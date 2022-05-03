#!/usr/bin/python

from jinja2 import Template

f = open("jupyter.def.j2", "r")
template = Template(f.read())
f.close()

data = {}
data["pip_packages"] = sorted( [ l.rstrip() for l in open("pip.txt", "r") ] )

print(template.render(data))

