**Scenario**

You have been tasked with building a URL file validator for a web crawler. A web crawler is an application that fetches a web page, extracts the URLs present in that page, and then recursively fetches new pages using the extracted URLs. The end goal of a web crawler is to collect text data, images, or other resources present in order to validate resource URLs or hyperlinks on a page. URL validators can be useful to validate if the extracted URL is a valid resource to fetch. In this scenario, you will build a URL validator that checks for supported protocols and file types.

**Introducing a split function:**

A split function is a string method. It is used to create a list of words that is separated by a particular delimiter.

A delimiter can be any character, comma, or space, or any word. For example, a student’s details (that is, name, age, and language) are given as a “John,25,English” string, and if you want to create a list. The string is delimited by “,”:

```
#example-1
	student_detail = “John,25,English”.split(“,”)
	print(student_detail)
	[“John”, “25”, “English”]

#example-2
	student_detail = “John|25|English”.split(“|”)
	print(student_detail)
	[“John”, “25”, “English”]
```

Validation

A URL is in the form of <Protocol>://<hostname>/<fileinfo>. In order to be a valid URL, it must fulfill the following requirements:

Protocol: This can be any value from given list, such as http, https, or ftp.

Hostname: Any string

File extension: fileinfo can be any filename, but it must have an extension from given list (such as .html, .csv, .docx, .jpg, .png, or .gif).

Let’s have a look at a few URL examples below:

Input: https://www.technotification.com/2018/06/best-programming-blog.html

Output: True

Input: rstp://www.technotification.com/2018/06/best-programming-blog.html

Output: False (an invalid protocol)

Input: http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv

Output: True

Input: http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample/

Output: False (an invalid file extension)

    (Problem here is to validate a resource URL, not a valid link.)

URL = <Protocol>://<hostname>/<fileinfo>