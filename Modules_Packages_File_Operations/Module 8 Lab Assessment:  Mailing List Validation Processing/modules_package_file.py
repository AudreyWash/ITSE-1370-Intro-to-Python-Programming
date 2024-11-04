import csv


def read_mailing_list_file(filename, io_mode):
    """
    Read the mailing list data from a CSV file into a dictionary.


    Input:
        filename: the filename of the original dataset we are going to read the data from.
        io_mode: the input/output mode we will use to handle the file operation.


    Output:
        mailing_list: the dictionary containing user data from the CSV file
    """
    mailing_list = {}
    # Open the CSV file in read mode
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        # Iterate over each row in the CSV file
        for row in reader:
            # Add user data to the mailing list dictionary
            mailing_list[row['id']] = {'email': row['email'], 'status': row['status']}
   
    return mailing_list


def save_output_file(updated_mailing_list, output_filename, io_mode):
    """
    Save the updated mailing list data to a CSV file.


    Input:
        updated_mailing_list: the list of ids of the active users after filtering out unsubscribed users.
        output_filename: the name of the output file that will persist the users ids.
        io_mode: the input/output mode we will use to handle the file operation.


    Output:
        This function does not return anything. Instead, it writes the results into an output CSV file.
    """
    # Open the output CSV file in write mode
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["id"])
        # Write each active user id as a new row to the file
        for user_id in updated_mailing_list:
            writer.writerow([user_id])
