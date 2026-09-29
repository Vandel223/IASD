### Developed for IASD at Instituto Superior Técnico - 1st Deliverable

# Gardener Problem

A search-based solver for the **Gardener Problem**: an agent moves around a grid watering plants before their deadlines, without running out of water.

## Files

- `solution.py` — defines the problem (grid, water tank, plants, deadlines) and checks whether a given plan is valid.
- `utils.py` — shared helper functions (AIMA-style search utilities).

## How it works

The gardener starts at `(0, 0)` with a water tank of capacity `W0`. It moves with `U`, `D`, `L`, `R` and waters a plant with `W`. Each plant needs a certain amount of water and must be watered before its deadline. The tank refills whenever the gardener returns to the start.

## Usage

```bash
python solution.py <input_file> --plan <plan_file>
```

- `<input_file>` — problem definition (grid size, tank capacity, grid layout, plant water/deadline info).
- `<plan_file>` — a plan to check, written as a string of moves (e.g. `RRWDLW`).

## Requirements

- Python 3
- NumPy
