import subprocess

def build_project():
    subprocess.run(["cmake", "-S", ".", "-B", "build"])
    subprocess.run(["cmake", "--build", "build"])

if __name__ == "__main__":
    build_project()
