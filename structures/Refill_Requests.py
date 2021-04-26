from json_data_funcs import read_data_from_users_database, write_data_to_users_database, json_serial
from json_data_funcs import read_data_from_admins_database, write_data_to_admins_database
from structures.func_Node import FuncNode

from datetime import datetime, timedelta
import time
import os


class RefRequest:

    def __init__(self, datetime_details=datetime.now(), dictionary=None):
        from structures.user_class import User
        usr = User.logged
        self.username = usr.username
        self.amount = 0
        while self.amount == 0:
            while True:
                try:
                    self.amount = int(input("\nHow much do you need?\n"))
                    break
                except ValueError:
                    print("\nEnter a valid number.\n")
                    continue

        self.datetime_details = json_serial(datetime_details)
        self.approved = False

        date_details = self.datetime_details.split("T")
        self.ddate = None
        self.ttime = None
        if not self.ddate:
            self.ddate = date_details[0]
        if not self.ttime:
            self.ttime = date_details[1].split(".")
            self.ttime = self.ttime[0]

        if dictionary:
            self.dictionary = dictionary
            for k in self.dictionary.keys():
                setattr(self, k, self.dictionary[k])

        # {
        # 'username': self.username,
        # 'amount': self.amount,
        # 'datetime_details': self.datetime_details,
        # 'approved': self.approved,
        # 'ttime': self.ttime,
        # 'ddate': self.ddate
        #     }

    def save_request_in_reqs_box(self):

        # TODO saving sent request to user's 'sent requests box'
        # users = read_data_from_users_database()
        # for u in users['users']:
        #     if u['username'] == usr.username:
        #         u['sent_request_box'].append(request)
        #         break

        print("\nSending your request to administrators...\n")
        admins = read_data_from_admins_database()
        try:
            print(f"Request number {self.request_id}.")
        except AttributeError:
            admins['admins_inf']['request_id'] += 1
            self.request_id = admins['admins_inf']['request_id']
            print(f"Request number {self.request_id}.")
        admins['admins_inf']['requests_box'].append(self.__dict__)
        # Notifications
        admins['admins_inf']['notifications'].append(f"You have a new request from {self.username}.")
        time.sleep(1)
        write_data_to_admins_database(admins)

        print("\nYour request is now being evaluated.\nIf not denied in 120 seconds, all requests are accepted "
              "automatically.")
        return

    @classmethod
    def print_all_requests(cls):
        admins = read_data_from_admins_database()
        r_box = admins['admins_inf']['requests_box']
        if len(r_box) > 0:
            total_money_requested = 0
            position = 1
            for r in r_box:
                total_money_requested += int(r['amount'])

                print(f"\n{position})\t"
                      f"\n{r['username']}"
                      f"\nAmount: {r['amount']}"
                      f"\nApproved: {str(r['approved'])}"
                      f"\nSubmitted: {r['ddate']}"
                      f" {r['ttime']}\n\n")
                position += 1
            print(f"Total money requested: {total_money_requested}\n")
        else:
            print("No requests to show.")
            time.sleep(2)
        position = 1
        return

    @classmethod
    def get_input_all_reqs_or_get_single_req(cls):
        while True:

            admins = read_data_from_admins_database()
            r_box = admins['admins_inf']['requests_box']
            os.system('clear')
            if len(r_box) > 0:
                RefRequest.print_all_requests()
                inp = input("\nEnter the positional number to browse a single request.\n\n"

                            "Enter A to mark all requests as accepted.\n"
                            "Enter D to mark all requests as declined.\n"
                            "Enter E to execute all requests.\n"
                            "Enter R to go back.\n")

                try:
                    inp = int(inp)
                    if inp not in range(1, len(r_box) + 1):
                        print("Choose valid option.")
                        time.sleep(2)
                        continue
                    else:
                        index = inp - 1
                        return index

                except ValueError:
                    opts = ["a", "d", "r", "e"]
                    inp = inp.lower()
                    if inp not in opts:
                        print("Choose valid option.")
                        time.sleep(2)
                        continue
                    else:
                        if inp == "a":
                            for req in r_box:
                                req['approved'] = True
                                write_data_to_admins_database(admins)
                                continue
                        if inp == "d":
                            for req in r_box:
                                req['approved'] = False
                                write_data_to_admins_database(admins)
                                continue
                        if inp == "r":
                            return FuncNode.current_node()
                        if inp == "e":
                            users = read_data_from_users_database()
                            for r in r_box:
                                for user in users['users']:
                                    if user['username'] == r['username']:
                                        if r["approved"]:
                                            user["wallet"] += r["amount"]
                                            user["notifications"].append(
                                                f"Your request for {r['amount']} points has been accepted.")
                                            print("\nRequest executed.\n")
                                        else:
                                            print("The request is not approved.")
                                            print("Deleting the request.")
                                            time.sleep(3)
                                            user["notifications"].append(
                                                f"Your request for {r['amount']} points has been rejected.")
                                        admins = read_data_from_admins_database()
                                        del admins['admins_inf']['requests_box'][:]
                                        del admins['admins_inf']['notifications'][:]
                                        write_data_to_users_database(users)
                                        write_data_to_admins_database(admins)
            else:
                # print("There are no new requests.")
                time.sleep(2)
                return

    @classmethod
    def browsing_single_request(cls, index):
        admins = read_data_from_admins_database()
        r_box = admins['admins_inf']['requests_box']
        req = r_box[int(index)]
        while True:

            os.system('clear')
            print(f"\n{req['username']}"
                  f"\nAmount: {req['amount']}"
                  f"\nApproved: {str(req['approved'])}"
                  f"\nSubmitted: {req['ddate']}"
                  f" {req['ttime']}\n\n")
            inp = input("Enter A to accept or D to decline.\n"
                        "Enter E to execute the request.\n"
                        "Enter R to go back.\n")

            opts = ['a', 'd', 'r', 'e']

            if inp not in opts:
                print("Choose valid option.")
                time.sleep(2)
                continue
            else:
                if inp == "a":
                    req['approved'] = True
                    write_data_to_admins_database(admins)
                    continue
                if inp == "d":
                    req['approved'] = False
                    write_data_to_admins_database(admins)
                    continue
                if inp == "r":
                    return
                if inp == "e":
                    users = read_data_from_users_database()
                    for user in users['users']:
                        if user['username'] == req['username']:
                            if req["approved"]:
                                user["wallet"] += req["amount"]
                                user["notifications"].append(
                                    f"Your request for {req['amount']} points has been accepted.")
                                print("\nRequest executed.\n")
                            else:
                                print("The request is not approved.")
                                print("Deleting the request.")
                                time.sleep(3)
                                user["notifications"].append(
                                    f"Your request for {req['amount']} points has been rejected.")
                            admins = read_data_from_admins_database()
                            del admins['admins_inf']['requests_box'][index]
                            del admins['admins_inf']['notifications'][index]
                            write_data_to_users_database(users)
                            write_data_to_admins_database(admins)
                return

    #         # except AttributeError or ValueError:
    #         #     print("Choose valid option.")
    #         #     time.sleep(2)
    #         #     os.system('clear')
    #         #     continue
    #         return
    @classmethod
    def show_requests(cls):
        admins = read_data_from_admins_database()
        r_box = admins['admins_inf']['requests_box']
        while len(r_box) > 0:
            os.system('clear')
            index = RefRequest.get_input_all_reqs_or_get_single_req()
            # print(index)
            try:
                RefRequest.browsing_single_request(index)
                continue
            except TypeError:
                break
        print("No requests!\n")
        inp = input("Press Enter to go back.\n")
        FuncNode.current_node()

    @classmethod
    def checking_pending_requests(cls):

        admins = read_data_from_admins_database()
        rq_box = admins['admins_inf']['requests_box']
        if len(rq_box) > 0:
            print("Checking pending requests...")
            for i in range(len(rq_box)):
                created = rq_box[i]["datetime_details"].replace("T", " ")
                then = datetime.strptime(created, '%Y-%m-%d %H:%M:%S.%f')  # '2021-03-25T19:41:54.083887'
                now = datetime.now()
                diff = now - then
                if diff >= timedelta(seconds=120):
                    print("\nApproving...\n")
                    rq_box[i]['approved'] = True
                    print(".")
                    time.sleep(0.25)
                    users = read_data_from_users_database()
                    for user in users['users']:
                        try:
                            if rq_box[i]['username'] == user['username']:
                                if rq_box[i]["approved"]:
                                    user["wallet"] += rq_box[i]["amount"]
                                    user["notifications"].append(f"Your request for {rq_box[i]['amount']} points has been accepted.")
                                    print("\nExecuting...\n")
                                del admins['admins_inf']['requests_box'][i]
                                del admins['admins_inf']['notifications'][i]
                                write_data_to_users_database(users)
                                write_data_to_admins_database(admins)
                                break
                        except IndexError:
                            print("The request has been handled automatically.")
                            time.sleep(2)
                            break
                continue

#
if __name__ == '__main__':
    RefRequest.checking_pending_requests()
