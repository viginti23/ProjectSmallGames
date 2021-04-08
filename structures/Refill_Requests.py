from json_data_funcs import read_data_from_users_database, write_data_to_users_database, json_serial
from datetime import datetime, timedelta
import time
from structures.func_Node import FuncNode


class RefRequest:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return RefRequest.create_refill_request(*args)

    @classmethod
    def create_refill_request(cls, usr):
        all_users = read_data_from_users_database()
        administrators = all_users['admins']
        request_id = 0 # TODO place in datebase
        if len(administrators) > 0:
            while True:
                try:
                    request_id += 1
                    amount = int(input("\nHow much do you need?\n"))
                    datetime_details = datetime.now()
                    datetime_details = json_serial(datetime_details)
                    approved = False
                    return {
                        'request_id': request_id,
                        'user': usr.username,
                        'amount': amount,
                        'datetime_details': datetime_details,
                        'approved': approved
                            }
                except ValueError:
                    print("\nEnter a valid number.\n")
                    continue
        else:
            print("\nThere are currently no admins.\n")
            return

    @classmethod
    def send_refill_request_to_admins(cls, usr, request):
        if request:
            usr.sent_request_box.append(request)
            print("\nSending your request to administrators...\n")
            all_users = read_data_from_users_database()
            administrators = all_users['admins']
            for admin in administrators:
                admin['requests_box'].append(request)
                admin['notifications'].append(f"You have a new request from {request['user']}.")
            time.sleep(1)
            write_data_to_users_database(all_users)
            print("\nYour request is now being evaluated.\nIf not denied in 30 minutes, all requests are accepted "
                  "automatically.")
            return

    @classmethod
    def pending_requests_check(cls):
        from structures.user_class import User
        all_users = read_data_from_users_database()
        try:
            rq_box = all_users['admins'][-1]['requests_box']
            print("Checking pending requests...")
            print("\nApproving...\n")
            for req in rq_box:
                created = req["datetime_details"].replace("T", " ")
                then = datetime.strptime(created, '%Y-%m-%d %H:%M:%S.%f')  # '2021-03-25T19:41:54.083887'
                now = datetime.now()
                diff = now - then
                if diff > timedelta(seconds=120):
                    req['approved'] = True
                    print(".")
                    time.sleep(0.25)
            write_data_to_users_database(all_users)
        except IndexError:
            pass
            # print("There are no admins.")

    @classmethod
    def executing_pending_requests(cls):
        all_users = read_data_from_users_database()
        try:
            r_box = all_users['admins'][-1]['requests_box']
            if len(r_box) > 0:
                for i in range(len(r_box)):
                    if r_box[i]['approved']:
                        print("Executing...")
                        RefRequest.execute_request(r_box[i])

                        # Cleaning.
                        administrators = all_users['admins']
                        for admin in administrators:
                            del r_box[i]
                            del admin['notifications'][i]
                        write_data_to_users_database(all_users)
        except IndexError:
            pass
            # print("There are no admins.")

    @classmethod
    def execute_request(cls, req):
        all_users = read_data_from_users_database()
        usrs = all_users['users']
        current_usr = None
        for usr in usrs:
            if usr['username'] == req['user']:
                current_usr = usr
                break
        if req["approved"]:
            current_usr["wallet"] += req["amount"]
            current_usr["notifications"].append(f"Your request for {req['amount']} points has been accepted.")
            print("\nRequest executed.\n")
        else:
            print("The request is not approved!")
        write_data_to_users_database(all_users)
        return

    @classmethod
    def show_reqs(cls, pos_numb=1):
        all_users = read_data_from_users_database()
        from structures.user_class import Admin
        adm = Admin.logged

        # All admins have the same request lists but each admin has their own one.
        # At the end we need to remember to update the rest of the admins' requests lists.
        for admin in all_users['admins']:
            adm.requests_box = admin['requests_box']
            break

        while len(adm.requests_box) > 0:

            total_requests_money = 0

            for req in adm.requests_box:
                total_requests_money += int(req['amount'])
                date_dets = req['datetime_details'].split("T")
                req['datte'] = date_dets[0]
                ttime = date_dets[1].split(".")
                req['ttime'] = ttime[0]
                req['position'] = pos_numb
                pos_numb += 1
                print(f"\n{req['position']})\t"
                      f"\n{req['user']}\nAmount: {req['amount']}\n{str(req['approved'])}"
                      f"\nSubmitted: {req['datte']}" 
                      f" {req['ttime']}\n\n")
            pos_numb = 1
            print(f"Total money requested: {total_requests_money}\n")

            choice = input("\nEnter the positional number to accept or refuse a single requests.\n"
                           "Enter A to accept all requests.\n"
                           "Enter R to refuse all requests.\n\n"
                           "Enter B to go back.\n")

            try:
                choice = int(choice)
                try:
                    chosen_req = adm.requests_box[choice - 1]
                except IndexError:
                    print("Please choose a valid request.")
                    continue

                # if choice in range(len(adm.requests_box)):
                #     chosen_req = adm.requests_box[choice-1]
                while True:
                    print(f"{chosen_req['position']})\t"
                          f"{chosen_req['user']}\t\tAmount: {chosen_req['amount']}"
                          f"\t{str(chosen_req['approved'])}\n "
                          f"Submitted: {chosen_req['datte']} {chosen_req['ttime']}\n\n")

                    inp = input("Enter A to accept or R to refuse.\n"
                                "Enter B to go back.\n")

                    if inp.lower() == 'b':
                        return FuncNode.current_node()
                    elif inp.lower() == 'a':
                        chosen_req['approved'] = True
                        RefRequest.execute_request(chosen_req)
                        return FuncNode.current_node()
                    elif inp.lower() == 'r':
                        del chosen_req
                        write_data_to_users_database(all_users)
                        return FuncNode.current_node()
                    else:
                        print("Choose valid option.")
                        continue
                continue

            except ValueError:
                if choice.lower() == "r":
                    for req in adm.requests_box:
                        req['approved'] = False
                        del req
                    print("Requests deleted.")
                elif choice.lower() == "a":
                    for req in adm.requests_box:
                        req['approved'] = True
                        RefRequest.execute_request(req)
                    print("Requests accepted and executed.")
                for ad in all_users['admins']:
                    ad['requests_box'] = adm.requests_box
                write_data_to_users_database(all_users)
                if choice.lower() == "b":
                    return FuncNode.current_node()

        else:
            print("\nThere are no new requests.")
            inp = input("\nPress Enter to continue.")
        return FuncNode.current_node()
