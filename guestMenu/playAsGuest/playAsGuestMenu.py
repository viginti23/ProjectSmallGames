# if user.logged_in to zawartość i view Play są dopasowane do zalogowanego użytkownika (np. Witaj X!), plus moduły Moje
# Konto, a w nim: my high scores, my wallet, change password

from structures.menu_Node import MenuNode

play_as_a_guest = {}

PlayAsAGuest = MenuNode("Play as a guest", play_as_a_guest)

# PlayAsAGuest.add_options()