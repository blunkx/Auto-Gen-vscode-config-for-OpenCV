# Auto-Gen-vscode-config-for-OpenCV
Generating c_cpp_properties.json and tasks.json for using OpenCV in vscode.
# Prerequirement
- Homebrew
- OpenCV 4 or later

    `brew install opencv`
- pkg-config

    `pkg-config`

# How to use?
Make sure you have already installed OpenCV and pkg-config by Homebrew.

Put your `c_cpp_properties.json` and `tasks.json` files in the same directory as the python file.

Execute the gen.py, and then it automatically generate the new JSON file.