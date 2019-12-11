def pad(text, block_size):
    pad_size = block_size - len(text)%block_size
    fit_text = text + chr(pad_size)*pad_size
    return (fit_text,)
    
def main():
    text = "YELLOW SUBMARINE"
    block_size = 20
    print(pad(text, block_size))
main()

