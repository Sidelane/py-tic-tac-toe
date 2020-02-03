class Player:
    def __init__(self, char: str):
        self.char = char
        self.has_turned = True
    
    def __repr__(self):
        return f"Player: {self.char} | Has Turned: {self.has_turned}"