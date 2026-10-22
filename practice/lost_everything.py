class Life:

    def __init__(self):
        # A clean slate is not an empty life; it is space to rebuild.
        self.possessions = []
        self.past = "Everything gone"
        self.resilience = float("inf")
        self.starting_over = True

    def breathe(self):
        return "You are still here."

    def next_step(self):
        return "One day, one moment, one line of code at a time."


me = Life()

print(me.breathe())
print(me.next_step())