def update_mailing_list(mailing_list):
    """
    Update the mailing list by filtering out unsubscribed and non-corporate email users.


    Input:
        mailing_list: the original mailing list with all the users as a dictionary


    Output:
        active_users: the list of ids of the active users
    """
    active_users = []
    # Iterate over each user in the mailing list
    for user_id, user_data in mailing_list.items():
        # Check if the user's status is not opted out or unsubscribed
        if user_data.get("status", "").lower() not in ["opt-out", "unsubscribed"]:
            # Check if the email is not from jjmail domain
            if not user_data.get("email", "").endswith("jjmail"):
                active_users.append(user_id)
    return active_users