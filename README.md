# fastPortal

A lightweight portal generating Python app.

## Installation

```bash
make install
```

## Usage

Define your portal page using YAML in [portals/](portals/). You can model yours after the [example](portals/example.yml). You may also include static elements in [static/](static/).

For development/testing:

```bash
make up
```

For a production deployment:

```bash
./publish.sh IMAGE_NAME:IMAGE_TAG
```
