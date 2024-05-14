import re

def split_text(text, max_length):
    chunks = []
    current_chunk = ""
    words = re.findall(r'\S+\s*', text)  # Split text into words including whitespaces
    for word in words:
        if len(current_chunk) + len(word) <= max_length:
            current_chunk += word
            if len(current_chunk) == max_length:  # If the chunk reaches max_length exactly, save it
                chunks.append(current_chunk.strip())
                current_chunk = ""
            else:
                current_chunk += " "  # Add whitespace after the word
        else:
            chunks.append(current_chunk.strip())  # Save the current chunk
            current_chunk = word + " "  # Start a new chunk with the current word
    if current_chunk:  # Add any remaining text to the chunks list
        chunks.append(current_chunk.strip())
    return chunks

def export_chunks(chunks, file_prefix):
    for i, chunk in enumerate(chunks):
        with open(f"{file_prefix}_{i+1}.txt", "w", encoding="utf-8") as file:
            file.write(chunk)

def main():
    max_length = 220
    with open("input.txt", "r", encoding="utf-8") as file:
        text = file.read()
    chunks = split_text(text, max_length)
    export_chunks(chunks, "output")

if __name__ == "__main__":
    main()
