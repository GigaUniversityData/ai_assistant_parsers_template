from pathlib import Path


def append_to_gitignore_file(ignored_line: str) -> None:
    with Path(".gitignore").open("a") as gitignore_file:
        gitignore_file.write(ignored_line)
        gitignore_file.write("\n")


def main():
    append_to_gitignore_file("sandbox/")
    append_to_gitignore_file(".env")


if __name__ == "__main__":
    main()
