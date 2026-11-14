# platitude-genre
Offline training pipeline for Platitude's on-device genre tagger. Trains a small
mel-CNN on a permissively-licensed FMA subset and exports `genre.onnx`.
See `docs` in the platitude repo: 2026-07-01-genre-tagging-design.md.
## Setup
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
