#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${YELLOW}Note Taker Installation Script${NC}"
echo -e "--------------------------------"

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed. Please install Python 3 first.${NC}"
    exit 1
fi

# Get Python version properly
python_version=$(python3 --version 2>&1)
echo -e "${GREEN}Found ${python_version}${NC}"

# Installation directories
INSTALL_DIR="$HOME/.local/share/notetaker"
VENV_DIR="$INSTALL_DIR/venv"
BIN_DIR="$HOME/.local/bin"
CONFIG_DIR="$HOME/.config/notetaker"

# Create directories
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
mkdir -o "$CONFIG_DIR"

# Check for notetaker directory structure
if [ -d "../v0.3_a/src" ]; then
    echo "Copying project files..."
    
    mkdir -p "$INSTALL_DIR/src"
    
    # Create root main.py as entry point
    cat > "$INSTALL_DIR/main.py" << 'EOL'
#!/usr/bin/env python3
"""
Note Taker Entry Point
"""
import sys
import os

# Add the installation directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import the main function from the package
from src.main import main

# Execute the main function when this script is run directly
if __name__ == "__main__":
    main()
EOL
    
    # Copy the application files from the correct location
    cp ../v0.3_a/src/main.py "$INSTALL_DIR/src/"
    cp ../v0.3_a/src/interface.py "$INSTALL_DIR/src/"
    cp ../v0.3_a/src/logic.py "$INSTALL_DIR/src/"
    cp ../v0.3_a/src/libs.py "$INSTALL_DIR/src/"
    
    # Copy __init__.py if it exists
    if [ -f "v0.3_a/src/__init__.py" ]; then
        cp v0.3_a/src/__init__.py "$INSTALL_DIR/src/"
    else
        # Create __init__.py if it doesn't exist
        cat > "$INSTALL_DIR/src/__init__.py" << 'EOL'
"""Note Taker - Simple note taking utility"""

__version__ = "0.3.0"
EOL
    fi
    
    # Copy README
    if [ -f "v0.3_a/README.md" ]; then
        cp v0.3_a/README.md "$INSTALL_DIR/"
    fi
    
    echo -e "${GREEN}Files copied successfully!${NC}"
else
    echo -e "${RED}Error: Source files not found. Make sure you're running this script from the correct directory.${NC}"
    exit 1
fi

# Create Python virtual environment
echo "Creating Python virtual environment..."
python3 -m venv "$VENV_DIR"
if [ $? -ne 0 ]; then
    echo -e "${RED}Failed to create virtual environment. Make sure the 'venv' module is installed.${NC}"
    echo -e "Try running: ${YELLOW}sudo apt-get install python3-venv${NC} (for Debian/Ubuntu)"
    echo -e "Try running: ${YELLOW}sudo pacman -S python-virtualenv${NC} (for Arch)"
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
"$VENV_DIR/bin/pip" install PyQt5>=5.15.11 pyyaml
if [ $? -ne 0 ]; then
    echo -e "${RED}Failed to install dependencies.${NC}"
    exit 1
fi

# Create launcher script
echo "Creating launcher script..."
cat > "$BIN_DIR/notetaker" << EOL
#!/bin/bash
# Note Taker Launcher
"$VENV_DIR/bin/python" "$INSTALL_DIR/main.py" "\$@"
EOL

chmod +x "$BIN_DIR/notetaker"

# Create desktop entry
echo "Creating desktop entry..."
mkdir -p "$HOME/.local/share/applications/"
cat > "$HOME/.local/share/applications/notetaker.desktop" << EOL
[Desktop Entry]
Name=Note Taker
Comment=Simple note taking utility
Exec=$BIN_DIR/notetaker
Terminal=false
Type=Application
Categories=Utility;
EOL

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo -e "${YELLOW}Note: $HOME/.local/bin is not in your PATH.${NC}"
    echo -e "You may want to add the following line to your .bashrc or .zshrc:"
    echo -e "${GREEN}export PATH=\"\$HOME/.local/bin:\$PATH\"${NC}"
    echo
    echo -e "For now, you can run Note Taker using the full path:"
    echo -e "${GREEN}$BIN_DIR/notetaker${NC}"
else
    echo -e "You can now run Note Taker by typing ${GREEN}notetaker${NC} in your terminal."
fi

echo -e "${GREEN}Note Taker has been successfully installed.${NC}"
echo -e "You can also find Note Taker in your application menu."
echo -e "--------------------------------"
echo -e "${YELLOW}Thank you for installing Note Taker! Please leave your thoughts and suggestions on my Github page.${NC}"
