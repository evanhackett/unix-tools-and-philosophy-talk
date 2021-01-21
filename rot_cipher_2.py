import argparse

def shift_char(ch, shift_amount):
    if not ch.isalpha():
        return ch
    offset = ord('A') if ch.isupper() else ord('a')
    return chr((ord(ch) + shift_amount - offset) % 26 + offset)

def shift(s, shift_amount):
    return ''.join([shift_char(ch, shift_amount) for ch in s])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt text using a ROT cipher')
    parser.add_argument('text', type=str, help='the text to encrypt/decrypt')
    parser.add_argument('--shift_amount', type=int, default=13, help='the amount to shift by')
    args = parser.parse_args()
    
    print(shift(args.text, args.shift_amount))
