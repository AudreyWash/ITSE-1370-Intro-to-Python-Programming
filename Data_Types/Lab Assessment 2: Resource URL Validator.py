import requests

def validate_url(url):
    valid_protocols = ['http', 'https', 'ftp']
    valid_fileinfo = [".html", ".csv", ".docx"]

    url_split = url.split("://")
    isProtocolValid = False
    isFilevalid = False
    for x in valid_protocols:
        if x in url_split[0]:
            isProtocolValid = True
    
    for x in valid_fileinfo:
        if x in url_split[1]:
            isFilevalid = True
    
    return(isProtocolValid and isFilevalid)
    url = input("Enter the url: ")

    print(validate_url(url))


##### Main #####
if __name__ == '__main__':
    url = input("Enter a URL: ")
    print(validate_url(url))





    """Validates the given url passed as string.
    Arguments:
    url -- String, A valid url should be of form
    <Protocol>://hostmain>/<fileinfo>

    Protocol = [http, https, ftp]
    Hostname = string
    Fileinfo = [.html, .csv, .docx]
    
    """

