import os
import sys
import shutil

# Try to import ComfyUI-specific modules, but don't fail if they're not available
try:
    import folder_paths
    is_comfyui_environment = True
except ImportError:
    is_comfyui_environment = False

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
    
    # We'll still try to define the required variables to prevent further errors
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
    
    # Exit early - don't try to import from the missing submodule
    __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
else:
    # Normal initialization when submodule exists
    from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    
    __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
    
    WEB_DIRECTORY = "./js"
    
    # Only run ComfyUI-specific code if we're in the ComfyUI environment
    if is_comfyui_environment:
        # remove old directory
        comfy_path = os.path.dirname(folder_paths.__file__)
        old_dir = os.path.join(comfy_path, "web", "extensions", "SDPromptReader")
        if os.path.exists(old_dir):
            shutil.rmtree(old_dir)
