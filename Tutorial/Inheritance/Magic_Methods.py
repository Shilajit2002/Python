class Ball:
    def __init__(self, t, p):
        self.t = t
        self.p = p

    def __str__(self):
        return f"Team Name : {self.t}"

    def __len__(self):
        return self.p


F = Ball("Brazil", 11)
print(F)
print("Total Player :", len(F))
