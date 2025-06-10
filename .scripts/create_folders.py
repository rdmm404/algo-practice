from pathlib import Path

plan_dir_name = "plan"
solutions_base_dir_name = "solutions"
gitkeep_filename = ".gitkeep"

# Create Path objects for the directories
plan_dir = Path(plan_dir_name)
solutions_base_dir = Path(solutions_base_dir_name)

# Ensure the 'plan' directory exists
if not plan_dir.exists():
    print(f"Error: The '{plan_dir}' directory does not exist.")
    exit()

# Create the base 'solutions' directory if it doesn't exist
solutions_base_dir.mkdir(parents=True, exist_ok=True)

# List all files in the 'plan' directory
for file_path in plan_dir.iterdir():
    if file_path.is_file() and file_path.suffix == ".md":
        # Get the name without the extension (e.g., "01-Arrays")
        topic_name = file_path.stem

        # Construct the full path for the topic directory in 'solutions'
        topic_dir_path = solutions_base_dir / topic_name

        # Create the topic directory
        topic_dir_path.mkdir(parents=True, exist_ok=True)

        # Create the .gitkeep file inside the topic directory
        gitkeep_file_path = topic_dir_path / gitkeep_filename
        gitkeep_file_path.touch()  # Creates an empty file

        print(f"Created directory: {topic_dir_path} with {gitkeep_filename}")

print("\nAll directories and .gitkeep files created successfully!")
