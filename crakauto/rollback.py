import subprocess

def update_system():
    print("Updating system...")

    subprocess.run(["git", "pull"])
    subprocess.run(["docker-compose", "build"])
    subprocess.run(["docker-compose", "up", "-d"])

    print("Update complete")
