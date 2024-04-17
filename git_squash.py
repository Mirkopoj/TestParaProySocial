import subprocess

subprocess.run(["rm", "-rf", ".git"]) 
subprocess.run(["git", "init"]) 
subprocess.run(["git", "add", "-A"]) 
subprocess.run(["git", "commit", "-m", "inicial"]) 
subprocess.run(["git", "remote", "add", "origin", "https://github.com/Mirkopoj/TestParaProySocial.git"]) 
subprocess.run(["git", "push", "-u", "origin", "master", "-f"]) 
