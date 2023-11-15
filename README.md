# Text Analysis Tool

## Overview

The Text Analysis Tool is a Python project designed to analyze text documents. It provides functionalities such as word frequency analysis, top N words, character frequency analysis, and palindrome checks. The tool allows users to input their custom text document for analysis

## How to Execute the Project

1. **Extract the Zip File:**

   - Extract it to a directory of your choice

2. **Navigate to the Project Directory:**

   - Open a terminal or command prompt
   - Change to the project directory: `cd path/to/text-analysis-tool`

3. **Run the Text Analysis Tool:**
   - Setup virtual environment
     `python -m venv venv`
   - Activate virtual environment
     `source venv/bin/activate`
   - Install requirements
     `pip install -r requirements.txt`
   - Execute the `text_analysis_tool` using the following command:
     `python main.py`

## How to Enter Inputs

When you run the script, the tool will prompt you for the following inputs:

1. **Text Document Path:**

   - Enter the path of the text document you want to analyze. If the path is invalid or the file is not found, the tool will use the default input file (`default_input.txt`) in the same directory

2. **Palindrome Check:**
   - After the analysis, you can enter a word to check if it is a palindrome

Follow the on-screen instructions to interact with the tool

## Example Usage

Suppose you have a text file named `sample_text.txt` in the project directory. To test the tool with this file, follow these steps:

1. Enter the path of the text document: `sample_text.txt`
2. After analysis, you can enter a word for palindrome check
