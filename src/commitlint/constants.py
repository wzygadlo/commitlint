"""This module defines constants used throughout the application."""
import os

# Define default value
DEFAULT_HEADER_MAX_LENGTH = 72

# Create a function to get header max length dynamically
def get_header_max_length():
    """Get the maximum header length from environment or use default."""
    return int(os.environ.get("COMMIT_HEADER_MAX_LENGTH", DEFAULT_HEADER_MAX_LENGTH))

COMMIT_TYPES = (
    "build",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "style",
    "test",
    "chore",
    "revert",
    "bump",
)

IGNORE_COMMIT_PATTERNS = (
    r"^((Merge pull request)|(Merge (.*?) into (.*?)|(Merge branch (.*?)))(?:\r?\n)*$)|"
    r"^(Merge tag (.*?))(?:\r?\n)*$|"
    r"^(R|r)evert (.*)|"
    r"^(Merged (.*?)(in|into) (.*)|Merged PR (.*): (.*))$|"
    r"^Merge remote-tracking branch(\s*)(.*)$|"
    r"^Automatic merge(.*)$|"
    r"^Auto-merged (.*?) into (.*)$|"
    r"[Bb]ump [^\s]+ from [^\s]+ to [^\s]+"
)
