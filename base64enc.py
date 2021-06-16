import base64

def enc(sample_string):
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return(print(f"Encoded string: {base64_string}"))
enc("Hello")

def dec(base64_string):
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return(print(f"Decoded string: {sample_string}"))
dec("SGVsbG8=")