from update_mailing_list import update_mailing_list


def mailinglist_validation_util(filename, output_filename, io_mode):
    """  
    Perform mailing list validation operations.


    Input:
        filename: the name of the input file with the raw mailing list
        output_filename: the name of the final, output CSV file
        io_mode: the I/O operation mode needed for file handling, passed as an array


    Output:
        output_length: the length of the output file
    """
    # Read the mailing list data from the input CSV file
    mailing_list = mlu.read_mailing_list_file(filename, io_mode)
    # Update the mailing list by filtering out unsubscribed and non-corporate email users
    active_users = update_mailing_list(mailing_list)
    # Save the updated mailing list to the output CSV file
    mlu.save_output_file(active_users, output_filename, io_mode)
    # Return the length of the output file
    return len(active_users)


if __name__ == "__main__":
    # Define input and output filenames and I/O mode
    input_filename = 'mailing_list.csv'
    output_filename = 'updated_mailing_list.csv'
    io_mode = ['r+', 'w+']
    # Perform mailing list validation and get the length of the output file
    output_length = mailinglist_validation_util(input_filename, output_filename, io_mode)
    print("Output file length:", output_length)