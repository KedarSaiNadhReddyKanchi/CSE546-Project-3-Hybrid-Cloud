# Group Project3 : Hybrid Cloud OpenFaas

## CSE 546: Cloud Computing Project

Group members:

- Atul Prakash - 1225542214
- Abhi Teja Veresi- 1225506321
- Kedar Sai Nadh Reddy Kanchi - 1225297164

<hr>

S3 bucket names: `cc-input-546` and `cc-output-546`

Credentials:

aws_access_key_id = `AKIAQOZDHDE5H5YOCBIJ `

aws_secret_access_key = `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`

Config: `region=us-east-1`

AWS ID: `kkanchi@asu.edu`

AWS Password: `CSE535CloudComputingAWSProjectAccountPasswordForKedarSaiNadhReddyKanchi@Fall2023`

IAM role: `CSE546PROJECT2ROLE  - arn:aws:iam::031749249338:role/CSE546PROJECT2ROLE`

PEM key -

-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAjdSQjUgeEix0JzyAf15lz5uWNrYx8BaMsS1VzEGUHnn4EdxV
6gmFlrSfnkGWNV/RV9ZlqYyLT09VyBTvJIFtVRWRl7k3vOA72bfXRg5fZLz9LmsQ
Tk+KpEefLPU4D5Z3a/uQIwfg8455NXbTDvo5iO8raT91W1y+dQZaI2z9xA/yLIlU
zWoDO64RCjrfHK/VQWzv0Ir98DPXiPlSjofG7xChIIVQDn1fMhWktb1zhN2Stael
WZ4MwTflsRgOMKWwBOQ8T1XXB+gYvWj+XUGJt1XckIB7D5ygmzsdUcds1nUanRD7
yL72m99Psvq6/lDo6U6kUsAxbOQgtv//32NP1wIDAQABAoIBABXdx8uAauJyaBYE
hesdKqUvX6FfxaM2VsqaKrgrBCMOuuhGCBjlDuuFPXawte/UrfnU3Cefu3qmyJro
X1ZJfgm4IZI6xBUinReb+FycqqhlWsNlTkZEjSN2x1uvEs2UbSUAy+AavtvOA3Hy
t+d/PI+YECFR304Opm50ZEFB9H3dnGo3/MqM+4phBJArQbmfCY3meQ+FgKvQl+Lo
BIrHkGScW7coVMT5fnwdMyZWrDtxZbMhzwWHQ9c7ciNoHaf44VKxydvqRo4DSHVC
TU7/9qBhlYa/Kwfx1gcFMwTVEo91nrl9c8A1qKsOKgEbGeOG4N6v8uB2f7kP/1PL
TiGgKsECgYEA0+wftUWH5mHg+R8Gn2Cov6pArlFfaSrel08sHS9w4RZWDP5zsdBj
aaXYx4W2diUH6fRzjyJwDdruZ3GpOSeqyA4dWP17I1ktASd6o/bRAZsXNMFyU+Id
rJGTFpr1/P0NcLLANI0zMm7uX1dy3mSXxwO+QxZcN9aKURqM5U1MQ2sCgYEAq1Re
GEVa9yqPTJavo/GE4ChMtoA4WIm1o3TJkvG8Au2wO6uYGytLh/O4UnTlev1i6BUh
YnHNEwEPfQ+KXxDsE6el7738sQpNEbGhQ95MtyBLEp5+MlkncRO1jg+YSwwSyCOS
UVM5p2AMlFqXMMCe362Zqf3tMVa2bmzz95UsbEUCgYEAmXl5hSfzwa7E5OXJQAca
bqP378ZSmLFJPr9BrWk8EGbCrupgEzhdppdLJUP63hj3YEF+pvxDtmUFHrk72n6V
ugguzNHWKcVdSGa09KW8u7L73WLzTziEUQOkSEy1NSB2aVWqyOQxXabkzvtf3xtu
p9xYH/HDm1SuGwplW3Lddj0CgYBph3LZwkZwfZ98TkhrU8VDiK8PrlSGfHQL9VB/
mTP0HdFyP5RWD8nbOIxtBaGfqtk0GGfSykPFk96lamARhEvVI2s7CyvNJIop/t5U
/mUEWvjCxCr4+h8oMDqhAQwOFaav7fEe9INLjAbTjiUYG10Aa1597XEe9ckypRt0
gUa2fQKBgQCb5PTYSGDSNlyYt5ynDSrF2RleTJPeF1gFco6MQMuRThZBJWipTLkl
+ojr7hfTnb+1trMre0zQtL1AcNA4zgU3bT4z8LsV8Cf2tyOOzwGUQLJ0pDBerpN4
HD/YY0A3PLgYjWdxKNUX1CTRcPP49wrtp05n7c3LgZLs4x+2fHp+yQ==
-----END RSA PRIVATE KEY-----

<hr>

## Member Tasks

### Atul Prakash - **(ASU ID: 1225542214)**

* ****Deploy OpenFaas to Minikube**:** I have worked on the setup part with respect to deploying OpenFaas to minikube. I have followed each of the 10 steps in order to achieve the desired result. There were a few errors that came up which I have resolved successfully by using some of the good solutions available online.
* **Trigger to the OpenFaas function:** I have worked on the trigger file which is used to trigger the OpenFaas function everytime a new file is uploaded into the S3 input bucket.
* **Report and Readme creation:** Helped in writing the report using the provided template and also created the README file which contains the details of the installation requirements and the steps to run the application.

### Abhi Teja Veresi – (ASU ID: 1225506321)

* ****AWS EC2 Virtual Machine Setup**:** In order for the entire team to work on one system, we have decided to create an AWS EC2 Instance and use that as our common virtual machine. So, I have created the instance using the Ubuntu Platform. I have created a new IAM role with the permission policies for this project.
* **Minikube start:** I have worked on setting up the minikube required for the OpenFaas. I have followed each and every step as mentioned in the canvas description to complete the setup. There were a few errors which have come up with respect to the docker when i tried to execute the command minikube start. But following a good stack overflow article I was able to resolve this issue and successfully execute the minikube start command.
* **Report and Readme creation:** Helped in writing the report for testing and code sections in it using the provided template.

### Kedar Sai Nath Reddy Kanchi-  (ASU ID: 1225297164)

- **Creating a new OpenFaas Function:** Firstly, I have worked on creating a new OpenFaas function following the articles given to us in the canvas description. As mentioned in the article, the OpenFaas CLI template engine built-in can create new functions in a given programming language. Therefore, before creating a new function I pulled in the official OpenFaaS language templates from GitHub via the templates repository.  Then, finally I used the new command to create a new open faas function.
- **Setting the code for the OpenFaas function:** I have used the python template for creating the OpenFaas function. Post the creation of the new OpenFaas function, I worked on making the docker build required for this project.
- **Code Generation:** I worked on the handler.py file which by default gets built with the handle function. Firstly, I worked on the handle function, which would first take in the payload json that is sent to the handler.py file from the trigger file when the OpenFaas function is invoked. Then I proceeded to firstly download the video in my tmp directory that I have created in my working system. Then, I proceeded to delete the video file from the input bucket. Then, I accessed the video saved in the tmp directory and then extracted the images from the video using the ffmpeg library. Then using the face_recognition library I worked on comparing the encodings from the extracted image and the encodings given to us in the encodings file. Once a definitive result is returned by the face_recognition library, I proceed to retrieve the data corresponding to that name from the dynamoDB. Finally, I created a csv file and pushed it into the output bucket.
