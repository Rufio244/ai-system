import subprocess

def rollback():
    print("Rolling back...")

    subprocess.run(["git", "checkout", "HEAD~1"])
    subprocess.run(["docker-compose", "up", "-d"])

    print("Rollback complete")
