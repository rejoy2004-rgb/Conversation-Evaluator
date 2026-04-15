def clean_facet_name(name):
    # remove extra spaces
    name = name.strip()

    # remove numbering like "899. Something"
    if "." in name:
        parts = name.split(".", 1)
        if parts[0].isdigit():
            name = parts[1]

    # remove colon
    name = name.replace(":", "")

    return name.strip()


def load_facets(file_path):
    facets = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines[1:]:  # skip header
        facet = line.strip()

        # ❌ skip invalid / git conflict lines
        if (
            not facet or
            facet.startswith("<<<") or
            facet.startswith("===") or
            facet.startswith(">>>")
        ):
            continue

        # clean facet name
        cleaned = clean_facet_name(facet)

        # add to list
        facets.append(cleaned)

    print(f"Using {len(facets)} facets for evaluation")
    return facets