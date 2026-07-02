def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    if not tokens:
        return []

    start, end = 0, min(chunk_size, len(tokens))
    ans = []
    while end <= len(tokens):
        ans.append(tokens[start:end])
        start = (end - overlap)
        end = start + chunk_size
        print(start, end)

    return ans