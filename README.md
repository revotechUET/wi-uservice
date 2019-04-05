# Regression service
---


### Requirements
---

* Java (maven)
* Python (pip)
* MongoDB


### Installation
---

Generate service

```bash
$ ./generate.sh
```

Run service

```bash
$ gunicorn -c prod.config.py wsgi:application
```
