from typing import List, Protocol


class Ant(Protocol):

    def do_your_job(self) -> None:
        raise NotImplementedError