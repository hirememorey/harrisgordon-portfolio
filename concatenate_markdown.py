#!/usr/bin/env python3
"""
Script to concatenate all markdown files in the project into a single .txt file.
"""

import os
import glob
from pathlib import Path

def concatenate_markdown_files():
    """Find all .md files and concatenate them into a single .txt file."""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Find all markdown files in the project
    md_files = glob.glob(str(script_dir / "*.md"))
    
    # Sort files for consistent output
    md_files.sort()
    
    # Output file
    output_file = script_dir / "concatenated_markdown.txt"
    
    print(f"Found {len(md_files)} markdown files:")
    for file in md_files:
        print(f"  - {os.path.basename(file)}")
    
    # Concatenate all markdown files
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, md_file in enumerate(md_files):
            filename = os.path.basename(md_file)
            
            # Add separator between files
            if i > 0:
                outfile.write("\n" + "="*80 + "\n\n")
            
            # Add file header
            outfile.write(f"FILE: {filename}\n")
            outfile.write("="*80 + "\n\n")
            
            # Read and write file content
            try:
                with open(md_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    if not content.endswith('\n'):
                        outfile.write('\n')
            except Exception as e:
                print(f"Error reading {md_file}: {e}")
                outfile.write(f"[Error reading file: {e}]\n")
    
    print(f"\nConcatenated markdown files saved to: {output_file}")
    print(f"Total files processed: {len(md_files)}")

if __name__ == "__main__":
    concatenate_markdown_files()
