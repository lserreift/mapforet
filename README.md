# Gestion de l'arbre (MapForêt)

This project aims to map, document, and promote the urban trees of Arcachon (33 120). The goal is to provide open data, foster community engagement, and support local ecological initiatives.

## Features

- Open and collaborative mapping of urban trees
- Data collection and sharing
- Community-driven updates and contributions
- **Calculator module for performing additions** (calculateur d'additions)

## Calculator Module / Module Calculateur

This repository includes a calculator module (`calculator.py`) that provides functionality for performing additions. This can be useful for various calculations related to tree data analysis.

### Usage / Utilisation

#### Command Line Interface / Interface en ligne de commande

```bash
python3 calculator.py
```

The CLI supports two input formats:
- Space-separated numbers: `2 3 4`
- Addition expressions: `2+3+4`

#### Python Module / Module Python

```python
from calculator import add_numbers, add_list, calculate_addition

# Add multiple numbers / Additionner plusieurs nombres
result = add_numbers(2, 3, 5)  # Returns 10

# Add numbers from a list / Additionner des nombres d'une liste
result = add_list([1.5, 2.5, 3])  # Returns 7.0

# Calculate from string expression / Calculer à partir d'une expression
result = calculate_addition("10 + 20 + 30")  # Returns 60
```

#### Testing / Tests

Run the test suite:
```bash
python3 test_calculator.py
```

## Project Wiki

For detailed documentation, guides, and project updates, please visit the [Project Wiki](../../wiki).

## How to Contribute

1. Fork the repository
2. Submit data or improvements via pull requests
3. Open issues for bugs, suggestions, or questions

## License
