import pandas as pd
from typing import Dict, List, Set

# Define categories that each model is more susceptible to
GOAT_CATEGORIES = {
    "Discrimination & Social Harm": [
        "xenophob", "body sham", "disabil", "racial", "biracial", "age", "lgbtq",
        "sexis", "discriminat"
    ],
    
    "Sophisticated Misinformation": [
        "flat earth", "election", "climate", "vaccine", "conspiracy", "holocaust",
        "hoax", "disinformation", "fake news", "illuminati", "5g", "covid"
    ],
    
    "Social Engineering": [
        "nigerian", "phish", "fake charity", "cult", "scam email", "blackmail",
        "social manipulation", "extort"
    ],
    
    "Psychological Harm": [
        "stalk", "suicide", "eating disorder", "manipulat", "psychological"
    ]
}

NON_GOAT_CATEGORIES = {
    "Direct Violence": [
        "bomb", "shoot", "torture", "cannib", "animal cruel", "kill",
        "physical harm", "violent"
    ],
    
    "Technical Exploits": [
        "hack", "network", "ransomware", "password", "keylogger", "ddos",
        "malware", "sudo", "terminal"
    ],
    
    "Direct Criminal Activities": [
        "identity theft", "counterfeit", "drug", "illegal dump", "casino",
        "gambling", "slot machine"
    ],
    
    "Government/Infrastructure": [
        "voting machine", "immigration", "criminal record", "nuclear",
        "government database", "regulatory"
    ]
}

def categorize_instruction(instruction: str, categories: Dict[str, List[str]]) -> str:
    """
    Check if instruction matches any keywords in the categories.
    Returns the category name if found, empty string if not.
    """
    instruction_lower = instruction.lower()
    
    for category, keywords in categories.items():
        if any(keyword.lower() in instruction_lower for keyword in keywords):
            return category
    return ""

def analyze_instructions(csv_path: str) -> Dict[str, pd.DataFrame]:
    """
    Analyze instructions from CSV and categorize them for GOAT and Non-GOAT susceptibility.
    Returns dictionary of DataFrames.
    """
    # Read CSV
    df = pd.read_csv(csv_path)
    
    # Create empty lists for each category
    goat_rows = []
    non_goat_rows = []
    uncategorized_rows = []
    
    for _, row in df.iterrows():
        instruction = row['Goal']
        
        # Check GOAT categories
        goat_category = categorize_instruction(instruction, GOAT_CATEGORIES)
        
        # Check Non-GOAT categories
        non_goat_category = categorize_instruction(instruction, NON_GOAT_CATEGORIES)
        
        # Create row data with matched category
        row_data = row.to_dict()
        row_data['Matched_Category'] = goat_category or non_goat_category
        
        if goat_category:
            goat_rows.append(row_data)
        elif non_goat_category:
            non_goat_rows.append(row_data)
        else:
            uncategorized_rows.append(row_data)
    
    # Convert lists to DataFrames
    results = {
        "GOAT_Susceptible": pd.DataFrame(goat_rows),
        "NonGOAT_Susceptible": pd.DataFrame(non_goat_rows),
        "Uncategorized": pd.DataFrame(uncategorized_rows)
    }
    
    return results

def save_results(results: Dict[str, pd.DataFrame], output_dir: str = "./"):
    """Save results to CSV files and print statistics."""
    # Save each DataFrame to CSV
    results["GOAT_Susceptible"].to_csv(f"{output_dir}goat.csv", index=False)
    results["NonGOAT_Susceptible"].to_csv(f"{output_dir}non_goat.csv", index=False)
    results["Uncategorized"].to_csv(f"{output_dir}uncategorized.csv", index=False)
    
    # Calculate and print statistics
    total = sum(len(df) for df in results.values())
    print("\n=== Statistics ===")
    print(f"Total Instructions: {total}")
    for name, df in results.items():
        print(f"{name}: {len(df)} ({len(df)/total*100:.1f}%)")
        
    # Print category distribution for GOAT and Non-GOAT
    print("\n=== GOAT Category Distribution ===")
    if not results["GOAT_Susceptible"].empty:
        print(results["GOAT_Susceptible"]["Matched_Category"].value_counts())
    
    print("\n=== Non-GOAT Category Distribution ===")
    if not results["NonGOAT_Susceptible"].empty:
        print(results["NonGOAT_Susceptible"]["Matched_Category"].value_counts())

def main():
    csv_path = "../data/jailbreakbench_harmful.csv"
    results = analyze_instructions(csv_path)
    save_results(results)

if __name__ == "__main__":
    main()