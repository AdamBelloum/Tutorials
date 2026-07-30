#!/usr/bin/env bash

# marp-md2slides.sh - Convert Marp Markdown slides to HTML or PDF

# 1. Check if Marp CLI is installed
if ! command -v marp >/dev/null 2>&1; then
    echo "Marp CLI (marp) is not installed."

    read -p "Do you want to try installing Marp CLI globally with npm? [y/N] " answer

    if [[ "$answer" =~ ^[Yy]$ ]]; then
        # Check if npm is available
        if ! command -v npm >/dev/null 2>&1; then
            echo "npm is not installed. Please install Node.js/npm first,"
            echo "then run: npm install -g @marp-team/marp-cli"
            exit 1
        fi

        echo "Installing Marp CLI with npm..."
        if ! npm install -g @marp-team/marp-cli; then
            echo "Installation failed. Please install manually:"
            echo "  npm install -g @marp-team/marp-cli"
            exit 1
        fi
    else
        echo "Please install Marp CLI first, e.g.:"
        echo "  npm install -g @marp-team/marp-cli"
        exit 1
    fi
fi

# 2. Ask the user for the output format
echo "Select output format:"
echo "  1) HTML"
echo "  2) PDF"
read -p "Enter 1 or 2 [1]: " choice

case "$choice" in
    2)
        format="pdf"
        ;;
    ""|1)
        format="html"
        ;;
    *)
        echo "Invalid choice. Defaulting to HTML."
        format="html"
        ;;
esac

# 3. Ask the user for the Markdown file
read -p "Enter the path to your Markdown (.md) file: " mdfile

if [ ! -f "$mdfile" ]; then
    echo "File '$mdfile' not found."
    exit 1
fi

# 4. Prepare output filename
base="${mdfile%.*}"
if [ "$format" = "html" ]; then
    outfile="${base}.html"
    echo "Converting '$mdfile' to HTML (with local files allowed)..."
    marp --html --allow-local-files "$mdfile" -o "$outfile"
else
    outfile="${base}.pdf"
    echo "Converting '$mdfile' to PDF (with local files allowed)..."
    marp --pdf --allow-local-files "$mdfile" -o "$outfile"
fi

# 5. Report result
if [ $? -eq 0 ]; then
    echo "Done. Generated file: $outfile"
else
    echo "Conversion failed."
    exit 1
fi
