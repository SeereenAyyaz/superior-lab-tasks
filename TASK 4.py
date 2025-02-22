import string

def luhn_algorithm(card_number):
    digits = [int(d) for d in str(card_number)][::-1]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def sort_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    return ' '.join(words)

if __name__ == "__main__":
    
    card_number = "45487525712830366" 
    print(f"Is the card number valid? {luhn_algorithm(card_number)}")
    
    sample_text = "Hello, Earth! How are you?"
    print(f"Text without punctuation: {remove_punctuation(sample_text)}")
    
    sample_sentence = "This is a test sentence for sorting."
    print(f"Sorted sentence: {sort_sentence(sample_sentence)}")
