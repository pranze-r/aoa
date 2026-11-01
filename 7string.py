#1------Naive String Matching-----
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            print("Pattern found at index:", i)


text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

naive_search(text, pattern)

#Rabin–Karp
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    d = 256
    q = 101

    h = pow(d, m - 1, q)

    p = 0
    t = 0

    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

   
    for i in range(n - m + 1):

        
        if p == t:
            if text[i:i + m] == pattern:
                print("Pattern found at index:", i)

        
        if i < n - m:
            t = (d * (t - ord(text[i]) * h)
                 + ord(text[i + m])) % q

            if t < 0:
                t += q



text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

rabin_karp(text, pattern)




#3-------KMP (Knuth–Morris–Pratt)----------
def create_lps(pattern):
    m = len(pattern)

    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = create_lps(pattern)

    i = 0
    j = 0

    while i < n:

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index:", i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:

            if j != 0:
                j = lps[j - 1]

            else:
                i += 1



text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

kmp_search(text, pattern)



#4-------- BOYER-MOORE---------

def bad_char_heuristic(pattern, size):
    bad_char = [-1] * 256
    for i in range(size):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore_search(text, pattern):
    text_lower, pattern_lower = text.lower(), pattern.lower()
    n, m = len(text_lower), len(pattern_lower)
    bad_char = bad_char_heuristic(pattern_lower, m)
    s = 0
    found = False

    while s <= (n - m):
        j = m - 1
        
        while j >= 0 and pattern_lower[j] == text_lower[s + j]:
            j -= 1
            
        if j < 0:
            print(f"Pattern found at index {s}")
            found = True
            s += (m - bad_char[ord(text_lower[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text_lower[s + j])])
            
    if not found:
        print("Pattern not found in the text.")

print("--- Boyer-Moore String Matching ---")
user_text = input("Enter the main text: ")
user_pattern = input("Enter the pattern to search: ")
boyer_moore_search(user_text, user_pattern)

