import csv

fully = []
partially = []
single = []
notes = []

with open('double-blind.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        partial = ""
        full = ""
        restricted = ""
        if row['partial']:
            partial = f"**{row['partial']}**"
        if row['full']:
            full = f"**{row['full']}**"
        if row['restricted']:
            restricted = f"**{row['restricted']}**"
        arxiv_notes = restricted
        if row['notes']:
            notes.append(f"[{row['conference']}] {row['notes']}")
            arxiv_notes = f"{restricted}({len(notes)})"
        if row['url2']:
            if row['notes']:
                arxiv_notes = f"[{restricted}]({row['url2']})({len(notes)})"
            else:
                arxiv_notes = f"[{restricted}]({row['url2']})"
        
        transition_year = row.get('transition_year', '')
        citation = ""
        if row.get('transition_citation', ''):
            citation = f"[Link]({row['transition_citation']})"
        
        row_str = (
            f"| [{row['conference']}]({row['url']}) | {partial} | {full} | "
            f"{arxiv_notes} | {transition_year} | {citation} |"
        )
        
        if row['partial'] == 'Y':
            if row['full'] == 'Y':
                fully.append(row_str)
            else:
                partially.append(row_str)
        else:
            single.append(row_str)

print(
    """| Conference | At least partially double-blind? | Fully double-blind (blind to accept)? | arXiv restricted? | Transition Year | Citation |
| :--        | :--:                             | :--:                                   | :--:            | :--:           | :--:     |
|            |                                  |                                        |                 |                |          |"""
)

print("| _fully double-blind conferences_ | |")
print(*fully, sep='\n')

print("| _partially double-blind conferences_ | |")
print(*partially, sep='\n')

print("| _single-blind conferences_ | |")
print(*single, sep='\n')

print("")
for index, string in enumerate(notes):
    print(f" * ({index+1}): {string}")

print("")
print("[GitHub site](https://github.com/double-blind-reviewing/double-blind-reviewing.github.io)")