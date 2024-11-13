import shutil
import os

def deploy():
    if os.path.exists("build"):
        shutil.copytree("build", "deployment", dirs_exist_ok=True)
        print("Deployment successful!")
    else:
        print("Build directory not found. Please run build first.")

if __name__ == "__main__":
    deploy()
