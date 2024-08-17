def to_jagex_name(name: str) -> str:
    """Convert a name to Jagex format."""
    return name.lower().replace("_", " ").replace("-", " ").strip()
