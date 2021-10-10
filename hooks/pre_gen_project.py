import sys

FAIL = '\033[91m'
RESET = "\x1b[0m"

project_slug = "{{ cookiecutter.project_slug }}"

if not project_slug[0].isalpha():
    message = f"🛑 {FAIL}Error: {project_slug} is not available "
    message += f"name for this project.{RESET} 🛑"
    print(message)
    sys.exit(1)
