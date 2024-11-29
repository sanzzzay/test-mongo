# test-mongo


# also there was some issue with the pip install

# Option 1: Downgrade prompt-toolkit to a compatible version
pip install "prompt-toolkit<3.0.39"

# Option 2: Use a virtual environment (recommended)
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate


#If you're still seeing conflicts, you can force the installation with:
pip install --no-deps prompt-toolkit==3.0.38
pip install pymongo

# Using a virtual environment (Option 2) is the recommended approach
