import subprocess

CYAN = '\033[96m'
GREEN = '\033[92m'
RESET = "\x1b[0m"

print(f"""{GREEN}Almost done! 🎉🙌
{GREEN}Initializing a git repository... {RESET}""")

try:
    # pipe output to /dev/null for silence
    null = open("/dev/null", "w")
    subprocess.Popen("git", stdout=null, stderr=null)
    null.close()

    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", "Initial commit"])
except OSError:
    print("git not found 😕")

print(f"""{CYAN}Never stop learning! Create and have fun!{RESET}""")
