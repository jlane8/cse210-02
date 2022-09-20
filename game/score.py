class Score:
    
    def __init__(self):
        self.score = 300

    def choice(self, is_correct):
        if is_correct:
            self.score += 100
        elif not is_correct:
            self.score -= 75
        if self.score <= 0:
            self.score = 0
        return self.score

    def get_score(self):
        return self.score
