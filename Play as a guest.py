# if user.logged_in to zawartość i view Play są dopasowane do zalogowanego użytkownika (np. Witaj X!), plus moduły Moje
# Konto, a w nim: my high scores, my wallet, change password

from Node import Node

play_as_a_guest = {}

PlayAsAGuest = Node("Play as a guest", play_as_a_guest)

# PlayAsAGuest.add_options()