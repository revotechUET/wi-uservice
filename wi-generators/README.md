# WIPM Generator

## Requirement
---

* Linux (recommended Ubuntu 18.04)

* Java 8 JRE


## Usage
---

Move to wi-mod and run `./gen.sh [spec file] [output folder code]`

Ex:

```bash
$ ./gen.sh example.yaml samples/example
```

Move to output folder and run server

```bash
$ gunicorn -c prod.config.py wsgi:application
```

Fully specification in [output folder]/src/specs/openapi.yaml


## Notice
---

Create folder static in output folder
