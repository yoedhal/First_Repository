import json
import pickle

def shift_char(ch, alphabet, k): # Changing the chars accordingly to the current K
    if ch in alphabet:
        index = alphabet.index(ch)
        new_index = (index - k) % len(alphabet)
        return alphabet[new_index]
    return ch # Unlikely but had to make sure

def decode_phrase(phrase, alphabet, k): # Returning new deciphered string accordingly to the current K
    return ''.join(shift_char(ch, alphabet, k) for ch in phrase)

def is_valid(decoded_phrase, lexicon): # Comparing deciphered string has current words with the lexicon
    words = decoded_phrase.split()
    for word in words:
        if word not in lexicon:
           return False # If there is any word that doesn't apply
    return True

def decipher_phrase(phrase, lexicon_filename, abc_filename):
    if not phrase:
        return {"status": 0, "orig_phrase": "", "K": -1} # Default

    with open(abc_filename, 'r', encoding='utf8') as f:
        alphabet = ''.join(f.read().split()) # Make it a string without any spaces

    with open(lexicon_filename, 'rb') as f:
        lexicon = set(pickle.load(f)) # For binary files

    for k in range(26):
        decipher = decode_phrase(phrase, alphabet, k)

        if not decipher.strip():
            continue

        if is_valid(decipher, lexicon): # For the right K
            return {"status": 1, "orig_phrase": decipher, "K": k}

    return {"status": -1, "orig_phrase": "", "K": -1}


students = {'id1': '207106238', 'id2': '322630716'}

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {1, -1, 0}

    if result["status"] == 1:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == -1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 0:
        print("empty phrase")
