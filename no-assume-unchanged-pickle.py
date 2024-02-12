import os
import subprocess

def unmark_pickle_files_as_assume_unchanged():
    # Find all .pickle files recursively
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pickle'):
                # Construct the file path
                file_path = os.path.join(root, file)
                # Unmark the file as assume unchanged using git update-index
                subprocess.run(['git', 'update-index', '--no-assume-unchanged', file_path])

if __name__ == "__main__":
    unmark_pickle_files_as_assume_unchanged()


# Check with 'git ls-files -v' if files are actually assumed unchanged or not so. H: not assumed unchanged; h: assumed unchanged.
