import os
import shutil

def on_config(config):
    # This hook safely copies the real directories into the temporary docs environment right before building
    for folder in ['Big-Data', 'Distributed-Systems', 'HPC', 'Introduction-to-ai']:
        if os.path.exists(folder):
            shutil.copytree(folder, os.path.join(config['docs_dir'], folder), dirs_exist_ok=True)
    return config
