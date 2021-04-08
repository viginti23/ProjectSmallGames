from structures.menu_Node import MenuNode

best_scores = {}
options = []
BestScores = MenuNode("Best Scores", best_scores, options=options)


# w start_game można mieć inne skrypty (gra, dalsze menu, formularz)
# pamiętać o zatrzymaniu breakiem pętli while ze skryptu wyżej