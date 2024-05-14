import re

def replace_math_symbols(text):
    symbol_callouts = {
        '∧': ' up arrow ',
        '∨': ' down arrow ',
        '¬': ' rotated L ',
        '⇒': ' right double arrow ',
        '⇔': ' left and right double arrow ',
        '∴': ' three dots triangle ',
        '∣': ' vertical bar ',
        '∀': ' upside down A ',
        '∃': ' backwards E ',
        '■': ' solid black square ',
        '□': ' hollow square ',
        '∈': ' epsilon or E symbol ',
        '⊆': ' subset symbol ',
        '∪': ' union symbol ',
        '∩': ' intersection symbol ',
        'A': ' an A symbol ',
        '∅': ' empty set symbol ',
        '∖': ' set difference symbol ',
        '×': ' multiplication symbol ',
        'N': ' capital N ',
        '^(-1)': ' negative exponent 1',
        'Z': ' capital Z ',
        '◦': ' bubbled circle ',
        '¹': ' exponent 1 ',
        'Q': ' capital Q ',
        'R': ' capital R ',
        '→': 'right arrow',
        '≤': ' less than or equal to ',
        '≥': ' greater than or equal to ',
        '<': ' less than ',
        '>': ' greater than ',
        
        'C': ' capital C ',
        'P(A)': ' power set of A '
    }
    
    pattern = '|'.join(map(re.escape, sorted(symbol_callouts, key=len, reverse=True)))
    return re.sub(pattern, lambda m: symbol_callouts[m.group()], text)

# Example usage
original_text = "∀x∈R(x2≥0)"
tts_friendly_text = replace_math_symbols(original_text)
print(tts_friendly_text)
