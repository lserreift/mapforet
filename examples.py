#!/usr/bin/env python3
"""
Example usage of the calculator module.
Exemple d'utilisation du module calculateur.

This script demonstrates how to use the calculator functions for various scenarios
that might be relevant in an urban tree management context.
"""

from calculator import add_numbers, add_list, calculate_addition


def main():
    """Demonstrate calculator functionality with tree-related examples."""
    
    print("=== Exemples d'utilisation du calculateur / Calculator Usage Examples ===\n")
    
    # Example 1: Counting trees in different areas
    print("Exemple 1: Comptage d'arbres dans différentes zones")
    print("Example 1: Counting trees in different areas")
    zone_a_trees = 25
    zone_b_trees = 18
    zone_c_trees = 32
    
    total_trees = add_numbers(zone_a_trees, zone_b_trees, zone_c_trees)
    print(f"Zone A: {zone_a_trees}, Zone B: {zone_b_trees}, Zone C: {zone_c_trees}")
    print(f"Total des arbres / Total trees: {total_trees}")
    print()
    
    # Example 2: Adding measurement data
    print("Exemple 2: Addition de données de mesure")
    print("Example 2: Adding measurement data")
    tree_heights = [12.5, 15.2, 8.7, 22.1, 18.9]
    total_height = add_list(tree_heights)
    average_height = total_height / len(tree_heights)
    
    print(f"Hauteurs des arbres / Tree heights: {tree_heights}")
    print(f"Hauteur totale / Total height: {total_height}m")
    print(f"Hauteur moyenne / Average height: {average_height:.2f}m")
    print()
    
    # Example 3: Budget calculations
    print("Exemple 3: Calculs budgétaires")
    print("Example 3: Budget calculations")
    maintenance_cost = "1500 + 2300 + 950 + 1800"
    total_cost = calculate_addition(maintenance_cost)
    
    print(f"Coûts d'entretien / Maintenance costs: {maintenance_cost}")
    print(f"Coût total / Total cost: {total_cost}€")
    print()
    
    # Example 4: Multiple species count
    print("Exemple 4: Comptage par espèces")
    print("Example 4: Species count")
    species_counts = {
        "Chênes / Oaks": 45,
        "Pins / Pines": 32,
        "Tilleuls / Lindens": 28,
        "Platanes / Plane trees": 19,
        "Autres / Others": 16
    }
    
    counts_list = list(species_counts.values())
    total_count = add_list(counts_list)
    
    for species, count in species_counts.items():
        print(f"  {species}: {count}")
    print(f"Total: {total_count} arbres / trees")
    print()
    
    # Example 5: Error handling demonstration
    print("Exemple 5: Gestion des erreurs")
    print("Example 5: Error handling")
    
    try:
        # This will raise an error
        result = add_numbers("not", "numbers")
    except TypeError as e:
        print(f"Erreur détectée / Error caught: {e}")
    
    try:
        # This will also raise an error
        result = calculate_addition("2*3")
    except ValueError as e:
        print(f"Expression invalide / Invalid expression: {e}")
    
    print("\n=== Fin des exemples / End of examples ===")


if __name__ == "__main__":
    main()