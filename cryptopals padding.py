def pkcs7_pad(data, block_size):
    padding_size = (block_size-len(data)) % block_size
    
    if padding_size == 0:
        padding_size = block_size

    padding = (chr(padding_size)*padding_size).encode()
    return data + padding

