 # File Compression Tool using Huffman Encoding

This project is a **File Compression Tool** that uses Huffman Encoding to compress and decompress text files. The tool is built with Python and provides a user-friendly interface using **Streamlit**. It allows users to upload text files, compress them, and download the compressed output as well as the corresponding Huffman codes. It also supports decompression of files using the uploaded Huffman codes.

## Features

- Compress text files using Huffman Encoding.
- Download the compressed binary file and the corresponding Huffman codes.
- Decompress previously compressed files using the Huffman codes.
- Simple and intuitive GUI built with Streamlit.

## File Structure

```

huffman_compression_tool/
│
├── huffman_compression.py      # Main Python script containing the Huffman encoding/decoding logic and Streamlit interface
├── input.txt                   # Example text file to compress
├── compressed_file.huff        # Example output file after compression
├── huffman_codes.txt           # Example Huffman codes output file
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── .gitignore                  # Ignore unnecessary files

```


## Installation and Usage

### Prerequisites

- Python 3.x
- Streamlit

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/huffman_compression_tool.git
    ```

2. Navigate to the project directory:
    ```bash
    cd huffman_compression_tool
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

You can run the Streamlit app by using the following command:

```bash
streamlit run huffman_compression.py

