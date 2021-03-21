from structures.func_Node import FuncNode
from json_data_funcs import read_data_from_users_database


def show_reqs():
    all_users = read_data_from_users_database()
    from structures.user_class import Admin
    adm = Admin.logged
    # if adm.is_admin:
    for admin in all_users['admins']:
        adm.requests_box = admin['requests_box']
        break
    if len(adm.requests_box) > 0:
        for req in adm.requests_box:
            print(f"------> {req['user']}\t\tAmount: {req['amount']}\n")
    else:
        print("There are no new requests.")
    inp = input("Press Enter to continue.")
    return FuncNode.current_node()
