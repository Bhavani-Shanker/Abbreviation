import streamlit as st

def generate_abbreviations(full_term):
    """
    Generate alternate abbreviations or variations for a given term.
    
    :param full_term: A string like "Horizontal Center of Gravity".
    :return: A list of variations (abbreviations).
    """
    # Split the full term into words
    words = full_term.split()
    
    # List to store the variations
    variations = []
    
    # 1. Full form
    variations.append(full_term)
    
    # Filter out the word "of" to create meaningful abbreviations
    filtered_words = [word for word in words if word.lower() != 'of']
    
    # 2. Abbreviations (initials of each word except "of")
    initials = ''.join([word[0].upper() for word in filtered_words])
    variations.append(initials)
    
    # 3. Variations with partial abbreviations
    # "Horizontal CG", "H Center of Gravity", "H CG", etc.
    if len(filtered_words) > 2:
        variations.append(f"{filtered_words[0]} {initials[1:]}")  # "Horizontal CG"
        variations.append(f"{initials[0]} {filtered_words[1]} of {filtered_words[2]}")  # "H Center of Gravity"
        variations.append(f"{initials[0]} {initials[1]} {filtered_words[2]}")  # "H C Gravity"
        variations.append(f"{initials[0]} {initials[1]} {initials[2]}")  # "HCG"
    
    return variations

# Streamlit app layout
st.title("Generate alternate abbreviations or variations for a given term")

# Input field for user to type the term
full_term = st.text_input("Enter the term", "Horizontal Center of Gravity")

# Button to generate abbreviations
if st.button("Generate Abbreviations"):
    abbreviations = generate_abbreviations(full_term)
    
    # Display the generated abbreviations
    st.subheader("Generated Abbreviations/Variations:")
    for abbr in abbreviations:
        st.write(abbr)
