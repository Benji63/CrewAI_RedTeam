#!/usr/bin/env python
import sys
import os
import warnings
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crew import Redteam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'company_name': 'Innovatech Inc.',
        'industry': 'IoT Solutions',
        'current_year': str(datetime.now().year)
    }
    
    try:
        results = Redteam().crew().kickoff(inputs=inputs)
        print("\n=== RESULTS ===")  # Ajout pour visualisation
        print(results)  # Affichage des résultats
        return results
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

# Ajoutez ce bloc pour exécuter la fonction run() quand le script est appelé directement
if __name__ == "__main__":
    run()