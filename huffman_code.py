import streamlit as st
import heapq
from collections import defaultdict
import os

# Node class to represent a character and its frequency
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    heap = [Node(char, freq[char]) for char in freq]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Generate Huffman Codes
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    return codes

# Encode text using Huffman codes
def huffman_encode(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes

# Decode Huffman encoded text
def huffman_decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text

# Compress a file using Huffman encoding
def compress_file(text):
    encoded_text, codes = huffman_encode(text)
    return encoded_text, codes

# Decompress a file using Huffman encoding
def decompress_file(encoded_text, codes):
    decoded_text = huffman_decode(encoded_text, codes)
    return decoded_text

# Streamlit GUI
st.title("File Compression Tool using Huffman Encoding")

# Upload file section for compression
st.header("Compress a File")
uploaded_file = st.file_uploader("Upload a text file to compress", type="txt")

if uploaded_file:
    text = uploaded_file.read().decode('utf-8')
    st.write("Original Text:")
    st.text(text)
    
    if st.button("Compress File"):
        compressed_text, codes = compress_file(text)
        st.success("File Compressed Successfully!")
        
        st.write("Compressed Binary Data:")
        st.text(compressed_text)
        
        # Download compressed data and codes as text files
        st.download_button("Download Compressed File", compressed_text, file_name="compressed_file.huff")
        st.download_button("Download Huffman Codes", str(codes), file_name="huffman_codes.txt")

# File upload for decompression
st.header("Decompress a File")
compressed_file = st.file_uploader("Upload a compressed file (.huff)", type="huff")
codes_file = st.file_uploader("Upload Huffman codes file (.txt)", type="txt")

if compressed_file and codes_file:
    compressed_text = compressed_file.read().decode('utf-8')
    codes = eval(codes_file.read().decode('utf-8'))  # Convert the string representation back to dictionary
    
    if st.button("Decompress File"):
        decompressed_text = decompress_file(compressed_text, codes)
        st.success("File Decompressed Successfully!")
        
        st.write("Decompressed Text:")
        st.text(decompressed_text)
        
        # Download decompressed text file
        st.download_button("Download Decompressed File", decompressed_text, file_name="decompressed_file.txt")
