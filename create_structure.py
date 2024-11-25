import os

# Define the directory structure
structure = {
    "environments": {
        "dev": ["main.tf", "variables.tf", "terraform.tfvars", "backend.tf"],
        "prod": ["main.tf", "variables.tf", "terraform.tfvars", "backend.tf"],
        "staging": ["main.tf", "variables.tf", "terraform.tfvars", "backend.tf"],
    },
    "modules": {
        "network": ["main.tf", "outputs.tf", "variables.tf", "README.md"],
        "compute": ["main.tf", "outputs.tf", "variables.tf", "README.md"],
        "security": ["main.tf", "outputs.tf", "variables.tf", "README.md"],
        "storage": ["main.tf", "outputs.tf", "variables.tf", "README.md"],
    },
    "pipelines": ["dev-pipeline.yaml", "prod-pipeline.yaml", "staging-pipeline.yaml"],
    "scripts": ["pre-deploy.sh", "post-deploy.sh"],
    ".gitignore": None,
    "README.md": None,
    "versions.tf": None
}

# Function to create files and directories
def create_structure(base_path, structure):
    for folder, content in structure.items():
        # Create directory
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        # If folder contains subfolders (like 'environments'), call the function recursively
        if isinstance(content, dict):
            create_structure(folder_path, content)
        elif isinstance(content, list):  # for files in the current directory
            for file in content:
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'w') as f:
                    pass  # Create empty file
        elif content is None:  # for .gitignore, README.md, and versions.tf
            file_path = os.path.join(base_path, folder)
            with open(file_path, 'w') as f:
                pass  # Create empty file

# Base path to create the structure (can be customized)
base_path = './terraform_project'

# Create the directory structure
create_structure(base_path, structure)

print(f"Terraform project structure created under: {base_path}")
