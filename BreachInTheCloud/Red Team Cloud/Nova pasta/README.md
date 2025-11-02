# 🚀 AWS S3 Enumeration Basics — Breach in the cloud

![level](https://img.shields.io/badge/level-Easy-brightgreen) ![platform](https://img.shields.io/badge/platform-Windows-blue) ![arch](https://img.shields.io/badge/arch-x86__64-orange) ![lang](https://img.shields.io/badge/lang-C%2FC%2B%2B-lightgrey) ![tool](https://img.shields.io/badge/tool-Ghidra-orange)

- **Author:** 
- **Uploaded:** 
- **Difficulty:** Beginner
- **Focus:** Red Team



---

## 🔎 Description
It's your first day on the red team, and you've been tasked with examining a website that was found in a phished employee's bookmarks. Check it out and see where it leads! In scope is the company's infrastructure, including cloud services.

---
## ⚙️ Prerequisites
- Basic Linux command line knowledge 

---
## Info
- S3 buckets are storage containers on Amazon's Simple Storage Service (S3) where you can store files, images, and other data. Think of them like folders on your computer, but they're online and can hold vast amounts of data.
- `` aws s3 ls s3://dev.huge-logistics.com --no-sign-request`` "aws is the name of the tool while s3 is the name of the service we want to interact with. ls is the action that we want to perform, in this case listing the contents. The URL s3://dev.huge-logistics.com refers to the name of the S3 bucket. Note that when listing the bucket, the s3:// doesn't actually have to be specified, but other actions such as cp (to copy files) require this prefix. If we omitted --no-sign-request , it would attempt to use any locally configured AWS credentials. This is because the AWS CLI v2 (the version we have installed) signs requests by default. To send an unsigned request, and test the bucket for public access, we can include the --no-sign-request switch. The default behavior of the AWS CLI v1 was to not sign requests by default."
---

## ▶️ Start
1. Open the Website http://dev.huge-logistics.com 
2. Analyse the source code of the website

<details>
  <summary>Solution (steps)</summary>

3. In the source code we see a link `` <script src="https://s3.amazonaws.com/dev.huge-logistics.com/static/script.js"></script>`` it uses an S3 bucket named dev.huge-logistics.com for storing static files, including images, CSS and JavaScript files
4. On the terminal on linux we have to install the AWS CLI with the command `` apt install awscli``
5. write on the terminal:`` aws s3 ls s3://dev.huge-logistics.com --no-sign-request ``

6. ![alt text](image.png)
7. It seems that both the admin and migration-files directories don't allow public access.
8. we have to open the file `` aws s3 ls s3://dev.huge-logistics.com/shared/ --no-sign-request ``
9. we have to open to the `` hl_migration_project.zip `` open the following :``aws s3 cp s3://dev.huge-logistics.com/shared/hl_migration_project.zip . --no-sign-request``
10. After unzipping the archive with the command unzip hl_migration_project.zip , we see a PowerShell script.
11. ![alt text](image-1.png) 
12. Along with the Access Key and Secret Key with see the region in the script is set to us-east-1 
13. ![alt text](image-2.png)
14. we have to configure the acocunt: ``  aws configure `` put the respective Key ID Access Key and region
15. Run the following:`` aws sts get-caller-identity`` we see a user named pam-test
16. We have to search the admin credencials por privileges ``aws s3 ls s3://dev.huge-logistics.com/migration-files/``
17. ![alt text](image-3.png)
18. Among PDFs related to the migration project are the migration_secrets.ps1 script again, and also a test-export.xml file.
19. We download the xml file``aws s3 cp s3://dev.huge-logistics.com/migration-files/test-export.xml`` 
20. We now have the credencials of the admin
21. ![alt text](image-4.png)
22. Reconfigure the AWS with the admin credencials
23. Now we can open the flag.txt and finish the Lab


</details>