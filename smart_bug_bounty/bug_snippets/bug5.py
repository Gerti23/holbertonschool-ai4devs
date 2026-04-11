def parse_tags(raw: str) -> list[str]:
    tags = raw.split(",")

    cleaned = []
    for tag in tags:
        normalized = tag.strip().lower()
        if normalized:
            cleaned.append(normalized)

    # Bug: converting to set loses original order
    return list(set(cleaned))


if __name__ == "__main__":
    print(parse_tags("Python, api, python, backend, Api"))
