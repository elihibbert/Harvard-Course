#Create associated dict (dictionary list) with cities, states, and populations
locations = [
    {"City": "Seattle", "State": "Washington", "Population": "755,000"},
    {"City": "New York City", "State": "New York", "Population": "8,258,000"},
    {"City": "Portland", "State": "Oregon", "Population": "630,000"},
]


for L in locations:
    print (L["City"], L["State"], L["Population"], sep=", ")

