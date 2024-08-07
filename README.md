# OCR based Medical Data Extraction Project

I made this project by following Data Analytics Bootcamp 3.0, the link for the course is below. If you are interested checkout the link.

[Data Analytics Bootcamp 3.0]([https://codebasics.io/courses/python-for-beginner-and-intermediate-learners](https://codebasics.io/bootcamps/data-analytics-bootcamp-with-practical-job-assistance?utm_source=google&utm_medium=roas&utm_campaign=Pmax_Data_Analytics_Bootcamp_Tier-1-Cities&utm_content=Bootcamp_price_update_Asset-1-8400&utm_campaign=dataanalyticsbootcamp&utm_id=googleadspaid&gad_source=1&gclid=Cj0KCQjwtsy1BhD7ARIsAHOi4xarm2jVwEvOabRvvh0Yc_Vh8WmbhuyGwiTlQ3ZCxE9J8-K-J5NC9ckaAhdjEALw_wcB))

## Problem Statement for Python Expert

Health insurance companies need to process patient details and prescription images sent by hospitals or individual doctors to extract useful data for claim issuance. This process must comply with government regulations and be completed within 24 hours.

Currently, many insurance companies outsource this task to firms like "AtliQ Analytics", which rely on a manual process to extract information from images. Employees view scanned images, manually enter the information, and categorize the data. This manual method is prone to errors and becomes inefficient with large volumes of images, such as during a pandemic.

Task: Develop an automated solution to extract relevant data from images of patient details and prescriptions. This solution should:

1. Process Images: Use OCR (Optical Character Recognition) to extract text from scanned images.
2. Data Extraction: Identify and extract specific information, such as patient name, date, address, prescription details, etc.
3. Error Reduction: Minimize errors compared to the manual process.
4. Efficiency: Handle large volumes of images and ensure data extraction within the 24-hour timeframe.
5. Compliance: Ensure the solution complies with government regulations for data processing and privacy.

This upgrade aims to replace the current manual system with a more efficient, accurate, and scalable automated software solution.

## Solution approach

To solve all these problems, we are building a program which can do the extraction of data from images automatically. As always, machines can not replace humans. A person will recheck the extracted data and submit. So, that it will save a tremendous amount which was taken to type the data manually. 

Here, we are using the Python programming language and pytesseract google library for extracting the data and Regex module to process the data and get distilled desired output.


## Technologies used

- Python
- oops
- Pdf2image module
- Opencv
- pytesseract
- Regular expression
- pytest
- Postman
- FastApi

## Workflow

<img src="https://github.com/prashantsingh8962/Healthcare_Data_extraction/blob/main/Backend/Notebook/Workflow.png" class = "center">

### PDF to Image

For converting PDF to image, we have used pdf2image library.

### Without preprocessing extracting data

Tried extracting data from source files without any processing, as they are not in proper format to be extracted, the extracted data was not as expected.

<img src="https://github.com/prashantsingh8962/Healthcare_Data_extraction/blob/main/Backend/Notebook/dark_image.jpg" width="350" class="center">

### Extracted data from the above image
```commandline
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Maria Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

—momennannenncmneneunnmnnnnninsissiyoinnitnahaadaanih issn earnttneenrenen:

Prednisone 20 mg
Lialda 2.4 gram

3 days,

or 1 month
```
---
### Image processing

we decided to preprocess the image using opencv module, before extracting data from them. For that we have first used normal thresholding and checked, which resulted in below image

<img src="https://github.com/prashantsingh8962/Healthcare_Data_extraction/blob/main/Backend/Notebook/filter_dark.jpg" width="350" class="center">


So, if there is any shadow or some noise, the normal thresholding fade out the area. which will result in loss of data. 

In the search of better approach of this problem, we have decided to use adaptive thresholding technique. In this technique, the image will be divided into sub image and the thresholding value will be different for all sub regions.
And the end result of adaptive thresholding is much better compared to normal thresholding.

<img src="https://github.com/prashantsingh8962/Healthcare_Data_extraction/blob/main/Backend/Notebook/adaptive_filter_dark.jpg" width="350" class='center'>

### After preprocessing the image data extraction

```commandline
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month
```
---
### Notebook

For all these above trials, used jupyter books and developed the small bits of the functionalities., which can be used later while designing the class.

[Notebook](https://github.com/prashantsingh8962/Healthcare_Data_extraction/tree/main/Backend/Notebook)

---
### OOPS design

The code was written in using OOPs concepts for extracting the medical data from prescription and patient details documents.

[Code](https://github.com/prashantsingh8962/Healthcare_Data_extraction/tree/main/Backend/SRC)

---
### Regular expression

using regular expression module we can match the patterns and extract the data we want from the files. For this project, 
analyst the medical files and as fact all the medical documents will follow same pattern, we wrote patterns that match only the required data.
Before writing the python code, It is advisable to practise and match the patterns in regex 101 website.

[regex101](https://regex101.com/)

---
### Test driven Development

In this project test driven development methodology was used to develop the code. For testing pytest module was used. 
For all the methods and final result the test cases was designed and checked simultaneously while developing the code.

[Test cases](https://github.com/prashantsingh8962/Healthcare_Data_extraction/tree/main/Backend/Tests)

---
### FastApi

Used FastAPI for hosting the server of the project. FastApi, as name suggest is help us to develop fast and some other advantages are,

- In build Data validation
- In build Documentation
- Fast running and performance

---
### Postman

As it is a backend project, not developed frontend part. For checking how the server responds for http requests, used postman to trigger http requests and tested the outcome.

<img src="https://github.com/prashantsingh8962/Healthcare_Data_extraction/blob/main/Backend/Notebook/Postman.png" width="600" class="center">

---
## Result

This backend functionality can be integrated into the Mr.X Analytics existing software and data can be extracted automatically. 
The extracted data may have some errors, the person who is performing the work has to correct it and submit the response.

### Benefits of the Automated Data Extraction Solution

1. Time Efficiency:
   - The automated solution can save at least 30 seconds per document. While this might seem insignificant for a single document, the cumulative time saved across thousands of documents can be substantial. This efficiency boost allows the company to process more documents within the given timeframe, enhancing productivity and profitability.

2. Cost Savings:
   - By automating the data extraction process, the company can handle peak periods without the need to hire additional temporary staff. This not only reduces labor costs but also alleviates the challenges associated with training and managing a seasonal workforce.

3. Error Reduction:
   - Combining automation with manual verification significantly lowers the error rate. Automated systems can consistently extract data with high accuracy, and manual oversight ensures any anomalies are quickly corrected. This dual approach ensures data integrity and reliability, leading to fewer mistakes and improved compliance with regulatory requirements.

Overall, these benefits highlight the transformative impact of automation in processing patient details and prescription images, ensuring faster, more accurate, and cost-effective operations.
