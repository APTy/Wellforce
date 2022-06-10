import sys
import subprocess


def find_latest_version():
    with open("RELEASES.md", "r") as f:
        for line in f.readlines():
            if line.startswith("##"):
                return line[line.index("[") + 1 : line.index("]")]
    raise Exception("no version found in RELEASES.md")


def main():
    version = find_latest_version()
    answer = input(f"Release version {version}? (yN) ")
    
    # lazy check for version number
    if len(answer) == 0 or answer.lower()[0] != "y":
        print("Aborted due to user input")
        sys.exit(0)
    
    print("Running git add/commit.")
    #subprocess.run("git add RELEASES.md", shell=True)
    #subprocess.run(f"git commit -m {version}", shell=True)
    
    print("Tagging release")
    #subprocess.run(f"git tag -a {version} -m {version}", shell=True)
    
    print("Pushing tags")
    #subprocess.run("git push --follow-tags", shell=True)


main()
