import os
import sys

# Check if the submodule exists
SUBMODULE_PATH = os.path.join(os.path.dirname(__file__), "stable_diffusion_prompt_reader")
if not os.path.exists(SUBMODULE_PATH) or not os.listdir(SUBMODULE_PATH):
    # Define colors for better visibility in console
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    RESET = "\033[0m"
    
    # Create a visually distinct error message
    error_message = f"""
{RED}╔══════════════════════════════════════════════════════════════════════════════╗
║                             INSTALLATION ERROR                                ║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}

{YELLOW}SD Prompt Reader Node{RESET} requires additional files that are missing.

{BLUE}The Problem:{RESET}
This node uses a git submodule that wasn't properly initialized during installation.

{BLUE}How to Fix:{RESET}
Run the following commands in your ComfyUI custom_nodes directory:

{YELLOW}cd comfyui-prompt-reader-node
git submodule init
git submodule update{RESET}

{BLUE}Current Directory:{RESET}
{YELLOW}{os.path.dirname(os.path.abspath(__file__))}{RESET}

{BLUE}Alternative Fix:{RESET}
Reinstall using the recursive clone command:

{YELLOW}git clone --recursive https://github.com/receyuki/comfyui-prompt-reader-node.git{RESET}

For more information, please visit:
https://github.com/receyuki/comfyui-prompt-reader-node#installation

{RED}The node will not function until this is resolved.

╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    
    print(error_message)
    print("Submodule check: Missing")
else:
    print("Submodule check: Present")
