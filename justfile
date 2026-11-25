build:
    uv run --no-project --with pyyaml scripts/build_catalog.py

zip:
    uv run --no-project --with pyyaml scripts/build_plugin.py

new-version:
    uv run --no-project --with pyyaml scripts/build_plugin.py --new-version
