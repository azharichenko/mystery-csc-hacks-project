from abc import ABC, abstractmethod


class StatefulApplication(ABC):
    @abstractmethod
    def on_creation(self):
        pass

    @abstractmethod
    def handle_optin(self):
        pass

    @abstractmethod
    def handle_closeout(self):
        pass

    @abstractmethod
    def handle_updateapp(self):
        pass

    @abstractmethod
    def handle_deleteapp(self):
        pass

    @abstractmethod
    def handle_noop(self):
        pass

    @abstractmethod
    @property
    def approval_program(self):
        pass

    @abstractmethod
    @property
    def clear_state_program(self):
        pass
