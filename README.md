# Software Testing and Devops 
  # App Description
  - Web application in which we can add notes.
  - User must be logged in in order to use application.
  - **Tools :** Flask - Sqlite3 
  
  ![image](https://user-images.githubusercontent.com/56639521/172022171-ab6cec3c-d4f6-432d-b603-8e8aef8da52d.png)
  
  ![image](https://user-images.githubusercontent.com/56639521/172022129-2c8a90d5-811d-4536-af1f-4e37cef09e08.png)
  
  # Software Testing
  
  1. Unit Testing
  2. Integration Testing
  3. E2E Testing
  4. User Acceptance Testing
  
  ## Unit Testing
  
  - In unit test I tested 8 functions,6 functions in NotesRepo (testShowAllNotes, testNumberOfNotes, testShowNoteById, TestAddNote, TestUpdateNote, TestDelete) and 2 functions in AuthRepo(testSignIn, testSignUp).
  - There are 3 phases to each test:
  
    - Given
    - When
    - Then
    
   - To run unit tests we can use the command : 
   ```
   coverage run -m unittest Tests/UnitTests/test_units.py
   ```
   ![image](https://user-images.githubusercontent.com/56639521/172022026-0a0a8f83-71fd-41d9-ac61-caadb6a5c2d0.png)  
   
   - To see the result of unit tests coverage we can use the commande : 
   ```
    coverage report
   ```
   ![image](https://user-images.githubusercontent.com/56639521/172044870-21b1fd8b-c989-4b08-8aeb-2e27f102f1bb.png)
   
   
   ## Integration Testing
   
   - In Integration test I tested 8 functions (test_register, test_login_page, test_signin_fail, test_signin_success, test_logout, test_notes, test_create_note_page, test_Note_add)
   - There are 3 phases to each test:
    - Given
    - When
    - Then
   - Tests are performed by testing the status code of the response as well as checking if the expected result is included in the response page.     
   
   - To run integration tests along with unit tests we can use the command : 
   ```
   coverage run -m pytest
   ```
   ![image](https://user-images.githubusercontent.com/56639521/172032606-85ab3d4a-08e7-4696-879b-63478b0e3f17.png)
   
   - To see the result of integration tests along with unit tests coverage we can use the commande :
   ```
    coverage report
   ``` 
  ![image](https://user-images.githubusercontent.com/56639521/172045527-5df2034a-4bf0-40e0-ae0e-6a13b054dafa.png)
  
  ## E2E testing
  - In E2E tests I tested 3 functions (test_01_register, test_02_signin, test_03_add_Note).
  - I used Selenium for this test.
  - The navigations by the selenium are saved as screenshots. These screen shots are saved in the file Screenshots.
  - To run e2e tests we can use the command : 
  ```
  coverage run -m unittest Tests/E2E/test_e2e.py
  ``` 
  
![image](https://user-images.githubusercontent.com/56639521/172171641-05e5b328-773a-4823-94b6-57db4348237c.png)


  
  
  ## User Acceptance Testing (UAT)
  - It is divided into 8 sections:
     - UAT Scope
     - UAT Assumptions and Constraints
     - UAT Risks
     - UAT Team Roles & Responsibilities
     - UAT Entry Criteria
     - UAT Requirements-Based Test Cases
     - UAT Test Results
     - Document Signatures


  # Devops CI/CD Pipeline
  ## What is CI CD?
   - CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are      continuous integration, continuous delivery, and continuous deployment.
   ### CI:
   - The workflow had 2 jobs the first one is a Test Job and the second is a Build job.
   - In the test job we test the app with integration tests, unit tests and e2e tests.
   - In the build job we build a docker image and pushed it to docker hub
   
   ![image](https://user-images.githubusercontent.com/56639521/172193606-68d15665-78ca-4180-a2ce-7f0825c2a483.png)

  ### CD
  
  - I added to the  workflow another job : Deploy job
  - For the deployment i used ECS.
  - I created a cluster then a task definition then a service.
  - The service has 3 tasks.
  
  ![image](https://user-images.githubusercontent.com/56639521/172431737-e0aa1659-702a-460c-8585-d2dc18aa3885.png)
  
  
  - You can access to MyNote app by typing this in the browser link 3.8.22.124:5000.

  ![image](https://user-images.githubusercontent.com/56639521/172431469-dd30e787-d204-49aa-9125-1367ccbeef85.png)


