# from json_data_funcs import read_data_from_users_database, write_data_to_users_database, json_serial
# from json_data_funcs import read_data_from_admins_database, write_data_to_admins_database
# from structures.func_Node import FuncNode
#
# from datetime import datetime, timedelta
# import time
# import os
#
#
# class RefRequest:
#     from structures.user_class import User
#     # Creates requests.
#     def __init__(self, user=User.logged, datetime_details=datetime.now(), dictionary=None, *args, **kwargs):
#         self.username = user.username
#         self.amount = 0
#         while self.amount == 0:
#             try:
#                 self.amount = int(input("\nHow much do you need?\n"))
#             except ValueError:
#                 print("\nEnter a valid number.\n")
#                 continue
#         self.approved = False
#         self.datetime_details = json_serial(datetime_details)
#
#         date_dets = self.datetime_details.split("T")
#         if not self.ddate:
#             self.ddate = date_dets[0]
#         if not self.ttime:
#             self.ttime = date_dets[1].split(".")
#             self.ttime = self.ttime[0]
#
#         if dictionary:
#             self.dictionary = dictionary
#             for k in self.dictionary.keys():
#                 setattr(self, k, self.dictionary[k])
#
#         self.req = self.__dict__
#         admins = read_data_from_admins_database()
#         admins['admins_inf']['requests_box'].append(self.req)
#         write_data_to_admins_database(admins)
#
#     def notification_and_request_id_check(self):
#         print("\nSending your request to administrators...\n")
#
#         admins = read_data_from_admins_database()
#
#         # Adding request_id to requests.
#         for r in admins['admins_inf']['requests_box']:
#             if 'request_id' not in r.keys():
#                 admins['admins_inf']['request_id'] += 1
#                 r['request_id'] = admins['admins_inf']['request_id']
#                 write_data_to_admins_database(admins)
#
#         # Adding notifications for admins.
#         admins['admins_inf']['notifications'].append(f"You have a new request from {self.req['username']}.")
#         time.sleep(1)
#         write_data_to_admins_database(admins)
#         print("\nYour request is now being evaluated.\n"
#               "If not denied in 120 seconds, all requests are accepted automatically.")
#         return
#
#     @classmethod
#     def show_requests(cls):
#         admins = read_data_from_admins_database()
#         r_box = admins['admins_inf']['requests_box']
#
#         total_money_requested = 0
#         position = 1
#         for r in r_box:
#             total_money_requested += int(r['amount'])
#
#
#             print(f"\n{position})\t"
#                   f"\n{r['username']}"
#                   f"\nAmount: {r['amount']}"
#                   f"\nApproved: {str(r['approved'])}"
#                   f"\nSubmitted: {r['ddate']}"
#                   f" {r['ttime']}\n\n")
#             position += 1
#         position = 1
#         write_data_to_admins_database(admins)
#         print(f"Total money requested: {total_money_requested}\n")
#
#         inp = input("\nEnter the positional number to browse a single request.\n\n"
#
#                     "Enter A to mark all requests as accepted.\n"
#                     "Enter D to mark all requests as declined.\n\n"
#                     "Enter E to execute all requests."
#
#                     "Enter B to go back.\n")
#         # if int - return given req
#         while True:
#             try:
#                 inp = int(inp)
#                 if inp not in range(1, len(r_box) + 1):
#                     print("Choose valid option.")
#                     time.sleep(2)
#                     continue
#                 else:
#                     return r_box[inp - 1]
#
#             except ValueError:
#                 opts = ["a", "d", "b"]
#                 if inp.lower() in opts:
#                     if inp.lower() == "a":
#                         for req in r_box:
#                             req.approving_request()
#                     elif inp.lower() == "d":
#                         for req in r_box:
#                             req.declining_request()
#                     write_data_to_admins_database(admins)
#                     if inp.lower() == "b":
#                         return FuncNode.current_node() # TODO return?
#                     return ### ????????????
#                 else:
#                     print("Choose valid option.")
#                     time.sleep(2)
#                     continue
#
#     @staticmethod
#     def single_request(req):
#
#         admins = read_data_from_admins_database()
#
#         req = RefRequest(dictionary=req)
#         print(f"\n{req.username}\nAmount: {req.amount}"
#               f"\nApproved: {str(req.approved)}"
#               f"\nSubmitted: {req.ddate} {req.ttime}\n\n")
#
#         while True:
#
#             inp = input("Enter A to accept or D to decline.\n"
#
#                         "You can change your decision until executing chosen requests.\n\n"
#
#
#                         "Enter B to go back.\n").lower()
#
#             opts = ["a", "d", "b"]
#             if inp in opts:
#                 if inp == "a":
#                     req.approving_request()
#                     break
#                 elif inp == "d":
#                     req.declining_request()
#                     break
#                 if inp == "b":
#                     return FuncNode.current_node()  # TODO return?
#             else:
#                 print("Choose valid option.")
#                 time.sleep(2)
#                 continue
#         r_box = admins['admins_inf']['requests_box']
#         for i in range(len(r_box)):
#             if r_box[i]['username'] == req.username and r_box[i]['datetime_details'] == req.datetime_details:
#                 del r_box[i]
#         r_box.append(req.req)
#         write_data_to_admins_database(admins)
#         time.sleep(1.5)
#         return
#
#     def approving_request(self):
#         self.req['approved'] = True
#
#     def declining_request(self):
#         self.req['approved'] = False
#
#     def execute_request(self):
#         users = read_data_from_users_database()
#         admins = read_data_from_admins_database()
#
#         if self.approved:
#
#
#     def run(self):
#
#         while True:
#
#             admins = read_data_from_admins_database()
#             requests_box = admins['admins_inf']['requests_box']
#             os.system('clear')
#             choice = RefRequest.show_requests()
#
#     #
#     # def executing_request(self):
#     #     users = read_data_from_users_database()
#     #     admins = read_data_from_admins_database()
#     #     requests_box = admins['admins_inf']['requests_box']
#     #     for request in requests_box:
#     #         if request['approved']:
#     #
#     #         else:
#     #
#     #
#     #
#     #
#     # def pending_requests(self):
#     #     admins = read_data_from_admins_database()
#     #     req_box = admins['admins_inf']['requests_box']
#     #     if len(req_box) > 0:
#     #         print("Found requests in requests box, checking if 'approved'.")
#     #         for req in req_box:
#     #             if req['approved']:
#     #
#     #             else:
#     #                 created = req["datetime_details"].replace("T", " ")
#     #                 then = datetime.strptime(created, '%Y-%m-%d %H:%M:%S.%f')  # '2021-03-25T19:41:54.083887'
#     #                 now = datetime.now()
#     #                 diff = now - then
#     #                 if diff > timedelta(hours=1, seconds=120):
#     #                     req['approved'] = True
#     #                     print(".")
#     #                     time.sleep(0.25)
#
# # 1. Tworzy requesty.
# # 2. Wysyła do admina - zapisanie do req boxa
# # 3. Przeglądanie listy requestów.
# # 4. Akceptowanie requestów. approved = True
# # 5. Odrzucanie requestów. approved = False
# # 7. Deleting given request from the requests box.
# # 8. Deleting notifications and automatic pending requests check and execution.
# # 9. Mark all as approved.
# # 10. Mark all as declined.
# # 6. Executing requests.
