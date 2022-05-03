#!/usr/bin/python

from jinja2 import Template

f = open("r-babs.def.j2", "r")
template = Template(f.read())
f.close()

data = {}
data["cran"] = "'" + "', '".join(sorted([l.rstrip() for l in open("cran.txt", "r")])) + "'"
data["bioc"] = "'" + "', '".join(sorted([l.rstrip() for l in open("bioc.txt", "r")])) + "'"

print(template.render(data))

