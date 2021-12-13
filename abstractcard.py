from abc import ABC, abstractmethod
import LoadImage


class Card(ABC):
    @abstractmethod
    def __init__(self, file_name, value):
        self.image = LoadImage.load_image(file_name)
        self.value = value

    @abstractmethod
    def move(self):
        pass
