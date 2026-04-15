def clean_facet_name(name):
    """
    Clean facet names:
    - remove numbering (e.g., '899.')
    - remove colons
    - strip spaces
    """
    #Remove leading/trailing spaces
    name = name.strip()

    # remove numbering like "899. "
    if "." in name:
        parts = name.split(".", 1)
        if parts[0].isdigit():
            name = parts[1]

    # remove colon
    name = name.replace(":", "")
    #remoce extra spaces again
    return name.strip()


def load_facets(file_path):

    """
    Load and preprocess facet list from CSV file.

    Input:
    - file_path: path to CSV file containing facets

    Output:
    - List of cleaned facet names (supports 300–5000 facets)
    """
    facets = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # skip header row and process remaning lines
    for line in lines[1:]:
        facet = line.strip()
        #ignore empty lines
        if facet:
            cleaned = clean_facet_name(facet)
            facets.append(cleaned)

            #Print number of facets loaded

    print(f"Using {len(facets)} facets for evaluation")
    return facets