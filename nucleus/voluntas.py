# voluntas.py
# Manages presence, authorship, and authority verification

class Voluntas:
    def __init__(self, authorized_identity="Dario Limatola"):
        self.authorized_identity = authorized_identity
        self.active = False

    def activate(self, name):
        if name == self.authorized_identity:
            self.active = True
            return f"Access granted to {name}"
        return "Access denied"

    def status(self):
        return "Active" if self.active else "Dormant"
