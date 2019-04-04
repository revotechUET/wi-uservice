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
$ install [model_name]
```

Run service

```bash
$ gunicorn -c prod.config.py wsgi:application
```
