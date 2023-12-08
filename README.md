# fastPortal

A lightweight portal generating Docker container.

## Installation

```bash
make install
```

## Usage

Define your portal page using YAML in [portals/](portals/). You can model yours after the [example](portals/example.yml).

For development/testing, run `make up`. View the [docker-compose.yml](docker-compose.yml) if you need to change ports.

For production deployment, run `./publish.sh IMAGE_NAME:IMAGE_TAG`.
