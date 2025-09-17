#!/usr/bin/env python3
"""
Calculator module for performing additions.
Module pour calculer des additions.

This module provides functionality to calculate additions, which can be useful
for various calculations in the urban tree management context.
"""


def add_numbers(*args):
    """
    Calculate the sum of multiple numbers.
    Calcule la somme de plusieurs nombres.
    
    Args:
        *args: Variable number of numeric arguments (int, float)
        
    Returns:
        float or int: The sum of all provided numbers
        
    Raises:
        TypeError: If any argument is not a number
        ValueError: If no arguments are provided
        
    Examples:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(1.5, 2.5, 3)
        7.0
        >>> add_numbers(10)
        10
    """
    if not args:
        raise ValueError("Au moins un nombre doit être fourni / At least one number must be provided")
    
    # Verify all arguments are numbers
    for i, arg in enumerate(args):
        if not isinstance(arg, (int, float)):
            raise TypeError(f"L'argument {i+1} n'est pas un nombre / Argument {i+1} is not a number: {arg}")
    
    return sum(args)


def add_list(numbers):
    """
    Calculate the sum of numbers in a list.
    Calcule la somme des nombres dans une liste.
    
    Args:
        numbers (list): List of numeric values
        
    Returns:
        float or int: The sum of all numbers in the list
        
    Raises:
        TypeError: If the input is not a list or contains non-numeric values
        ValueError: If the list is empty
        
    Examples:
        >>> add_list([1, 2, 3, 4])
        10
        >>> add_list([1.5, 2.5])
        4.0
    """
    if not isinstance(numbers, list):
        raise TypeError("L'entrée doit être une liste / Input must be a list")
    
    if not numbers:
        raise ValueError("La liste ne peut pas être vide / List cannot be empty")
    
    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise TypeError(f"L'élément {i+1} de la liste n'est pas un nombre / List item {i+1} is not a number: {num}")
    
    return sum(numbers)


def calculate_addition(expression):
    """
    Calculate addition from a string expression.
    Calcule l'addition à partir d'une expression sous forme de chaîne.
    
    Args:
        expression (str): Addition expression like "2+3+4" or "1.5 + 2.5"
        
    Returns:
        float or int: The result of the addition
        
    Raises:
        ValueError: If the expression is invalid or contains non-addition operations
        
    Examples:
        >>> calculate_addition("2+3")
        5
        >>> calculate_addition("1.5 + 2.5 + 3")
        7.0
    """
    if not isinstance(expression, str):
        raise TypeError("L'expression doit être une chaîne / Expression must be a string")
    
    # Remove spaces and check for valid characters
    clean_expr = expression.replace(" ", "")
    
    if not clean_expr:
        raise ValueError("L'expression ne peut pas être vide / Expression cannot be empty")
    
    # Check if expression contains only numbers, dots, and plus signs
    allowed_chars = set("0123456789+.")
    if not all(c in allowed_chars for c in clean_expr):
        raise ValueError("L'expression contient des caractères non valides / Expression contains invalid characters")
    
    # Split by + and convert to numbers
    try:
        parts = clean_expr.split("+")
        numbers = []
        for part in parts:
            if not part:  # Empty part (e.g., "2++3")
                raise ValueError("Expression invalide / Invalid expression")
            numbers.append(float(part) if "." in part else int(part))
        
        result = sum(numbers)
        # Return int if result is a whole number
        return int(result) if result.is_integer() else result
        
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Expression invalide - impossible de convertir en nombres / Invalid expression - cannot convert to numbers")
        raise


if __name__ == "__main__":
    # Simple CLI interface
    print("=== Calculateur d'additions / Addition Calculator ===")
    print("Exemples / Examples:")
    print("- Nombres séparés: 2 3 4")
    print("- Expression: 2+3+4")
    print("- Tapez 'quit' pour quitter / Type 'quit' to exit")
    print()
    
    while True:
        try:
            user_input = input("Entrez votre calcul / Enter your calculation: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Au revoir! / Goodbye!")
                break
            
            if '+' in user_input:
                # Expression mode
                result = calculate_addition(user_input)
                print(f"Résultat / Result: {result}")
            else:
                # Space-separated numbers mode
                numbers = []
                for part in user_input.split():
                    try:
                        numbers.append(float(part) if '.' in part else int(part))
                    except ValueError:
                        raise ValueError(f"'{part}' n'est pas un nombre valide / '{part}' is not a valid number")
                
                if numbers:
                    result = add_numbers(*numbers)
                    print(f"Résultat / Result: {result}")
                else:
                    print("Aucun nombre fourni / No numbers provided")
            
        except (ValueError, TypeError) as e:
            print(f"Erreur / Error: {e}")
        except KeyboardInterrupt:
            print("\nAu revoir! / Goodbye!")
            break
        except EOFError:
            break