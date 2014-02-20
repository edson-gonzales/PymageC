class SearchDuplicateSolver:
    
    def __init__(self, strategy):
        self.strategy = strategy

    def solver_search_duplicated(self, list_images):
        return self.strategy.search_duplicate(list_images)

    def change_search(self, strategy):
        self.strategy = strategy