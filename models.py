

class Coordinate():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class ValidPath():
    def __init__(self, path) -> None:
        self.path = path

    def __repr__(self) -> str:
        return f"ValidPath<{self.path}>"


class Solution():
    def __init__(self, paths: list[ValidPath], coverage: set[Coordinate]) -> None:
        self.paths = paths
        self.coverage = coverage
