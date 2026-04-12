def markdown_to_blocks(markdown: str):
    text = markdown.split('\n\n')
    new_text = []
    for t in text:
        n = t.strip()
        if n == '':
            continue
        new_text.append(n)
    return new_text
