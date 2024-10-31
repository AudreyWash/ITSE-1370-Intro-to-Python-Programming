def resources_scanner(package):
    # Use the dir method to list resources
    resources = dir(package)


    # Print each resource
    for resource in resources:
        print(resource)


if __name__ == '__main__':
    import string
    resources_scanner(string)
