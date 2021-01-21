def shift_char(ch, shift_amount):
    if not ch.isalpha():
        return ch
    offset = ord('A') if ch.isupper() else ord('a')
    return chr((ord(ch) + shift_amount - offset) % 26 + offset)

def shift(s, shift_amount):
    return ''.join([shift_char(ch, shift_amount) for ch in s])


if __name__ == '__main__':
    text = input('enter text to shift: ')
    shift_amount = int(input('enter the amount to shift: '))
    
    print(shift(text, shift_amount))
